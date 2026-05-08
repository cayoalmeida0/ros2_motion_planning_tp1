#!/usr/bin/env python3

import math
from enum import Enum

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseArray
from sensor_msgs.msg import LaserScan


def quat_to_yaw(x, y, z, w):
    return math.atan2(2.0 * (w * z + x * y), 1.0 - 2.0 * (y * y + z * z))


def wrap_to_pi(a):
    return math.atan2(math.sin(a), math.cos(a))


def clamp(v, vmin, vmax):
    return max(vmin, min(v, vmax))


class State(Enum):
    MOVE_TO_GOAL = 0
    FOLLOW_OBSTACLE = 1
    GOAL_REACHED = 2


class TangentBugNode(Node):
    def __init__(self):
        super().__init__("tangent_bug_node")

        self.declare_parameter("goal_x", 0.0)
        self.declare_parameter("goal_y", 0.0)
        self.declare_parameter("pose_topic", "/ld90_gt_pose")
        self.declare_parameter("scan_topic", "/scan")
        self.declare_parameter("cmd_vel_topic", "/cmd_vel")

        self.declare_parameter("v_max", 1.0)
        self.declare_parameter("w_max", 0.5)
        self.declare_parameter("kp_heading", 1.5)
        self.declare_parameter("kp_wall", 1)

        self.declare_parameter("goal_tolerance", 0.02)
        self.declare_parameter("front_block_distance", 1.5)
        self.declare_parameter("wall_follow_distance", 0.1)
        self.declare_parameter("discontinuity_threshold", 0.4)
        self.declare_parameter("heuristic_epsilon", 0.02)

        self.goal_x = float(self.get_parameter("goal_x").value)
        self.goal_y = float(self.get_parameter("goal_y").value)

        self.v_max = float(self.get_parameter("v_max").value)
        self.w_max = float(self.get_parameter("w_max").value)
        self.kp_heading = float(self.get_parameter("kp_heading").value)
        self.kp_wall = float(self.get_parameter("kp_wall").value)

        self.goal_tolerance = float(self.get_parameter("goal_tolerance").value)
        self.front_block_distance = float(self.get_parameter("front_block_distance").value)
        self.wall_follow_distance = float(self.get_parameter("wall_follow_distance").value)
        self.discontinuity_threshold = float(self.get_parameter("discontinuity_threshold").value)
        self.heuristic_epsilon = float(self.get_parameter("heuristic_epsilon").value)

        pose_topic = str(self.get_parameter("pose_topic").value)
        scan_topic = str(self.get_parameter("scan_topic").value)
        cmd_vel_topic = str(self.get_parameter("cmd_vel_topic").value)

        self.x = None
        self.y = None
        self.yaw = None
        self.scan = None

        self.state = State.MOVE_TO_GOAL
        self.best_h_last = None
        self.d_followed = float("inf")

        self.create_subscription(PoseArray, pose_topic, self.pose_callback, 10)
        self.create_subscription(LaserScan, scan_topic, self.scan_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, cmd_vel_topic, 10)

        self.create_timer(0.05, self.control_loop)

        self.get_logger().info(
            f"Tangent Bug iniciado. Goal=({self.goal_x:.2f}, {self.goal_y:.2f})"
        )

    # -------------------------
    # Callbacks
    # -------------------------
    def pose_callback(self, msg):
        if not msg.poses:
            return
        p = msg.poses[0]
        self.x = p.position.x
        self.y = p.position.y
        self.yaw = quat_to_yaw(
            p.orientation.x, p.orientation.y, p.orientation.z, p.orientation.w
        )

    def scan_callback(self, msg):
        self.scan = msg

    # -------------------------
    # Utilidades
    # -------------------------
    def publish_cmd(self, v, w):
        cmd = Twist()
        cmd.linear.x = clamp(v, -self.v_max, self.v_max)
        cmd.angular.z = clamp(w, -self.w_max, self.w_max)
        self.cmd_pub.publish(cmd)

    def stop(self):
        self.publish_cmd(0.0, 0.0)

    def goal_distance(self):
        return math.hypot(self.goal_x - self.x, self.goal_y - self.y)

    def goal_angle_world(self):
        return math.atan2(self.goal_y - self.y, self.goal_x - self.x)

    def goal_angle_robot(self):
        return wrap_to_pi(self.goal_angle_world() - self.yaw)

    def sector_min(self, center_angle, half_width_deg):
        if self.scan is None:
            return float("inf")

        half_width = math.radians(half_width_deg)
        vals = []

        for i, r in enumerate(self.scan.ranges):
            if not math.isfinite(r):
                continue
            if r < self.scan.range_min or r > self.scan.range_max:
                continue

            ang = self.scan.angle_min + i * self.scan.angle_increment
            if abs(wrap_to_pi(ang - center_angle)) <= half_width:
                vals.append(r)

        return min(vals) if vals else float("inf")

    def goal_visible(self):
        if self.scan is None:
            return False
        a = self.goal_angle_robot()
        return self.scan.angle_min <= a <= self.scan.angle_max

    def goal_blocked(self):
        if not self.goal_visible():
            return True

        d_goal = self.goal_distance()
        d_dir = self.sector_min(self.goal_angle_robot(), 18.0)
        return d_dir < min(d_goal, self.front_block_distance)

    def scan_points_world(self):
        pts = []
        if self.scan is None or self.x is None or self.y is None or self.yaw is None:
            return pts

        for i, r in enumerate(self.scan.ranges):
            if not math.isfinite(r):
                continue
            if r < self.scan.range_min or r > self.scan.range_max:
                continue

            ang = self.scan.angle_min + i * self.scan.angle_increment
            a = self.yaw + ang
            px = self.x + r * math.cos(a)
            py = self.y + r * math.sin(a)
            pts.append((i, r, px, py))

        return pts

    def visible_boundary_min_goal_distance(self):
        pts = self.scan_points_world()
        if not pts:
            return float("inf")
        return min(math.hypot(self.goal_x - px, self.goal_y - py) for _, _, px, py in pts)

    def detect_discontinuities(self):
        if self.scan is None or self.x is None or self.y is None or self.yaw is None:
            return []

        out = []
        rs = self.scan.ranges

        for i in range(len(rs) - 1):
            r1, r2 = rs[i], rs[i + 1]
            f1, f2 = math.isfinite(r1), math.isfinite(r2)

            choose = None
            idx = None

            if f1 and f2 and abs(r2 - r1) > self.discontinuity_threshold:
                if r1 < r2:
                    choose, idx = r1, i
                else:
                    choose, idx = r2, i + 1

            elif f1 != f2:
                if f1:
                    choose, idx = r1, i
                else:
                    choose, idx = r2, i + 1

            if choose is not None:
                ang = self.scan.angle_min + idx * self.scan.angle_increment
                a = self.yaw + ang
                ox = self.x + choose * math.cos(a)
                oy = self.y + choose * math.sin(a)
                out.append((idx, ox, oy))

        return out

    def best_discontinuity(self):
        cands = self.detect_discontinuities()
        if not cands:
            return None

        best = None
        best_h = float("inf")

        for idx, ox, oy in cands:
            h = math.hypot(ox - self.x, oy - self.y) + math.hypot(self.goal_x - ox, self.goal_y - oy)
            if h < best_h:
                best_h = h
                best = (idx, ox, oy, h)

        return best

    # -------------------------
    # Comportamentos
    # -------------------------
    def move_to_goal(self):
        d_goal = self.goal_distance()
        if d_goal < self.goal_tolerance:
            self.get_logger().info("Goal reached.")
            self.state = State.GOAL_REACHED
            self.stop()
            return

        if not self.goal_blocked():
            e = wrap_to_pi(self.goal_angle_world() - self.yaw)
            v = min(self.v_max, 0.8 * d_goal)
            w = self.kp_heading * e
            self.publish_cmd(v, w)
            self.best_h_last = None
            return

        best = self.best_discontinuity()
        if best is None:
            self.publish_cmd(0.0, 0.4)
            return

        _, ox, oy, h = best
        desired = math.atan2(oy - self.y, ox - self.x)
        e = wrap_to_pi(desired - self.yaw)

        v = min(0.15, 0.5 * math.hypot(ox - self.x, oy - self.y))
        w = self.kp_heading * e
        self.publish_cmd(v, w)

        if self.best_h_last is not None and h > self.best_h_last - self.heuristic_epsilon:
            self.state = State.FOLLOW_OBSTACLE
            self.d_followed = self.visible_boundary_min_goal_distance()
            self.get_logger().info(
                f"Entrando em FOLLOW_OBSTACLE | d_followed={self.d_followed:.3f}"
            )
            return

        self.best_h_last = h

    def follow_obstacle(self):
        d_goal = self.goal_distance()
        if d_goal < self.goal_tolerance:
            self.get_logger().info("Goal reached.")
            self.state = State.GOAL_REACHED
            self.stop()
            return

        d_reach = self.visible_boundary_min_goal_distance()
        if d_reach < self.d_followed:
            self.get_logger().info(
                f"Voltando para MOVE_TO_GOAL | d_reach={d_reach:.3f} < d_followed={self.d_followed:.3f}"
            )
            self.state = State.MOVE_TO_GOAL
            self.best_h_last = None
            return

        self.d_followed = min(self.d_followed, d_reach)

        d_front = self.sector_min(0.0, 20.0)
        d_front_left = self.sector_min(math.radians(45.0), 18.0)
        d_left = self.sector_min(math.radians(65.0), 15.0)

        if d_front < self.front_block_distance or d_front_left < self.front_block_distance:
            self.publish_cmd(0.06, -0.45)
            return

        if not math.isfinite(d_left) or d_left > 2.0:
            self.publish_cmd(0.10, 0.25)
            return

        e_wall = self.wall_follow_distance - d_left
        self.publish_cmd(0.12, self.kp_wall * e_wall)

    # -------------------------
    # Loop principal
    # -------------------------
    def control_loop(self):
        if self.x is None or self.y is None or self.yaw is None or self.scan is None:
            return

        if self.state == State.GOAL_REACHED:
            self.stop()
            return

        if self.state == State.MOVE_TO_GOAL:
            self.move_to_goal()
        else:
            self.follow_obstacle()


def main(args=None):
    rclpy.init(args=args)
    node = TangentBugNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            if rclpy.ok():
                node.stop()
        except Exception:
            pass

        if rclpy.ok():
            node.destroy_node()
            rclpy.shutdown()


if __name__ == "__main__":
    main()
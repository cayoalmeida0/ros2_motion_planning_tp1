"""*****************************************************************************
* IMPORTS
*****************************************************************************"""
import rclpy
from rclpy.node import Node
import math
from tf_transformations import euler_from_quaternion
from geometry_msgs.msg import Twist, PoseArray
from sensor_msgs.msg import LaserScan
import numpy as np

"""*****************************************************************************
* DEFINES
*****************************************************************************"""
FEEDBACK_LINEARIZATION_L = 0.3

ATTRACTIVE_GAIN = 1
REPULSIVE_GAIN = 1
REPULSIVE_THRESHOLD = 2.0
MAX_SPEED = 1.0


VELOCITY_TOPIC = "/cmd_vel"
SCAN_TOPIC = "/scan"
POSE_TOPIC = "/ld90_gt_pose"


"""*****************************************************************************
* HELPER CLASSES
*****************************************************************************"""

class Pose2D:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0

    def update_from_msg(self, p):
        self.x = p.position.x
        self.y = p.position.y
        quat = [p.orientation.x, p.orientation.y, p.orientation.z, p.orientation.w]
        self.yaw = euler_from_quaternion(quat)[2]


"""*****************************************************************************
* NODE CLASS
*****************************************************************************"""
class PotentialFieldsNode(Node):
    # Constructor --------------------------------------------------------------
    def __init__(self):
        super().__init__("curve_follower_node")
        self.pose = Pose2D()
        self.scan:LaserScan = None
        self.create_subscription(PoseArray, POSE_TOPIC, self.pose_callback, 10)
        self.vel_publisher = self.create_publisher(Twist, VELOCITY_TOPIC, 10)
        self.create_subscription(LaserScan, SCAN_TOPIC, self.scan_callback, 10)

        self.create_timer(0.05, self.control_loop)
        self.goal = (6.0,0)


    # Callbacks ----------------------------------------------------------------
    def pose_callback(self, msg):
        p = msg.poses[0]
        self.pose.update_from_msg(p)

    def scan_index_to_rad(self, index):
        if self.scan is None:
            return None
        return self.scan.angle_min + (index * self.scan.angle_increment)    
        

    def get_min_closest_obstacle(self,scan):
        if self.scan is None or len(self.scan.ranges) == 0:
            return (float('inf'), 0.0)

        ranges = np.array(self.scan.ranges)
        ranges[(ranges < self.scan.range_min) | (ranges > self.scan.range_max)] = float('inf')

        min_dist = np.min(ranges)
        
        if min_dist == float('inf'):
            return (float('inf'), 0.0)

        min_index = np.argmin(ranges)
        angle = self.scan_index_to_rad(min_index)

        return (min_dist, angle)

    def control_loop(self):
        if self.scan is None:
            return

        attr_vx, attr_vy = self.get_attractive_force(self.goal)

        dist, local_angle = self.get_min_closest_obstacle(self.scan)
        rep_mag = self.get_repulsive_force_magnitute(dist)
        
        rep_angle_global = self.local_angle_to_global_angle(local_angle) + math.pi
        rep_vx, rep_vy = self.decompose_vector(rep_mag, rep_angle_global)

        total_vx = attr_vx + rep_vx
        total_vy = attr_vy + rep_vy

        current_magnitude = math.sqrt(total_vx**2 + total_vy**2)

        if current_magnitude > MAX_SPEED:
            scaling_factor = MAX_SPEED / current_magnitude
            total_vx *= scaling_factor
            total_vy *= scaling_factor

        v, w = self.inverse_fl(total_vx, total_vy)

        self.publish_vel(v, w)

    def decompose_vector(self, magnitude, angle):
        fx = magnitude * math.cos(angle)
        fy = magnitude * math.sin(angle)
        return (fx, fy)

    def local_angle_to_global_angle(self, angle):
        return self.pose.yaw + angle

    def stop(self):
        self.publish_vel(0.0, 0.0)

    def publish_vel(self, v, w):
        cmd = Twist()
        cmd.linear.x = v
        cmd.angular.z = w
        self.vel_publisher.publish(cmd)

    def inverse_fl(self, vx_h, vy_h):
        theta = self.pose.yaw
        l = FEEDBACK_LINEARIZATION_L
        v = math.cos(theta) * vx_h + math.sin(theta) * vy_h
        omega = (-math.sin(theta) * vx_h + math.cos(theta) * vy_h) / l
        
        return (v, omega)

    def get_attractive_force(self,goal):
        fx = -ATTRACTIVE_GAIN*(self.pose.x-goal[0])
        fy = -ATTRACTIVE_GAIN*(self.pose.y-goal[1])
        return (fx,fy)

    def get_repulsive_force_magnitute(self,dist):
        if dist > REPULSIVE_THRESHOLD:
            return 0
        return REPULSIVE_GAIN*(1/dist-1/REPULSIVE_THRESHOLD)*1/(dist**2)

    def scan_callback(self, msg):
        self.scan = msg




def main(args=None):
    rclpy.init(args=args)
    node = PotentialFieldsNode()

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
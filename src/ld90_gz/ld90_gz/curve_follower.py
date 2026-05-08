"""*****************************************************************************
* IMPORTS
*****************************************************************************"""
import rclpy
from rclpy.node import Node
from rclpy.time import Time
import math
from tf_transformations import euler_from_quaternion
from geometry_msgs.msg import Twist, PoseArray


"""*****************************************************************************
* DEFINES
*****************************************************************************"""
CONTROLLER_K = 1.0

FEEDBACK_LINEARIZATION_L = 0.1
CURVE_SIZE_MULTIPLIER = 3.0
CURVE_TIME_MULTIPLIER = 0.2 

VELOCITY_TOPIC = "/cmd_vel"
POSE_TOPIC = "/ld90_gt_pose"
MAX_SPEED = 1.0


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


class SpeedTracker:
    def __init__(self):
        self.current_pose = Pose2D()
        self.prev_pose = Pose2D()
        self.vx = 0.0
        self.vy = 0.0
        self.v_yaw = 0.0
        self.last_time = None

    def update(self, pose_msg, time):        
        quat = [
            pose_msg.orientation.x, 
            pose_msg.orientation.y, 
            pose_msg.orientation.z, 
            pose_msg.orientation.w
        ]
        new_yaw = euler_from_quaternion(quat)[2]
        if self.last_time is not None:
            dt = (time - self.last_time).nanoseconds / 1e9
            
            if dt > 0:
                new_x = pose_msg.position.x
                new_y = pose_msg.position.y
                
                self.vx = (new_x - self.current_pose.x) / dt
                self.vy = (new_y - self.current_pose.y) / dt

                delta_yaw = new_yaw - self.current_pose.yaw
                delta_yaw = math.atan2(math.sin(delta_yaw), math.cos(delta_yaw))
                self.v_yaw = delta_yaw / dt

        self.current_pose.update_from_msg(pose_msg)
        self.last_time = time

    def get_point_speed(self):
        return self.vx, self.vy
    
    def get_yaw_speed(self):
        return self.v_yaw






"""*****************************************************************************
* NODE CLASS
*****************************************************************************"""
class CurveFollowerNode(Node):
    # Constructor --------------------------------------------------------------
    def __init__(self):
        super().__init__("curve_follower_node")
        self.pose = Pose2D()
        self.speed_trk = SpeedTracker()
        self.create_subscription(PoseArray, POSE_TOPIC, self.pose_callback, 10)
        self.vel_publisher = self.create_publisher(Twist, VELOCITY_TOPIC, 10)
        self.create_timer(0.05, self.control_loop)


    # Callbacks ----------------------------------------------------------------
    def pose_callback(self, msg):
        now_time = self.get_clock().now()
        p = msg.poses[0]
        self.pose.update_from_msg(p)
        self.speed_trk.update(p,now_time)


    def control_loop(self):
        now_time = self.get_clock().now()
        vx_total,vy_total = self.get_correction_fl_point_speed(now_time)
        current_magnitude = math.sqrt(vx_total**2 + vy_total**2)
        if current_magnitude > MAX_SPEED:
            scaling_factor = MAX_SPEED / current_magnitude
            vx_total *= scaling_factor
            vy_total *= scaling_factor

        diff_speeds = self.inverse_fl(vx_total,vy_total)
        self.publish_vel(diff_speeds[0],diff_speeds[1])

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


    def get_correction_fl_point_speed(self,time:Time):
        desired_speed = self.get_curve_velocity_at_time(time)
        position_error = self.get_position_error(time)
        return tuple(a - CONTROLLER_K* b for a, b in zip(desired_speed, position_error))

    def get_position_error(self,time:Time):
        desired_point = self.get_curve_point_at_time(time)
        fl_point = self.get_feedback_linearization_point_position()
        x_error = fl_point[0]-desired_point[0]
        y_error = fl_point[1]-desired_point[1]
        return (x_error,y_error)

    def get_speed_error(self,time):
        desired_speed = self.get_curve_velocity_at_time(time)
        fl_speed = self.get_feedback_linearization_point_speed()
        vx_error = fl_speed[0]-desired_speed[0]
        vy_error = fl_speed[1]-desired_speed[1]
        return (vx_error,vy_error)

    def get_feedback_linearization_point_position(self):
        x = self.pose.x + FEEDBACK_LINEARIZATION_L*math.cos(self.pose.yaw)
        y = self.pose.y + FEEDBACK_LINEARIZATION_L*math.sin(self.pose.yaw)
        return (x,y)
    
    def get_feedback_linearization_point_speed(self):
        center_vx, center_vy = self.speed_trk.get_point_speed()
        vx = center_vx - FEEDBACK_LINEARIZATION_L * math.sin(self.pose.yaw) * self.speed_trk.get_yaw_speed()
        vy = center_vy + FEEDBACK_LINEARIZATION_L * math.cos(self.pose.yaw) * self.speed_trk.get_yaw_speed()
        return (vx,vy)


    def get_curve_point_at_time(self,time:Time):
        
        theta = time.nanoseconds/1e9 *CURVE_TIME_MULTIPLIER
        sin_t = math.sin(theta)
        cos_t = math.cos(theta)
        denom = 1 + sin_t**2

        x = (CURVE_SIZE_MULTIPLIER * cos_t)/denom
        y = (CURVE_SIZE_MULTIPLIER * sin_t * cos_t)/denom
        return (x,y)

    def get_curve_velocity_at_time(self, time:Time):
        
        theta = time.nanoseconds/1e9 * CURVE_TIME_MULTIPLIER
        sin_t = math.sin(theta)
        denom = 1 + sin_t**2
        d_theta = CURVE_TIME_MULTIPLIER
        
        dx_dtheta = CURVE_SIZE_MULTIPLIER * (sin_t * (sin_t**2 - 3)) / (denom**2)
        vx = dx_dtheta * d_theta
        
        dy_dtheta = CURVE_SIZE_MULTIPLIER * (1 - 3 * sin_t**2) / (denom**2)
        vy = dy_dtheta * d_theta
        return (vx, vy)





def main(args=None):
    rclpy.init(args=args)
    node = CurveFollowerNode()

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
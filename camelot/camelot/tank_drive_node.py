#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from camelot_interfaces.msg import DiffDrive
from sensor_msgs.msg import Joy


class TankDriveNode:
    def __init__(self):
        super().__init__("tank_drive_node")
        self.get_logger().info("Started tank_drive_node")

        self.motor_pub = rospy.Publisher(DiffDrive, "motor_cmd", 10)

        self.subscription = self.create_subscription(
            Joy,
            "joy",
            self.joy_callback,
            10)
        self.subscription

    def joy_callback(self, joy):
        motor_msg = DiffDrive()
        motor_msg.r_cmd = joy.axes[1]
        motor_msg.l_cmd = joy.axes[3]

        self.motor_pub.publish(motor_msg)

def main(args=None):
    rclpy.init(args=args)

    tank_drive_node = TankDriveNode()

    rclpy.spin(tank_drive_node)

    tank_drive_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()


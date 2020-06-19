#!/usr/bin/env python3

import rospy

from camelot.msg import DiffDrive
from sensor_msgs.msg import Joy

class TankDriveNode:
    def __init__(self):
        rospy.loginfo("Started tank_drive_node")

        self.motor_pub = rospy.Publisher("motor_cmd", DiffDrive, queue_size=10)
        rospy.Subscriber("joy", Joy, self.joy_callback)

    def joy_callback(self, joy):
        motor_msg = DiffDrive()
        motor_msg.r_cmd = joy.axes[1]
        motor_msg.l_cmd = joy.axes[3]

        self.motor_pub.publish(motor_msg)


if __name__ == "__main__":
    rospy.init_node("tank_drive_node")
    node = TankDriveNode()
    rospy.spin()

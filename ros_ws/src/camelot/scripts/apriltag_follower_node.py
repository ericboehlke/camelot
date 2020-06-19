#!/usr/bin/env python3

import rospy

from camelot.msg import DiffDrive
from sensor_msgs.msg import Joy
from apriltag_ros.msg import AprilTagDetectionArray

class ApriltagFollowerNode:
    def __init__(self):
        rospy.loginfo("Started apriltag_follower_node")

        self.motor_pub = rospy.Publisher("motor_cmd", DiffDrive, queue_size=10)
        rospy.Subscriber("joy", Joy, self.joy_callback)
        rospy.Subscriber("tag_detections", AprilTagDetectionArray, self.tag_callback)
        self.forward_gain = 2.0
        self.difference_gain = 1.5
        self.set_point = 1.0
        self.dead_man = False

    def joy_callback(self, joy):
        self.dead_man = joy.buttons[4]

    def tag_callback(self, tags):
        if len(tags.detections) > 0:
            x = float(tags.detections[0].pose.pose.pose.position.x)
            z = float(tags.detections[0].pose.pose.pose.position.z)

            speed_difference = self.difference_gain * x
            forward_speed = self.forward_gain * (z - self.set_point)
            a = min(1-(abs(forward_speed) + abs(speed_difference/2.0)), 0)
            forward_speed -= a * (-1.0 if forward_speed < 0 else 1.0)

            rospy.loginfo("a=%.2f, z=%.2f, x=%.2f, fs=%.2f, sd=%.2f" % (a, z, x, forward_speed, speed_difference))
            drive = DiffDrive()
            if self.dead_man:
                drive.r_cmd = forward_speed + speed_difference/2 
                drive.l_cmd = forward_speed - speed_difference/2 
            else:
                drive.r_cmd = 0
                drive.l_cmd = 0
            self.motor_pub.publish(drive)

        else:
            stop = DiffDrive()
            stop.r_cmd = 0
            stop.l_cmd = 0
            self.motor_pub.publish(stop)

if __name__ == "__main__":
    rospy.init_node("apriltag_follower_node")
    node = ApriltagFollowerNode()
    rospy.spin()


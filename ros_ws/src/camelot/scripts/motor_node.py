#!/usr/bin/env python3

import rospy
import wiringpi
from camelot.msg import DiffDrive 

class Motor:
    def __init__(self, dirPin, speedPin, forward=1):
        self.dirPin = dirPin
        self.speedPin = speedPin
        self.forward = 1 if forward == 1 else -1
        wiringpi.pinMode(self.dirPin, 1)
        wiringpi.pinMode(self.speedPin, 1)
        wiringpi.softPwmCreate(self.speedPin, 0, 100)

    def setSpeed(self, speed):
        # speed should be from -1 to 1
        speed = max(-1, min(1, speed))
        wiringpi.digitalWrite(self.dirPin, max(0, self.forward*(1 if speed > 0 else -1)))
        wiringpi.softPwmWrite(self.speedPin, int(abs(100*speed)))



class MotorNode:
    def __init__(self, rightMotor, leftMotor):
        self.rightMotor = rightMotor
        self.leftMotor = leftMotor
        rospy.loginfo("Starting motor_node")
        self.count = 0
        rospy.Subscriber("motor_cmd", DiffDrive, self.drive_callback)
        #rospy.Timer(rospy.Duration(0.1), self.timer_callback)

    def drive_callback(self, msg):
        self.count = 0
        self.rightMotor.setSpeed(msg.r_cmd)
        self.leftMotor.setSpeed(msg.l_cmd)

    def timer_callback(self, event):
        self.count += 1
        if self.count > 5:
            self.rightMotor.setSpeed(0)
            self.leftMotor.setSpeed(0)


if __name__ == "__main__":
    rightMotorDir = 27
    leftMotorDir = 28
    rightMotorSpeed = 23
    leftMotorSpeed = 26

    wiringpi.wiringPiSetup()
    rightMotor = Motor(rightMotorDir, rightMotorSpeed, 1)
    leftMotor = Motor(leftMotorDir, leftMotorSpeed, -1)

    def stop_motors():
        rightMotor.setSpeed(0)
        leftMotor.setSpeed(0)

    rospy.init_node("motor_node")
    rospy.on_shutdown(stop_motors)
    node = MotorNode(rightMotor, leftMotor)
    rospy.spin()

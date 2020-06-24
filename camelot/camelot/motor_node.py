#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import wiringpi
from camelot_interfaces.msg import DiffDrive 

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



class MotorNode(Node):
    def __init__(self, rightMotor, leftMotor):
        super().__init__("motor_node")
        self.rightMotor = rightMotor
        self.leftMotor = leftMotor
        self.get_logger().info("Starting motor_node")
        self.count = 0
        self.subscription = self.create_subscription(
            DiffDrive, 
            "motor_cmd", 
            self.drive_callback, 
            10)

    def drive_callback(self, msg):
        self.count = 0
        self.rightMotor.setSpeed(msg.r_cmd)
        self.leftMotor.setSpeed(msg.l_cmd)


def main(args=None):
    rightMotorDir = 28
    leftMotorDir = 27
    rightMotorSpeed = 26
    leftMotorSpeed = 23

    wiringpi.wiringPiSetup()
    rightMotor = Motor(rightMotorDir, rightMotorSpeed, -1)
    leftMotor = Motor(leftMotorDir, leftMotorSpeed, 1)

    def stop_motors():
        rightMotor.setSpeed(0)
        leftMotor.setSpeed(0)
   
    rclpy.init(args=args)

    motor_node = MotorNode(rightMotor, leftMotor) 

    rclpy.spin(motor_node)

    motor_node.destroy_node()
    stop_motors()
    rclpy.shutdown()


if __name__ == "__main__":
    main()


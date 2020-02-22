import wiringpi
import time

rightMotorDir = 28
leftMotorDir = 29
rightMotorSpeed = 23
leftMotorSpeed = 26 

wiringpi.wiringPiSetup()
wiringpi.pinMode(rightMotorDir, 1)
wiringpi.pinMode(leftMotorDir, 1)
wiringpi.pinMode(rightMotorSpeed, 1)
wiringpi.pinMode(leftMotorSpeed, 1)

wiringpi.softPwmCreate(rightMotorSpeed, 0, 100)
wiringpi.softPwmCreate(leftMotorSpeed, 0, 100)

# Start with low power
wiringpi.softPwmWrite(rightMotorSpeed, 10) 
wiringpi.softPwmWrite(leftMotorSpeed, 10) 


while True:
	time.sleep(1)

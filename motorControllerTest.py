import wiringpi
import time

rightMotorDir = 29
leftMotorDir = 28
rightMotorSpeed = 23
leftMotorSpeed = 26 

wiringpi.wiringPiSetup()
wiringpi.pinMode(rightMotorDir, 1)
wiringpi.pinMode(leftMotorDir, 1)
wiringpi.pinMode(rightMotorSpeed, 1)
wiringpi.pinMode(leftMotorSpeed, 1)

wiringpi.softPwmCreate(rightMotorSpeed, 0, 100)
wiringpi.softPwmCreate(leftMotorSpeed, 0, 100)

# Start with low power for 3 seconds
wiringpi.digitalWrite(rightMotorDir, 1)
wiringpi.digitalWrite(rightMotorDir, 1)
  
wiringpi.softPwmWrite(rightMotorSpeed, 10) 
wiringpi.softPwmWrite(leftMotorSpeed, 10) 

time.sleep(3)

# Switch direction
wiringpi.digitalWrite(rightMotorDir, 0)
wiringpi.digitalWrite(leftMotorDir, 0)


time.sleep(3)


wiringpi.softPwmWrite(rightMotorSpeed, 0) 
wiringpi.softPwmWrite(leftMotorSpeed, 0) 

while True:
	time.sleep(1)

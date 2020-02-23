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
wiringpi.digitalWrite(leftMotorDir, 0)
  
wiringpi.softPwmWrite(rightMotorSpeed, 100) 
wiringpi.softPwmWrite(leftMotorSpeed, 100) 

time.sleep(1)

# Switch direction
wiringpi.digitalWrite(rightMotorDir, 0)
wiringpi.digitalWrite(leftMotorDir, 1)


time.sleep(1)


wiringpi.softPwmWrite(rightMotorSpeed, 0) 
wiringpi.softPwmWrite(leftMotorSpeed, 0) 


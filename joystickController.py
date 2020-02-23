import wiringpi
import time
import xbox 

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


rightMotorDir = 29
leftMotorDir = 28
rightMotorSpeed = 23
leftMotorSpeed = 26 


if __name__ == "__main__":
	wiringpi.wiringPiSetup()
	rightMotor = Motor(rightMotorDir, rightMotorSpeed, 1)
	leftMotor = Motor(leftMotorDir, leftMotorSpeed, -1)
	joy = xbox.Joystick()
	
	try:
		while True:
			joyRight, joyLeft = joy.rightY(), joy.leftY()
			print(str(joyLeft) + ", " + str(joyRight))
			rightMotor.setSpeed(joyRight)
			leftMotor.setSpeed(joyLeft)
			time.sleep(0.1)
	except KeyboardInterrupt:
		rightMotor.setSpeed(0)
		leftMotor.setSpeed(0) 



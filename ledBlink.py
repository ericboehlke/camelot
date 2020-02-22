import wiringpi
import time

wiringpi.wiringPiSetup()
pin = 23
wiringpi.pinMode(pin, 1)
wiringpi.softPwmCreate(pin, 0, 100)
wiringpi.softPwmWrite(pin, 20)

while True:
	time.sleep(1)

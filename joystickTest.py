import xbox
import time

joy = xbox.Joystick()

while True:
	print str(joy.rightY()) + ", " + str(joy.leftY())
	time.sleep(.1)

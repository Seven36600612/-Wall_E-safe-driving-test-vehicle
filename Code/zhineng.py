import RPi.GPIO as  GPIO
import importlib
import time
import sys

LedR	=	31
LedG	=	22
LedB	=	16
Buzz	=	12

#导入模块
joystick	=	importlib.import_module('15_joystick_PS2')
ds18b20		=	importlib.import_module('26_ds18b20')
beep		=	importlib.import_module('10_active_buzzer')
rgb			=	importlib.import_module('02_rgb_led')

joystick.setup()
ds18b20.setup()
beep.setup(Buzz)
rgb.setup(LedR, LedG, LedB)

color = {'Red':0xFF0000, 'Green':0x00FF00, 'Blue':0x0000FF}

def setup():
	global lowl, highl
	lowl = 25
	highl = 32

def edge():
	global lowl, highl
	temp = joystick.direction()
	if temp == 'Button pressed':
		destroy()
		quit()
	if temp == 'up' and highl <= 125:
		highl += 1
	if temp == 'down' and lowl < highl-1:
		highl -= 1
	if temp == 'right' and lowl < highl-1:
		lowl += 1
	if temp == 'left' and lowl >= -5:
		lowl -= 1

def loop():
	while True:
		edge()
		temp = ds18b20.read()
		print ('The lower limit of temperature : ', lowl)
		print ('The upper limit of temperature : ', highl)
		print ('Current temperature : ', temp)
		print ('')
		if float(temp) < float(lowl):
			rgb.setColor(color['Blue'])
			for i in range(0, 3):
				beep.beep(0.5)
		if temp >= float(lowl) and temp < float(highl):
			rgb.setColor(color['Green'])
		if temp >= float(highl):
			rgb.setColor(color['Red'])
			for i in range(0, 3):
				beep.beep(0.1)

def destroy():
	beep.destroy()
	joystick.destroy()
	ds18b20.destroy()
	rgb.destroy()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
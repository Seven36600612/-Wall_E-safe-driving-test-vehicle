#!/usr/bin/env python
import RPi.GPIO as GPIO

TouchPin = 35
Rpin   = 12
Gpin   = 13

tmp = 0

def setup():
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
    GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
    GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

def Led(x):     #当手触摸时为高电平1，亮红灯；当拿开手指时为低电平0，亮绿灯
    if x == 0:
        GPIO.output(Rpin, 1)
        GPIO.output(Gpin, 0)
    if x == 1:
        GPIO.output(Rpin, 0)
        GPIO.output(Gpin, 1)


def Print(x):
    global tmp
    if x != tmp:
        if x == 1:  #当手触摸时为高电平，打印Touch ON
            print ('    ************')
            print ('    * Touch ON *')
            print ('    ************')

        if x == 0:  #当拿开手指时为低电平,打印Take OFF
            print ('    ************')
            print ('    * Take OFF *')
            print ('    ************')
        tmp = x

def loop():
    while True:
        print (GPIO.input(TouchPin))  #当手触摸时为高电平1，当拿开手指时为低电平0
        Led(GPIO.input(TouchPin))
        Print(GPIO.input(TouchPin))

def destroy():
    GPIO.output(Gpin, GPIO.LOW)       # Green led off
    GPIO.output(Rpin, GPIO.LOW)       # Red led off
    GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
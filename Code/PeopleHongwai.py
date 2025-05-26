import RPi.GPIO as GPIO
import time
import os
import lirc
makerobo_rgbPins = {'Red':6, 'Green':25, 'Blue':23}
makerobo_pirPin = 18

def makerobo_setup():
    global pir_R,pir_G, pir_B
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(makerobo_pirPin, GPIO.IN)

    for i in makerobo_rgbPins:
        GPIO.setup(makerobo_rgbPins[i], GPIO.OUT, initial=GPIO.HIGH)
    pir_R = GPIO.PWM(makerobo_rgbPins['Red'], 2000)
    pir_G = GPIO.PWM(makerobo_rgbPins['Green'], 2000)
    pir_B = GPIO.PWM(makerobo_rgbPins['Blue'], 2000)

    pir_R.start(0)
    pir_R.start(0)
    pir_R.start(0)

def makerobo_MAP(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def makerobo_setColor(color):
    R_val = (color & 0xFF0000) >> 16
    G_val = (color & 0x00FF00) >> 8
    B_val = (color & 0x0000FF) >> 0

    R_val = makerobo_MAP(R_val, 0, 255, 0, 100)
    G_val = makerobo_MAP(G_val, 0, 255, 0, 100)
    B_val = makerobo_MAP(B_val, 0, 255, 0, 100)

    pir_R.ChangeDutyCycle(R_val)
    pir_G.ChangeDutyCycle(G_val)
    pir_B.ChangeDutyCycle(B_val)

def makerobo_loop():
    sockid = lirc.init("che", "lircrc", blocking=False)
    while True:
        car = lirc.nextcode()
        pir_val = GPIO.input(makerobo_pirPin)
        if pir_val==GPIO.HIGH:
            print ('注意行人！')
        else :
            print ('安全')
        if car == ['KEY_NUMERIC_0']:
            os._exit(0)
def destroy():
    pir_R.stop()
    pir_G.stop()
    pir_B.stop()
    pir.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    makerobo_setup()
    try:
        makerobo_loop()
    except KeyboardInterrupt:
        destroy()
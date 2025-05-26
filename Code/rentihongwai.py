import time
import RPi.GPIO as GPIO
import os
import lirc
BODY_GPIO = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BODY_GPIO, GPIO.IN)

def body_detect():

    signal = GPIO.input(BODY_GPIO)
    if signal == 1:
        print ("注意行人!")
    else:
        print ("安全!")

if __name__ == "__main__":
    count = 0
    sockid = lirc.init("che", "lircrc", blocking=False)
    while True:
        car = lirc.nextcode()
        body_detect()
        time.sleep(3)
        count += 1
        if count == 20:
            break
        if car == ['KEY_NUMERIC_0']:
            os._exit(0)
    GPIO.cleanup()
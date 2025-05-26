import RPi.GPIO as GPIO
import time
import os
import lirc
pin_avoid_obstacle=22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_avoid_obstacle, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if __name__ == '__main__':
    try:
        sockid = lirc.init("che", "lircrc", blocking=False)
        while True:
            car = lirc.nextcode()
            status = GPIO.input(pin_avoid_obstacle)
            if status == False:
                print('我是红外避障模组，没有检测到障碍物，一切正常！')
            else:
                print('我是红外避障模组，检测到障碍物，注意停车')
            time.sleep(0.5)
            if car == ['KEY_NUMERIC_0']:
                os._exit(0)
    except KeyboardInterrupt:
        GPIO.cleanup()
import lirc
import time
import os
import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

IN1 = 32
IN2 = 36
IN3 = 38
IN4 = 40

ranging = False

def init():
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)
    stop()
#前进的代码
def qianjin():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

#后退
def cabk():
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    GPIO.output(IN3,GPIO.HIGH)
    GPIO.output(IN4,GPIO.LOW)

#左转
def right():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,GPIO.LOW)
    GPIO.output(IN4,GPIO.HIGH)

#右转
def left():
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

def stop():
    GPIO.output(IN1,False)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    sockid = lirc.init("che", "lircrc", blocking=False)
    try:
        while True:

            car = lirc.nextcode()
            GPIO.setmode(GPIO.BOARD)

            if car == ['KEY_NUMERIC_5']:
                init()
                time.sleep(0.3)
                stop()

            if car == ['KEY_NUMERIC_2']:
                qianjin()
                time.sleep(0.3)
                stop()
                print ('2')

            if car == ['KEY_NUMERIC_8']:
                cabk()
                time.sleep(0.3)
                stop()
                print ('8')

            if car == ['KEY_NUMERIC_4']:
                left()
                time.sleep(0.5)
                stop()
                print ('4')

            if car == ['KEY_NUMERIC_6']:
                right()
                time.sleep(0.3)
                stop()
                print ('6')

            if car == ['BTN_0']:
                stop()
                print ('stop')

            if car == ['KEY_CHANNELDOWN']:
                os.system('python3 ranging.py')

            if car == ['KEY_CHANNEL']:
                os.system('python3 MQ2.py')

            if car == ['KEY_CHANNELUP']:
                os.system('python3 Read.py')

            if car == ['KEY_PREVIOUS']:
                os.system('python3 max30102.py')

            if car == ['KEY_PLAYPAUSE']:
                os.system('python3 zhineng.py')

            if car == ['KEY_VOLUMEUP']:
                os.system('python3 touch.py')

            if car == ['KEY_VOLUMEDOWN']:
                os.system('python3 bizhang.py')

            if car == ['KEY_NEXT']:
                os.system('python3 rentihongwai.py')

            if car == ['KEY_NUMERIC_1']:
                os.system('python3 01_face_dataset.py')

            if car == ['KEY_NUMERIC_3']:
                os.system('python3 02_face_training.py')

            if car == ['KEY_NUMERIC_7']:
                os.system('python3 dlib_blinks.py')

            if car == ['KEY_NUMERIC_9']:
                os.system('python3 03_face_recognition.py')
    except KeyboardInterrupt:
        destroy()
    finally:
        lirc.deinit()
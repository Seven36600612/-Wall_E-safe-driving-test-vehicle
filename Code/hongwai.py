import RPi.GPIO as GPIO
import time
makerobo_ObstaclePin = 37
def makerobo_setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(makerobo_ObstaclePin, GPIO,IN, pull_up_down=GPIO.PUD_UP)
    def makerobo_loop():
        while True:
            if (0 == GPIO.input(makerobo_ObstaclePin)):
                print ("Makerobo Detected Barrier!")
                time.sleep(0.2)
    def destroy():
        GPIO.cleanup()
    if __name__ == '__main__':
        makerobo_setuo()
        try:
            makerobo_loop()
        except KeyboardInterrupt:
            destroy()
import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, True)
        time.sleep()
        GPIO.output(led_pin, False)
        time.sleep()
except KeyboardInterrupt:
    pass
GPIO.cleanup()
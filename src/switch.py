import RPi.GPIO as GPIO
import time
import uinput

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

device = uinput.Device([
        uinput.KEY_P,
        uinput.KEY_N,
        uinput.KEY_F5,
        ])
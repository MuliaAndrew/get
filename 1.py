import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)

leds_num = [21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds_num, gpio.OUT)

for _ in range(3):
    for num in leds_num:
        gpio.output(num, gpio.HIGH)
        time.sleep(0.2)
        gpio.output(num, gpio.LOW)

gpio.output(leds_num, gpio.OUT)

gpio.cleanup()
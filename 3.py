import RPi.GPIO as g
import time

g.setmode(g.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

aux = [22, 23, 27, 18, 15, 14, 3, 2]

g.setup(leds, g.OUT)

g.setup(aux, g.IN)

## while True:
   ## for i in range(8):
     ##   g.output(leds[i], g.input(aux[i]))

g.output(leds, g.LOW)

g.cleanup()
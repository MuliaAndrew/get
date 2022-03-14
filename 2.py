import RPi.GPIO as g
import time

g.setmode(g.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

num = [0, 1, 1, 1, 1, 1, 1, 1]

g.setup(dac, g.OUT)

g.output(dac, num)

input()
g.cleanup()
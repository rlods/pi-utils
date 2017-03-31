#!/usr/bin/env python

from gpiozero import LED, Button
from time import sleep

led = LED(4)
b1 = Button(14)
b2 = Button(15)

def pressed(b):
	print(str(b.pin.number))
	led.on()

def released(b):
	led.off()

b1.when_pressed = pressed
b2.when_pressed = pressed
b1.when_released = released
b2.when_released = released

while True:
	sleep(1)


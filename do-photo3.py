#!/usr/bin/env python

from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image
from blinkt import set_clear_on_exit, set_brightness, set_pixel, show

set_clear_on_exit()
set_brightness(0.1)

camera = PiCamera()
camera.start_preview()
# Warmup
sleep(2)

while True:
	# Create the in-memory stream
	stream = BytesIO()
	camera.capture(stream, format='jpeg')
	# "Rewind" the stream to the beginning so we can read its content
	stream.seek(0)
	with Image.open(stream) as image:
		image = image.resize((2, 4)).convert('RGB')
		for x in xrange(8):
			r,g,b = image.getpixel((x/4, x%4))
			set_pixel(x, r, g, b)
		show()
	sleep(0.5)

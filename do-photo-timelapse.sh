#!/bin/sh

# 6h = 21600000ms
raspistill -o toto%04d.jpg -tl 5000 -t 21600000 -vf --width 1280 --height 960 -v


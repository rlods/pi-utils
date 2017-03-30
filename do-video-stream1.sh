#!/bin/sh

# http://www.magdiblog.fr/divers/raspberry-pi-camera-5-facons-de-faire-du-streaming/
# access with vlc using http://host:8090
raspivid -t 0 -n -vf --width 640 --height 360 -o - | cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8090}' :demux=h264


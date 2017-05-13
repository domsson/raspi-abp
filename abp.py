#!/usr/bin/env python3

import sys
import vlc
import time
import signal 
import RPi.GPIO as gpio 
from rotary_class import RotaryEncoder
from pbutton_class import PushButton

vlc_instance = None
vlc_player = None
vlc_media = None

playing = False
volume = 50

running = False

def init_vlc():
    global vlc_instance
    global vlc_player
    global vlc_media
    global vlc_player
    global volume
    vlc_instance = vlc.Instance("--aout=alsa")
    vlc_player = vlc_instance.media_player_new()
    vlc_media = vlc_instance.media_new("test.mp3")
    vlc_player.set_media(vlc_media)
    vlc_player.audio_set_volume(volume)

def signal_handler(signal, frame):
    global running
    running = False

def cleanup():
    gpio.cleanup()
    vlc_player.stop()

def btn1_action(pin, event):
    global playing
    global vlc_player
    
    playing = not playing

    if playing:
        vlc_player.play()
        print("playing...")
    else:
        vlc_player.stop()
        print("stopped.")

def btn2_action(pin, event):
    global vlc_player
    global volume
    
    volume = volume - 10
    if volume < 0:
        volume = 0

    vlc_player.audio_set_volume(volume)
    print("volume: " + str(volume))

def btn3_action(pin, event):
    global vlc_player
    global volume

    volume = volume + 10
    if volume > 100:
        volume = 100

    vlc_player.audio_set_volume(volume)
    print("volume: " + str(volume))

def btn4_action(pin, event):
    print("btn 4, pin " + str(pin))

def btn5_action(pin, event):
    print("btn 5, pin " + str(pin))

def rot1_action(event):
    if event == RotaryEncoder.CW:
        volume = set_volume(vlc_player.audio_get_volume() + 1)
        print("vol = " + str(volume))
    elif event == RotaryEncoder.CCW:
        volume = set_volume(vlc_player.audio_get_volume() - 1)
        print("vol = " + str(volume))
    else:
        print("rot1 x")

def rot2_action(event):
    if event == RotaryEncoder.CW:
        print("rot2 cw")
    elif event == RotaryEncoder.CCW:
        print("rot2 ccw")
    else:
        print("rot2 x")

def set_volume(volume):
    if volume > 100:
        volume = 100
    elif volume < 0:
        volume = 0
    vlc_player.audio_set_volume(volume)
    return vlc_player.audio_get_volume()

signal.signal(signal.SIGINT, signal_handler)

init_vlc()
running = True

pin_btn1 = 15
bnc_btn1 = 300

pin_btn2 = 27
bnc_btn2 = 900

pin_btn3 = 10
bnc_btn3 = 300

pin_btn4 = 5
bnc_btn4 = 300 

pin_btn5 = 21
bnc_btn5 = 300 

rot1_pin1 = 11
rot1_pin2 = 0

rot2_pin1 = 16
rot2_pin2 = 20

gpio.setmode(gpio.BCM)

#gpio.setup(pin_btn1, gpio.IN, pull_up_down = gpio.PUD_UP)
#gpio.add_event_detect(pin_btn1, gpio.FALLING, callback = button_test, bouncetime = bnc_btn1)

#gpio.setup(pin_btn2, gpio.IN, pull_up_down = gpio.PUD_UP)
#gpio.add_event_detect(pin_btn2, gpio.FALLING, callback = btn2_action, bouncetime = bnc_btn2)

#gpio.setup(pin_btn3, gpio.IN, pull_up_down = gpio.PUD_UP)
#gpio.add_event_detect(pin_btn3, gpio.FALLING, callback = btn3_action, bouncetime = bnc_btn3)

#gpio.setup(pin_btn4, gpio.IN, pull_up_down = gpio.PUD_UP)
#gpio.add_event_detect(pin_btn4, gpio.FALLING, callback = btn4_action, bouncetime = bnc_btn4)

btn1 = PushButton(gpio, pin_btn1, bnc_btn1, btn1_action)
btn2 = PushButton(gpio, pin_btn2, bnc_btn2, btn2_action)
btn3 = PushButton(gpio, pin_btn3, bnc_btn3, btn3_action)
btn4 = PushButton(gpio, pin_btn4, bnc_btn4, btn4_action)
btn5 = PushButton(gpio, pin_btn5, bnc_btn5, btn5_action)
rot1 = RotaryEncoder(gpio, rot1_pin1, rot1_pin2, rot1_action)
rot2 = RotaryEncoder(gpio, rot2_pin1, rot2_pin2, rot2_action)

while running:
    time.sleep(1)

print("bye!\n")
cleanup()
sys.exit(0)
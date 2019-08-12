# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import Connection
import time
from time import strftime


gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN, pull_up_down = gpio.PUD_DOWN)

def door_read(): 
    #date = strftime("%b %d %Y %H:%M:%S: ")
    if(gpio.input(17) == False):
     #print('{}The door is open'.format(date))
     Connection.publisher('False')
    #print('teste')
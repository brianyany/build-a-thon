#!/usr/bin/python
# post_processing.py 

# TODO: import sensor reading stuff

import RPi.GPIO as GPIO
import time
import GPIO_IR
import random

door = ['door','lock']

unlock = ['unlock','unlocked']

livingroom = ['livingroom', 'living'] 

study = ['study']

shower = ['bathroom', 'shower']

night =['night','sleep']

plant = ['plant', 'watering','water', 'plants']

cat = ['cat']

trash =['recycle','bin','trash','waste']

thanks = ['thanks','thank']

music = ['music']

def lock_door():
    global doorlock
    if(!doorlock)
        return "your door is unlocked, locking it for you.";
    else:
        return "your door is securely locked.";
    
def unlock_door():
    global doorlock
    if(doorlock)
        return "welcome home, unlocking the door for you.";
    else:
        return "your door is not locked. Wanna lock it?";

def livingroom():
    global light_livingroom
    global light_livingroom_pin
    if(light_livingroom)
        
        return "turning living room light off. Good night."
    else:
        
        return "turning living room light on. want some music?"
    
def study():
    global light_study
    global light_study_pin
    if(light_study)
        
        return "turning study light off. Good work today."
    else:
        
        return "turning study light on. want some music?"
    
def bathroom():
    global light_bathroom
    global light_bathroom_pin
    if(light_bathroom)
        
        return "turning living room light off. Good night."
    else:
        
        return "turning living room light on. want some music?"

def throw_trash():
    ran = random.randint()
    if ran%5 ==0:
        return "your door is unlocked.";
    else:
        return "your door is securely locked.";
sensors = {'humidity':(humidity, get_humidity), 'temperature':(temperature, get_temperature), 'barcode':(barcode, get_barcode), 'ir':(door, get_door)}

def check_for_keyword(words):
    words = words.split(' ')
    for k,v in sensors.items():
        for w in words:
            if w in v[0]:
                value = v[1]()
                print(value)
                return k, value

    return None, None
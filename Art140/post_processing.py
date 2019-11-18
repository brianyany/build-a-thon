#!/usr/bin/python
# post_processing.py 

# TODO: import sensor reading stuff

import RPi.GPIO as GPIO
import time
import GPIO_IR
import random
doorlock =False
door = ['door','lock']
unlock = ['unlock','unlocked']

light_livingroom =False
livingroom = ['livingroom', 'living'] 

light_study =False
study = ['study']

light_bathroom =False
shower = ['bathroom', 'shower']

night =['night','sleep', 'off']

plant = ['plant', 'watering','water', 'plants']

cat = ['cat']

trash =['recycle','bin','trash','waste']

thanks = ['thanks','thank']

speaker = False
music = ['music']

def lock_door():
    global doorlock
    if not doorlock:
        doorlock = True
        return "your door is unlocked, locking it for you."
    else:
        doorlock = False
        return "your door is securely locked."
    
def unlock_door():
    global doorlock
    if doorlock:
        doorlock = False
        return "welcome home, unlocking the door for you."
    else:
        doorlock = True
        return "your door is not locked. Wanna lock it?"

def inLivingroom():
    global light_livingroom
    global light_livingroom_pin
    if light_livingroom:
        light_livingroom = False
        return "turning living room light off. Good night."
    else:
        light_livingroom = True
        return "turning living room light on. want some music?"
    
def inStudy():
    global light_study
    global light_study_pin
    if light_study:
        light_study = False
        return "turning study light off. Good work today."
    else:
        light_study = True
        return "turning study light on. want some music?"
    
def inBathroom():
    global light_bathroom
    global light_bathroom_pin
    if light_bathroom:
        light_bathroom = False
        return "turning living room light off. Good night."
    else:
        light_bathroom = True
        return "turning living room light on. want some music?"

def goodNight():
    ran = random.randint(1,10)
    if ran%5 ==0:
        return "We are gonna be up all night."
    else:
        return "Good Night."

def waterPlants():
    ran = random.randint(1,10)
    if ran%5 ==0:
        return "Opps your plant is dead."
    else:
        return "Watering plants."

def catPlay():
    ran = random.randint(1,10)
    if ran%5 ==0:
        return "Hiss Hiss."
    else:
        return "Meow Meow."

def throwTrash():
    ran = random.randint(1,10)
    if ran%5 ==0:
        return "your door is unlocked."
    else:
        return "your door is securely locked."

def thankYou():
    ran = random.randint(1,10)
    if ran%5 ==0:
        return "your door is unlocked."
    else:
        return "your door is securely locked."

def playMusic():
    global speaker
    if speaker:
        speaker =False
        return "Music Off."
    else:
        speaker = True
        return "Music On."

sensors = {'lock':(door, lock_door), 'unlock':(unlock, unlock_door), 'livingroom':(livingroom, inLivingroom), 'study':(study, inStudy), 'bathroom':(bathroom,inBathroom),
'night':(night,goodNight),'plants':(plant,waterPlants),'cat':(cat,catPlay),'trash':(trash,throwTrash),'thanks':(thanks,thankYou),'music':(music,playMusic)}

def check_for_keyword(words):
    words = words.split(' ')
    for k,v in sensors.items():
        for w in words:
            if w in v[0]:
                value = v[1]()
                print(value)
                return k, value

    return None, None
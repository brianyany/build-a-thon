#!/usr/bin/python
# post_processing.py 

# TODO: import sensor reading stuff
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import GPIO_IR

humidity = ['humidity', 'humid']

temperature = ['temperature', 'hot', 'cold', 'weather']

barcode = ['scan']

ir = ['door']

def barcode_reader():
    global scan, scanned
    inp = input('')
    if inp == "028400090896":
        scan = 'Doritos Nacho Cheese snack size'
    if inp == "844660026617":
        scan = 'Monoprice VGA to HDMI'
    if inp == "845156001118":
        scan = 'Sparkfun electronics resistor kit 500'
    if inp == "640522710850":
        scan = 'Raspberry pi 3 model 3 motherboard'
    if inp == "025000058806":
        scan = 'Minute Maid Pink Lemonade 12 ounce'
    if inp == "028400040112":
        scan = 'Cheetos crunchy snack size original'
    if inp == "X001CYIACJ":
        scan = 'Wifi Nano 11 AC adapter usb'
    if inp == "028400090858":
        scan = 'Lays Classic potato chips snack size'
    
    scanned=True
    return scan

def get_humidity():
	sensor = Adafruit_DHT.DHT22
	pin = 2
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return humidity

def get_temperature():
	sensor = Adafruit_DHT.DHT22
	pin = 2
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	return temperature

def get_barcode():
	print('read barcode')
	code = barcode_reader()
	print(code)
	return code

def get_ir():
	GPIO_IR.setup()
	return GPIO_IR.objectDetected();

sensors = {'humidity':(humidity, get_humidity), 'temperature':(temperature, get_temperature), 'barcode':(barcode, get_barcode), 'ir':(ir, get_ir)}

def check_for_keyword(words):
    words = words.split(' ')
    for k,v in sensors.items():
        for w in words:
            if w in v[0]:
            	value = v[1]()
            	print(value)
            	return k, value

    return None, None
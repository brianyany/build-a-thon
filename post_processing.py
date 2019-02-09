#!/usr/bin/python
# post_processing.py 

# TODO: import sensor reading stuff
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import GPIO_IR
import GPIO_Barcode

humidity = ['humidity', 'humid']

temperature = ['temperature', 'hot', 'cold', 'weather']

barcode = ['scan']

ir = ['door']


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
    code = GPIO_Barcode.barcode_reader()
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
# post_processing.py 

# TODO: import sensor reading stuff
import Adafruit_DHT

humidity = ['humidity']

temperature = ['temperature']

barcode = ['price']

ir = ['object']

sensors = {'humidity':(humidity, get_humidity), 'temperature':(temperature, get_temperature), 'barcode':(barcode, get_barcode), 'ir':(ir, get_ir)}

def check_for_keyword(words):
    words = words.split(' ')
    for k,v in sensors.items():
        for w in words:
            if w in v[0]:
                return k, v[1]()

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
    return

def get_ir():
    return
    
# post_processing.py 

# TODO: import sensor reading stuff

humidity = ['humidity']

temperature = ['temperature']

barcode = ['price']

ir = ['object']

sensors = {'humidity':(humidity, get_humidity), 'temperature':(temperature, get_temperature), 'barcode'=(barcode, get_barcode), 'ir'=(ir, get_ir)}

def check_for_keyword(words):
    words = words.split(' ')
    for k,v in sensors.items():
        for w in words:
            if w in v[0]:
                return k, v[1]()

def get_humidity():
    return 

def get_temperature():
    return 

def get_barcode():
    return

def get_ir():
    return
    
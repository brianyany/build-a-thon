#!/usr/bin/python
#server.py on pi

import socket               # Import socket module
import json
from post_processing import *
import threading
from cap_touch import *


s = socket.socket()         # Create a socket object
host = "10.195.92.22" # Get local machine name
port = 12000                  # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

# def my_callback(self):
#    print("ir!!!")
#    c.send(json.dumps('irdetected').encode('utf-8'))

# def ir_monitor():
#    s = socket.socket()         # Create a socket object
#    host = "172.16.117.108" # Get local machine name
#    port = 13999                  # Reserve a port for your service.
#    s.bind((host, port))        # Bind to the port

#    print ('IR Monitor connection waiting')

#    s.listen(5)
#                     # Now wait for client connection.
#    c, addr = s.accept()     # Establish connection with client.
#    print ('IR Monitor got connection from', addr)

#    GPIO.setwarnings(False)
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
#    GPIO.setup(4 ,GPIO.IN, pull_up_down =GPIO.PUD_DOWN)
#    GPIO.add_event_detect(4, GPIO.BOTH)
#    GPIO.add_event_callback(4, my_callback)

#    while True:
#       pass

# t_monitor = threading.Thread(target=ir_monitor)
# t_monitor.start()

s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)
TOU_THRESH = 50
REL_THRESH = 70
setup(0x5a)

while True:
   # data, server = s.recvfrom(4096)
   currentTap = readData(0x5a)
    for i in range(12):
        pin_bit = 1 << i
        #print ("message is: "+ str(currentTap1)+str(currentTap0) ) 
        if currentTap & pin_bit and not lastTap & pin_bit:
          print ("Touched: " + str(i)) 
        if not currentTap & pin_bit and lastTap & pin_bit:
          print ("Released: " + str(i))
        lastTap = currentTap
        time.sleep(0.1)
    if msg:
      c.send(json.dumps(msg).encode('utf-8'))

   data = c.recv(1024)
   if not data:
      continue
   print ("recvied message")
   text = json.loads(data.decode('utf-8'))
   if text == "This connection is going to the morgue.":
      c.close()

      c, addr = s.accept()     # Establish connection with client.
      print ('Got connection from', addr)


      continue

   print ("I think you said: " + text)

   msg = 'ack'
   c.send(json.dumps(msg).encode('utf-8'))
   print('message send')

   if text:
      keyword, sensor_value = check_for_keyword(text)
      if keyword is None:
         c.send(json.dumps('I\'m not sure.').encode('utf-8'))
      else:
         msg = (keyword, sensor_value)
         c.send(json.dumps(msg).encode('utf-8'))
         print ("response given")
   else:
      c.send(json.dumps('Sorry I didn\'t get that').encode('utf-8'))
               # Close the connection


#!/usr/bin/python
#server.py on pi

import socket               # Import socket module
import json
from post_processing import *



s = socket.socket()         # Create a socket object
host = "172.16.117.108" # Get local machine name
port = 31337                  # Reserve a port for your service.
s.bind((host, port))        # Bind to the port


s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print ('Got connection from', addr)

while True:
   # data, server = s.recvfrom(4096)
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

   print (text)

   msg = 'ack'
   c.send(json.dumps(msg).encode('utf-8'))
   print('message send')

   if text:
      keyword, sensor_value = check_for_keyword(text)
      if keyword is None:
         c.send(json.dumps('invalid').encode('utf-8'))
      else:
         print(sensor_value)
         msg = (keyword, sensor_value)
         c.send(json.dumps(msg).encode('utf-8'))
         print ("response given")
   else:
      c.send(json.dumps('invalid').encode('utf-8'))

   c.close()                # Close the connection

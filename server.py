#server.py on pi

import socket               # Import socket module
import json
from post_processing import *



s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 31337                  # Reserve a port for your service.
s.bind((host, port))        # Bind to the port


s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   # data, server = s.recvfrom(4096)
   data = c.recv(1024)
   print ("recvied message")
   text = json.loads(data.decode('utf-8'))
   print (text)

   msg = 'ack'
   c.send(json.dumps(msg).encode('utf-8'))
   print('message send')

   keyword, sensor_value = check_for_keyword(text)

   msg = (keyword, sensor_value)
   c.send(json.dumps(msg).encode('utf-8'))
   print ("response given")

   c.close()                # Close the connection
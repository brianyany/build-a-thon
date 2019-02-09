#server.py on pi

import socket               # Import socket module
import json
import pyttsx3



s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 31341                  # Reserve a port for your service.
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

   # TODO: post processing

   # TODO: fetch sensor data

   msg = 'The temperature is 17 degrees'     # TODO: compose sentence as response 
   c.send(json.dumps(msg).encode('utf-8'))
   print ("response given")

   # TODO:read the response
   engine = pyttsx3.init(driverName='nsss')
   engine.say(msg)
   engine.runAndWait()

   c.close()                # Close the connection
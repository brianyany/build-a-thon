#client.py on pc

import socket               # Import socket module
import json

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 31341                # Reserve a port for your service.

s.connect((host, port))
msg = 'what is the temperature'         #TODO: retrive sentence from speech to text 
s.send(json.dumps(msg).encode('utf-8'))     # sentece the request

data = s.recv(1024)             # wait for ack
text = json.loads(data.decode('utf-8'))
print (text)

data = s.recv(1024)             # wait for response, might not be necessary 
text = json.loads(data.decode('utf-8'))
print (text)

# TODO: text to speech??

s.close()                     # Close the socket when done
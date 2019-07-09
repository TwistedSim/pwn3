

import socket
import base64
from itertools import permutations
from string import printable

HOST = 'challenge01.root-me.org'
PORT = 51035

# [id=546815648;na                 me=AAAAAAAAAAAAA                 AAAAAAAAAAAAAAAA                 AAAAAAAAAAAAAAAA                 ;is_member=false                 ;mail=;pad=0000]
# 211663061e86c6379823b619bf1c1f04 15642060f918ec21554ffae531f9ce61 cadf60b14dbcbcaab7ea39031c939799 81a364892d76b922215b0525d82f41c7 a8aed8fc4669ce5fb5b2d71fe165f2d5 f0c60b3880ad4c3a105233d3c4c1d14e


payload  = bytes.fromhex('211663061e86c6379823b619bf1c1f04')  
payload += bytes.fromhex('15642060f918ec21554ffae531f9ce62') # change the 1 -> 2 to scramble this part and detokenize it

# We need to execute this attack in two part. We need to know how the server will decode our token in this block to be able to write on top with XOR
if True:
	# Second part after we found out the `current` block
	current  = b'\x133\xa4\x97\n\xde}\x18xmy\x12\x1e\xc8n\xdf'  # This is the part in the token if we only send the token with the next payload
	wanted   = ';name=TwistedSim'.encode()
	encoded  = bytes.fromhex('cadf60b14dbcbcaab7ea39031c939799')
	payload += bytes(c^w^e for c,w,e in zip(current, wanted, encoded))
else:
	# First part
	payload += bytes.fromhex('cadf60b14dbcbcaab7ea39031c939799')

current  = ';is_member=false'.encode()
wanted   = ';is_member=true;'.encode()
encoded  = bytes.fromhex('81a364892d76b922215b0525d82f41c7')
payload += bytes(c^w^e for c,w,e in zip(current, wanted, encoded))

payload += bytes.fromhex('a8aed8fc4669ce5fb5b2d71fe165f2d5')
payload += bytes.fromhex('f0c60b3880ad4c3a105233d3c4c1d14e')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    data = s.recv(1024)    
    data = s.recv(1024)       

    s.send(b'2\n') # ask for auth token
    s.recv(1024)	  
        
    s.send(base64.b64encode(payload)+b'\n')    
    s.recv(1024)
    answer = s.recv(1024).decode()
    
    if 'Hack' not in answer:
	    s.send(b'2\n')
	    s.recv(1024)
	    print(s.recv(1024).decode().split('\n')[5])
    else:
        print('Decrypt token by the server:', answer.split('\n')[0].split('Token')[1][5:-1])  # Take the part after the AAAAAA for the first "current" payload
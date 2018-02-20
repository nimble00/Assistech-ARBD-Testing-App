import socket
s=socket.socket()
print "socket created"
host='10.184.41.164'
port = 2300
s.connect((host,port))
print "connected to port"

msg=raw_input("Enter a command to be executed:")
# msg is a string of the form : msg="['K1','K2',..]"
while msg!="stop":
	s.send(msg)
	data=s.recv(1024)
	print "Recieved outptu from server:"+str(data)
	msg=raw_input("Enter the next command")
if msg=="stop":
	s.send(msg)
	data=s.recv(1024)
	print str(data)
	
s.close()
print "the client socket is also closed"

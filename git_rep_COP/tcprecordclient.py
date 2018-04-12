import socket
import time
import subprocess
import paramiko
from subprocess import call,Popen,PIPE
s=socket.socket()
print "socket created"
host='192.168.7.2'
port = 1360
s.connect((host,port))
print "connected to port"
import time
filename=raw_input("Enter the name of the text file where recording has to be done(in the form 'abc.txt'):")
s.send("filename"+filename)

msg=raw_input("To start recording enter 'r':")


ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.7.2',username='ubuntu',password='temppwd')

while msg!="stop":
	s.send(msg)
	data=s.recv(1024)
	
	print str(data)
	print "Start giving keystrokes"
	#for i in range(30):
	#	time.sleep(1)
	#	print "stop executing in "+str(30-i)+"seconds"
	msg=raw_input("Started recording. To continue enter 'c', else enter 'stop':")
if msg=="stop":
	ftp_client=ssh_client.open_sftp()
	ftp_client.get('/home/ubuntu/' + filename ,'/home/sudhi/COP/working_temporary/' + filename)
	ftp_client.close()

	
	s.send(msg)
	data=s.recv(1024)
	print str(data)
	
s.close()
print "the client socket is also closed"



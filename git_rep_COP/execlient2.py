
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#runs 10 lines in linker, asks to continue or not
#make sure executer5 is in the sam file as this client
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
from subprocess import Popen,PIPE,call
from executer5 import linker
import socket
s=socket.socket()
print "socket created"
host='192.168.7.2'
port = 1302
s.connect((host,port))
print "connected to port"

import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.7.2',username='ubuntu',password='temppwd')

flee=raw_input("Enter the log file name or enter 'stop' to stop:")

#arbdlogfiles/1/arbd.log_2017-12-12_09-28
global ki,l,k,flo
flo=flee
ki=0
l=0
if flee!='stop':
	k=linker(flee)
else:
	k=[]


	
for i in range(len(k)):
	
	if flo!="stop":
	        if i == len(k)-1:
	  		flo=="stop"
			
		j=k[i] 
		         		
		lst=j[-2]
		delta=j[-1]
		msg=str(lst)+'::'+str(delta)
		msg=str(msg) #msg is a str  of the from '['k=uinput.KEY_K1','k=uinput.KEY_K2',...],timedifference'

		s.send(msg)
		data=s.recv(1024)
		l+=1
		print l, ki
		print "Recieved output from server:"+str(data)
		
		if l-ki==10:
			flo = raw_input("To continue execution enter 'c',else enter 'stop' to stop:")
			ki = ki + 10
	elif flo=='stop':
		msg="stop"

		ftp_client=ssh_client.open_sftp()
		ftp_client.get('/home/ubuntu/reco.txt','/home/sudhi/COP/working_temporary/reco.txt')
		ftp_client.close()		

		s.send(msg)
		data=s.recv(1024)
		ki='qwer'
		print "stopped executing"
		print str(data)


msg="stop"			
if flo=="stop" and ki!='qwer':
	s.send(msg)
	data=s.recv(1024)
	print str(data)
	
s.close()
print "the client socket is also closed"

import os

import sys
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE

def server(host,port):
	s=socket.socket()
	ip=''
	s.bind((ip,port))
	print 'waiting....'
	s.listen(1)
	c,addr=s.accept()
	print 'connected...'

	wut=c.recv(1024)
	c.send('recieved wut')
	if str(wut)=='r':
		recordserver(s,c)
	s.close()	#close the socket, keep this at the last, or at the end of the loop
def follow(thefile):
	#keeps producing an infinitely long generator wrt time
    thefile.seek(0,2)
    while True:
	
        line = thefile.readline()
	 
        if not line:
            
	    time.sleep(0.1)
            continue
	    		
        yield line

def recordserver(s,c):

		#grep might interfer with stout.read so don't use grep		

		#>>!!cmd1='ls -t /opt/arbd/logs/ | head -1 '
		cmd1='ls -t /home/sudhi/COP/piping| head -1 '
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
				
		chi=p1.communicate() 
		
		llf=str(chi[0][:-1]) #llf=latest log file
		print chi[0][:-1]
		
		#>>!!cmd2='tail -0f /opt/arbd/logs/' + llf  #'| grep  -E Keyboard.*event\|Current.*window\|BRF.*data ' 
		 
		cmd2='tail -0f /home/sudhi/COP/piping/' + llf 
		#cmd2='sudo sh -c "tail -0f /home/sudhi/COP/arbd.log_2018-03-12_12-33 | grep  -E Keyboard.*event\|Current.*window\|BRF.*data > /home/sudhi/COP/working_temporary/temp_log.txt" ' 	#make sure there is no space bw ' and sudo	
		p2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		#p2.stdin.write("temppwd\n")
		#p2.stdin.flush()
		#p2.stdin.write("@3wRETyyUI\n") #can't use communicate here because communicate will wait for process to terminate
		
		
		l=[]
		lenl=0
		
    		for line in iter(lambda: p2.stdout.readline(),''):
			if ('Keyboard event' in line) or ('Current window' in line) or ("BRF data" in line):			
				msg=c.recv(1024)
				
				if msg=='continue':
					print line
					l.append(line)
					c.send(line)
			
				if msg=='stop':
					c.send('recording stopped')	
					break
		
								
		
		

host= "127.0.0.1"
port=5678
server(host,port)
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
		cmd1='ls -t /opt/arbd/logs/ | head -1 '
		#cmd1='sudo sh -c "ls -t  /home/sudhi/COP/ | head -1" '
		#cmd1="ls -t  /home/sudhi/COP/ | head -1" 
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		#p2.stdin.write("temppwd")		
		chi=p1.communicate() # don't write \n
		#input="@3wRETyyUI"
		llf=str(chi[0][:-1]) #llf=latest log file
		print chi[0][:-1]
		f=open("temp_log.txt","w+")
		f.close()
		cmd2='tail -0f /opt/arbd/logs/' + llf + '| grep  -E Keyboard.*event\|Current.*window\|BRF.*data > /home/ubuntu/temp_log.txt'  #temp_log.txt is the temporary log file 
		print cmd2
		#cmd2='sudo sh -c "tail -0f /home/sudhi/COP/arbd.log_2018-03-12_12-33 | grep  -E Keyboard.*event\|Current.*window\|BRF.*data > /home/sudhi/COP/working_temporary/temp_log.txt" ' 	#make sure there is no space bw ' and sudo	
		p2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		#p2.stdin.write("temppwd\n")
		#p2.stdin.flush()
		#p2.stdin.write("@3wRETyyUI\n") #can't use communicate here because communicate will wait for process to terminate
		
		print 'temp_log created'
		l=[]
		lenl=0
		logfile = open("temp_log.txt","r") #latest log file name
    		loglines = follow(logfile)
    		for line in loglines:
			msg=c.recv(1024)
        		
			if msg=='continue':
				l.append(line)
				c.send(line)
			
			if msg=='stop':
				c.send('recording stopped')
				logfile.close()			
				break
		
								
		
		

host= "192.168.7.2"
port=3120
server(host,port)
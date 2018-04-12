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
	#print 'waiting....'
	s.listen(1)
	c,addr=s.accept()
	#print 'connected...'

	wut=c.recv(1024)
	c.send('recieved wut')
	if str(wut)=='r':
		recordserver(s,c)
	elif str(wut)=='e':
		exeserver(s,c)
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

		cmd1='ls -t /opt/arbd/logs/ | head -1 '
		#>>!!cmd1='ls -t /home/sudhi/COP/piping| head -1 '
		p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
				
		chi=p1.communicate() 
		
		llf=str(chi[0][:-1]) #llf=latest log file
		#print chi[0][:-1]
		
		cmd2='tail -0f /opt/arbd/logs/' + llf   
		 
		#>>!!cmd2='tail -0f /home/sudhi/COP/piping/' + llf 
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
					#print line
					l.append(line)
					c.send(line)
			
				if msg=='stop':
					c.send('recording stopped')	
					break
		
								
def exeserver(s,c):
	l = 0
	cmd1='ls -t /opt/arbd/logs/ | head -1 '
	#cmd1='sudo sh -c "ls -t  /home/sudhi/COP/ | head -1" '
	#cmd1="ls -t  /home/sudhi/COP/ | head -1"
	p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
	#p2.stdin.write("temppwd")		
	chi=p1.communicate() # don't write \n
	#input="@3wRETyyUI"
	llf=str(chi[0][:-1]) #llf=latest log file
	print chi[0][:-1]
	while l==0:
	    temps = ""
	    cwobrf = []
	    pp2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True, preexec_fn=os.setsid)
	    keps = c.recv(1024)
		# command will be of the form "['K1','K2',..]"   , command is a string
 	    if not keps:
		break
	    elif keps == "EOF":
		break
	    else:
			print "Message received:" + str(keps)
			comlist=list(keps)
			try :
				#comlist is a list of the form ['k=uinput.KEY_K1','k=uinput.KEY_K2',...]
				combo=[]
				for i in comlist:
					if i!='no_key':
					        exec(i)
						combo.append(k)
				if len(combo)==0:
					
					output="No keyboard event to execute in this line"
					time.sleep(delta)
				else:			
							
					Keyboard.emit_combo(combo)
					output="Keyboard event executed"
					time.sleep(delta)
				for line in iter(lambda: pp2.stdout.readline(),''):
					if "Current window" in line or "BRF data" in line:
						cwobrf.append(line)
				c.send(str(cwobrf))
				os.killpg(os.getpgid(pp2.pid), signal.SIGTERM)  # Send the signal to all the process groups
			except Exception as e:
				print "An error occured in execution."
				output="An error occured in execution; Error"+ e.__doc__ +", "+"Error message:"+ e.message
			print output		
		

host= "192.168.7.2"
port=2333
server(host,port)

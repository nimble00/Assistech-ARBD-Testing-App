import socket
import subprocess
from subprocess import Popen,PIPE,call
import time

#these two are not used anywhere as of now:
import sys
import os



def Main():
	print "server file runninng"
	s=socket.socket()
	host=''
	port=1301
	s.bind((host,port))
	s.listen(10)
	c,addr=s.accept()
	print "Connection from:" + str(addr)
	#commands is the list of list, containing all commands executed	
	commands=[]
	global l
	l=0
	while l==0:
	    command=c.recv(1024)
	    if not command:
	   		break
	    elif "filename" in str(command):
			s=str(command)			
			filename=s[8:]
	    elif str(command)=='r':
			cmd='sudo sh -c "tail -0f /opt/arbd/logs/arbd.log_2018-02-21_17-46 > /home/ubuntu/'+filename+'"'
			# sh -c and ".." makes sure permission is for both the code before and after >
			p = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True) # select popen, or call or run such that it doesn't block the current terminal
			p.stdin.write("temppwd\n")
			p.stdin.flush()
			c.send("Recording started...")
	    elif str(command)=='c':
			c.send("Recording continuing...")	
	    elif str(command)=="stop":
			#os.system(send file to client)
			#stdout,stderr = p.communicate()
			#print stdout,stderr
			c.send("The server socket is closed.")
			c.close()
			l+=1
			print "The client disconnected."
#-------------------------------------------------------------------------------------------------------------------	   
	    
	    elif str(command)[0]=='u':
			print "Command passed:" + str(command)
			command=command[2:]

			try:			
				#this is the output execution and output recording part
				#popen creates a new process, subprocess.check_output doesn't 
				command_list=command.split(" ")
				commands.append(command_list)
				output=subprocess.check_output(command_list)
				if len(output)==0:
					output="No output printed in cmd"
					
			except Exception as e:
				print "An error occured execution."
				output="A error occured in output recording/execution ;Error in recording :"+ e.__doc__ +", "+"Error message:"+ e.message

			else:
				print "Output recorded"
			
			c.send(output)
			print "output sent,Waiting for next command"
#-------------------------------------------------------------------------------------------------------------------	

if __name__ == '__main__':
	Main()

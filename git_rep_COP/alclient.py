'''NOTE:
1.alserver and alclient ,stop_button.txt,stop_button.py,executer5 should be in the same directory in PC
2.There must be something written in the last three lines after server fxn defn in alserver
3.Stop_button.py waits for 3 seconds after recieving the stop command to actually send stop to alclient.py
4.IMP:The stop_button.py has to be run every time along with alclient.py or else it won't work prorply
'''
import os
import paramiko, getpass, re, time
import sys
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE
from executer6 import ex,ex2,di


def recordclient(s):
	testcase_name=raw_input("Enter the name in which the test case has to be saved:")
	print "Recording started,you can start giving keystrokes..."
	s.send('continue')
	qwer=0
	testcase=[]
	l=0
	while qwer==0:
		
		
		stop_button=open("stop_button.txt","r")
		stop_button.seek(0,0)
		u_input=stop_button.readline()                            
		stop_button.close()
		
		#stop_button.py waits for 3 seconds after recieving the stop command to actually send stop to alclient.py

		line=s.recv(1024)
		if 'Keyboard event received' in line:
			print_ln=str(ex(str(line))) + ' : ' + str(ex2(str(line)))
			print print_ln		
		testcase.append(str(line))
		
		if u_input=='stop':
			s.send('stop')			
			qwer+=1
			
		else:
			
			s.send('continue')
	
	print s.recv(1024)
	print 'The test case recorded is:'
	for i in testcase:
		print i
	test_file=open(testcase_name,'w')
	test_file.write(str(testcase))
	

def execute(s):
	s.send('blah blah') #first send	

#----------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------
#host=raw_input('Enter the arbd(server) ip address:')
port=int(raw_input('Enter the port number to which you have to connect:'))
host='192.168.7.2'
#----------------------------------------------------------------------------------------
f=open('alserver.py','r')
lines = f.readlines()
f.close()

f=open('alserver.py','w')
for i in lines[:-3]:
	f.write(i)
	
f.write('host= "'+host+'"')
f.write('\nport='+str(port))
f.write('\nserver(host,port)')
f.close()
#----------------------------------------------------------------------------------------
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname=host,username='sudhi',password='@3wRETyyUI')
ssh_client.connect(hostname=host,username='ubuntu',password='temppwd')
dir_path = os.path.dirname(os.path.realpath(__file__))
ftp_client=ssh_client.open_sftp()
ftp_client.put(dir_path+'/alserver.py','/home/ubuntu/alserver.py')
ftp_client.put(dir_path+'/ser.sh','/home/ubuntu/ser.sh')
stdin,stdout,stderr=ssh_client.exec_command("chmod +x ser.sh")
ftp_client.put(dir_path+'/tempo.py','/home/ubuntu/tempo.py')
#ftp_client.put(dir_path+'/alserver.py',dir_path+'/alserversshed.py')
time.sleep(1)
#ftp_client.put(dir_path+ '/ser.sh','/home/ubuntu/ser.sh')
#ftp_client.put(dir_path+'/ser.sh',dir_path+'/ser.sh')
ftp_client.close()
'''
ssh =paramiko.SSHClient()
session = ssh.get_transport().open_session()
session.set_combine_stderr(True)
session.get_pty()
command = 'sudo ./ser.sh'
session.exec_command("sudo bash -c \"" + command + "\"")
stdin = session.makefile('wb', -1)
#stdout = session.makefile('rb', -1)
stdin.write(temppwd + '\n')
stdin.flush()
#print(stdout.read().decode("utf-8"))


ssh = paramiko.SSHClient()


stdin,stdout,stderr=ssh.exec_command('sudo python alserver.py',timeout=15,get_pty=True)
stdin.write('temppwd\n')
stdin.flush()


stdin,stdout,stderr=ssh_client.exec_command("chmod +x ser.sh")
commands = ['sudo -S ./ser.sh true']
channel = ssh_client.invoke_shell()
# clear welcome message and send newline
time.sleep(1)
channel.recv(9999)
channel.send("\n")
for command in commands:
	    channel.send(command + "\n")
	    channel.send("temppwd\n")
	    print "chala"
	    while not channel.recv_ready(): #Wait for the server to read and respond
	        time.sleep(0.1)
	    time.sleep(0.1) #wait enough for writing to (hopefully) be finished
	    output = channel.recv(9999) #read in
print(output.decode('utf-8'))
time.sleep(0.1)
channel.close()
time.sleep(1)

'''

s=socket.socket()
s.connect((host,port))
print 'Connection established,sockets created and connected.'

wut=raw_input("Enter 'r' to record or 'e' to execute a recorded test case:")

while (wut !='r' and wut !='e'):
	wut=raw_input("You gave a wrong input, please enter 'r' to record or 'e' to execute a recorded test case:")
s.send(wut)
recv_msg=s.recv(1024)
if wut == 'r':
	recordclient(s)



#----------------------------------------------------------------------------------------



		
	

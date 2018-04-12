'''NOTE:
1.alserver and alclient ,stop_button.txt,stop_button.py,executer6,indnt_exeserver.py should be in the same directory in PC
2.There must be something written in the last three lines after server fxn defn in alserver
3.
4.If even after calling stop, functioning has not stopped then give a few more keystrokes.This might not be rquired in ARBD as log file still gets updated even afer last keyboard event line.
5.IMP:The stop_button.py has to be run every time along with alclient.py or else it won't work prorperly as stop.txt in default condition has 'stop'.
6.Every testcase is saved of the form testcase_name.py, which has the code from indnt_exeserver.py, the lists link and testcase, and also the line sassy(link) (check the format of testcase at ln114)
7.compare fxn won't function properly if any user types "[display-svc] [debug] BRF data :".
8.If execution of whole file is completed, done.txt will have one line called 'done'.
9.done.txt and testcase.py files are buffer in arbd
10. make sure uinstall is installed in the ARBD
11.assuming wut won't get any value other than r ,e or x; make sure of this in GUI linking
'''
import os
import paramiko, getpass, re, time
import sys
import time
import subprocess
import socket
from subprocess import Popen,call,PIPE
from executer6 import ex,ex2,di,timeparse,linker,timedifference
def compare(resulted_link_l,ideal_link_l):
	#resulted_link_l = resulted_link[l][-1],ideal_link_l = ideal_link[l][q]
	#compares last appended BRF data in resulted_link[l],ideal_link[l] 
	
	
	brf1=resulted_link_l.split("[display-svc] [debug] BRF data :")[-1]
	brf2=ideal_link_l.split("[display-svc] [debug] BRF data :")[-1]
	if brf1==brf2:
		return True
	else:
		return False
def recordclient0(s):
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
		
		#stop_button.py waits for 2 seconds after recieving the stop command to actually send stop to alclient.py

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
	
def recordclient(s):
	#gives a file of the name testcase_name which has two lists.The first list is parsed one and the second list is unparsed.
	testcase_name=raw_input("Enter the name in which the test case has to be saved:")
	print "Recording started,you can start giving keystrokes..."
	s.send('continue')
	qwer=0
	testcase=[]	#testcase contains the unparsed lines as srecieved	
	blink=[]		#blink contains parsed lines of the logfile. blink=BRF_BASED_link
	'''blink= [ 'o',b0,[l01],[l02],...,b1,[l11],[l12],...,b2,....,bn,[ln1],[ln2],...,bn_1,........bfinal/[lfinal] ]
	
		where bn = string containg nth BRF data line,bn_1 = string containg (n+1)th BRF data line
		and [lnm] = list of the form : [lnm]=[line,time,['k=uinput.KEY_K1','k=uinput.KEY_K2',...],timediff] .
		line is a string containing Keyboard Event, time is a string, third element is a list of the given format,
		timediff is an int and is the time difference (lnm_1 - lnm)
		b0 might come or might not come based on whether during recording first line from logfile is brfdata or keyboard event	

	'''
	blink.append('o')
	
	while qwer==0:
		
		
		stop_button=open("stop_button.txt","r")
		stop_button.seek(0,0)
		u_input=stop_button.readline()                            
		stop_button.close()
		
		#stop_button.py waits for 2 seconds after recieving the stop command to actually send stop to alclient.py
		#this is necessary as the last few BRF data lines in the log_file after the last keyboard event line is also required.
		line=s.recv(1024)
		testcase.append(str(line))
		
		if ('BRF data' in line):
			blink.append(line)	
                        
			
		elif ('Keyboard event received' in line):
			ji=ex(line)
			blink.append([line,timeparse(line),ji])
			print_ln=str(ji) + ' : ' + str(ex2(line))
			print print_ln
		if u_input=='stop':
			s.send('stop')	
			f=s.recv(1024)	
			print f	
			qwer+=1
		
		else:
			
			s.send('continue')

	for i in range(len(blink)-1): #adding timedifference
		if str(type(blink[i]))=="<type 'list'>":
			
			k=i+1
                        
			while k<len(blink)-1:
				if str(type(blink[k]))=="<type 'list'>":
					break
				else:
					k+=1
			print blink[i][1],blink[k][1],blink[k]
			if str(type(blink[k]))=="<type 'list'>":	#to make sure that last line is a keyboard event list
				blink[i].append(timedifference(blink[i][1],blink[k][1]))
	ik=len(blink)-1	
	while ik >0:
		if str(type(blink[ik]))=="<type 'list'>": #adding timediff to last element
			blink[ik].append(0)
			ik-=1
	
	
	print 'The test case recorded is:'
	for i in range(len(testcase)-1):
				
			print testcase[i]
			
			print blink[i+1]
			print ' '
	  		
    	with open(testcase_name+'.txt', "w") as f1:
        		
			f1.write(str(blink)+'\n')
			f1.write(str(testcase)+'\n')
			   #to call the function sassy
	
	#no need to close files, with automatically closes
	
	#link is the arsed one and testcase is the unparsed.
	


def execute(s, tc,ssh_c):
	testcase_name=tc+'.txt'
	with open(testcase_name,'r') as f:
		ideal_link=f.readlines()[0]
		#print ideal_link
		ilink=eval(ideal_link)
		sendlist=[]
		executed=[]
		for line in ilink:
			if "BRF data" in line:
				
				if len(sendlist)==0:
					continue
				s.send(str(sendlist))
				print 'sendlist:'+str(sendlist)
				sendlist=[]
				outbrf=s.recv(1024)
				if not outbrf:
					break
				ibrf = str(line).split(" [display-svc] [debug] BRF data :")[-1]
				
				obrf = eval(outbrf)
				tick = False
				uip ='c'
				print "IDEAL:" + ibrf
				print "RECEIVED:" + str(obrf)
				print ' '
				for string in obrf:
					if not "BRF data" in string:
						continue
					sbrf = str(string).split(" [display-svc] [debug] BRF data :")[-1]
					executed.append(string)
					if sbrf == str(ibrf):
						tick = True
						break
				if tick is True:
					print "BRF data: " + str(ibrf[-1]) + " matched!"
				else:
					uip = raw_input("Test case '" + tc + "' failed: Enter 'c' to continue or 's' to stop:")
				if uip == "s":
					s.send("tervar=1")
					break
			elif not('o' in line):
				sendlist.append(line)
				executed.append(line)
		print "Test case '" + tc + "' passed!"
	
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
#host=raw_input('Enter the arbd(server) ip address:')
port=int(raw_input('Enter the port number to which you have to connect:'))
#>>!!host='192.168.7.2'
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
#!!>>
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh_client.connect(hostname=host,username='sudhi',password='@3wRETyyUI')
ssh_client.connect(hostname=host,username='ubuntu',password='.Book40')
dir_path = os.path.dirname(os.path.realpath(__file__))
ftp_client=ssh_client.open_sftp()
ftp_client.put(dir_path+'/alserver.py','/home/ubuntu/alserver.py')
time.sleep(1)
'''
#__________________________________________________________________________
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host,username='ubuntu',password='.Book40')



stdin,stdout,stderr=ssh.exec_command('echo ".Book40" | sudo -S ls')	
lo=stdout.readlines()
print lo

stdin,stdout,stderr=ssh.exec_command('sudo python /home/ubuntu/alserver.py', get_pty = True)
time.sleep(5)
#print stderr.readlines()
#print stdout.readlines()
stdin,stdout,stderr=ssh.exec_command('pgrep -af python')
print stdout.readlines()
print stderr.readlines()
'''
#____________________________________________________________________________
'''
ftp_client.put(dir_path+'/ser.sh','/home/ubuntu/ser.sh')
stdin,stdout,stderr=ssh_client.exec_command("chmod +x ser.sh")
ftp_client.put(dir_path+'/tempo.py','/home/ubuntu/tempo.py')
#ftp_client.put(dir_path+'/alserver.py',dir_path+'/alserversshed.py')
time.sleep(1)
#ftp_client.put(dir_path+ '/ser.sh','/home/ubuntu/ser.sh')
#ftp_client.put(dir_path+'/ser.sh',dir_path+'/ser.sh')
ftp_client.close()

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

wut=raw_input("Enter 'r' to record or 'e' to execute a recorded test case or 'x' to exit connection:")
#assuming wut won't get any value other than r ,e or x; make sure of this in GUI linking
while wut !='x':
	s.send(wut)
	recv_msg=s.recv(1024)
	if wut == 'r':
		print 'make sure stop_button.py is STARTED ON ' 
		recordclient(s)
	elif wut == "e":
		tc=raw_input("Please enter the name of test case to be executed(without '.py' or '.txt') :")
		#write code to make sure testcase exists
		execute(s,tc,ssh_client)
	wut=raw_input("Please enter 'r' to record or 'e' to execute a recorded test case or 'x' to exit connection:")


s.send(wut)
s.close()	#closes the socket, keep this at the last, or at the end of the loop



#----------------------------------------------------------------------------------------



		
	

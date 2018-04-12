'''NOTE:
1.alserver and alclient ,stop_button.txt,stop_button.py,executer6,indnt_exeserver.py should be in the same directory in PC
2.There must be something written in the last three lines after server fxn defn in alserver
3.Stop_button.py waits for 2 seconds after recieving the stop command to actually send stop to alclient.py;this is necessary as the last few BRF Data lines in the log_file after the last keyboard event line is also required.
4.If even after calling stop, functioning has not stopped then give a few more keystrokes.This might not be rquired in ARBD as log file still gets updated even afer last keyboard event line.
5.IMP:The stop_button.py has to be run every time along with alclient.py or else it won't work prorperly as stop.txt in default condition has 'stop'.
6.Every testcase is saved of the form testcase_name.py, which has the code from indnt_exeserver.py, the lists link and testcase, and also the line sassy(link) (check the format of testcase at ln114)
7.compare fxn won't function properly if any user types "[display-svc] [debug] BRF data :".
8.If execution of whole file is completed, done.txt will have one line called 'done'.
9.done.txt and testcase.py files are buffer in arbd
10. make sure uinstall is installed in the ARBD

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
	link=[]		#link contains parsed lines of the logfile.
	
	link.append([0,"0000",'0:0:0'])
	

	
	li=0
	while qwer==0:
		
		
		stop_button=open("stop_button.txt","r")
		stop_button.seek(0,0)
		u_input=stop_button.readline()                            
		stop_button.close()
		
		#stop_button.py waits for 2 seconds after recieving the stop command to actually send stop to alclient.py
		#this is necessary as the last few BRF data lines in the log_file after the last keyboard event line is also required.
		line=s.recv(1024)
		testcase.append(str(line))
		if 'Keyboard event received' in line:
			ji=ex(link[li][1])			#make sure ex,ex2 is imported
			print_ln=str(ji) + ' : ' + str(ex2(link[li][1]))
			print print_ln	
			link[li].append(ji)  #imp:line and link[li][1] are not same, line = link[li+1][1]
			
			li=li+1
			link.append([li,line,timeparse(line)])	
		elif ('BRF data' in line):
			link[li].append(line)
		
		if u_input=='stop':
			s.send('stop')	
			f=s.recv(1024)		
			qwer+=1
		
		else:
			
			s.send('continue')
	
	link[len(link)-1].append(ex(link[li][1])) #last line parsing
	for i in range(0,len(link)):     #adding time difference
		if i==0 or i==len(link)-1:
			link[i].append(0)
		else :
			link[i].append(timedifference(link[i][2],link[i+1][2]))

	print s.recv(1024)
	print 'The test case recorded is:'
	for i in testcase:
		print i

	with open('int_exeserver.py','r') as f:	
    		lines = f.readlines()
    		
    		with open(testcase_name+'.py', "w") as f1:
        		f1.writelines(lines)
	
			f1.write('link='+str(link)+'\n')
			f1.write('testcase='+str(testcase)+'\n')
			f1.write('sassy(link)'+'\n')    #to call the function sassy
	
	#no need to close files, with automatically closes
	
	#link is the arsed one and testcase is the unparsed.
	


def execute(s,tc,ssh_c):
	
	#uses the earlier created paramiko.SSHClient() for sending testcase i.e ssh_c
	#creates two buffer files  in arbd, one is the testcase another is done.txt
	#executes the tetcase and records the logfiles independently 
	testcase_name=tc+'.py'
	dir_path = os.path.dirname(os.path.realpath(__file__))
	ftp_client=ssh_c.open_sftp()
	ftp_client.put(dir_path+'/'+testcase_name,'/home/ubuntu/'+testcase_name)
	time.sleep(1)	
	s.send(testcase_name)
	d=s.recv(1024)
	print d
	s.send('start execution')
	d=s.recv(1024)
	print d
	
	with open(testcase_name,'r') as f:
		 ideal_link=f.readlines()[-3]
	ideal_link=ideal_link.split('link=')
	ideal_link=eval(ideal_link[-1])
	print type(ideal_link)
	# now ideal link is a link in the format of link as in executer6

	s.send('continue')
	qwer=0
	executed_result=[]	#executed_result contains the unparsed lines as srecieved	
	resulted_link=[]		#resulted_link contains parsed lines of the logfile.
	
	resulted_link.append([0,"0000",'0:0:0'])
	
	u_input='o'
	
	l=0
	while qwer==0:
		#comparision is happening for l th item while recieved item is line. received item and compared items are not same
		line=s.recv(1024)
		executed_result.append(str(line))
		if ('BRF data' in line):
			resulted_link[l].append(line)
			print 'recieved:'+resulted_link[l][-1]
			q=len(resulted_link[l])-1
			if len(ideal_link[l])!=5 and (q!=len(ideal_link[l])-1):   # case1=if there is no BRF data between two Keyboard events; and case2= q has reached the last element of ideal_link[l] which is ["k=uiniput.K1",...]
				print 'ideal' + str(type(ideal_link[l][q]))	
				print ideal_link[l]
				print q
				print resulted_link[l]
		
				print ideal_link[l][q]			# ideal=[1,2,3,4,5,6] ,received=[1,2,3,4], ideal[q]=4
				if not compare(resulted_link[l][-1],ideal_link[l][q]):
					d=raw_input("To continue execution press c, else to stop press s:")
					if d=='s':
						u_input='stop'
		elif 'Keyboard event received' in line:
			ji=ex(resulted_link[l][1])			#make sure ex,ex2 is imported
			print_ln=str(ji) + ' : ' + str(ex2(resulted_link[l][1]))
			print print_ln	
			
			resulted_link[l].append(ji)  #imp:line and resulted_link[l][1] are not same, line = resulted_link[l+1][1]
			
			l=l+1
			resulted_link.append([l,line,timeparse(line)])	
		
		
		if u_input=='stop':
			s.send('stop')	
			f=s.recv(1024)		
			qwer+=1
		
		else:
			
			s.send('continue')
	
	resulted_link[len(resulted_link)-1].append(ex(resulted_link[l][1])) #last line parsing
	for i in range(0,len(resulted_link)):     #adding time difference
		if i==0 or i==len(resulted_link)-1:
			resulted_link[i].append(0)
		else :
			resulted_link[i].append(timedifference(resulted_link[i][2],resulted_link[i+1][2]))

	print s.recv(1024)
	print 'The test case recorded is:'
	for i in executed_result:
		print i

	with open('int_exeserver.py','r') as f:	
    		lines = f.readlines()
    		
    		with open("executed_"+testcase_name+'.py', "w") as f1:
        		f1.writelines(lines)
	
			f1.write('link='+str(link)+'\n')
			f1.write('testcase='+str(testcase)+'\n')
			f1.write('sassy(link)'+'\n')    #to call the function sassy
	
	#no need to close files, with automatically closes
	
	#link is the parsed one and testcase is the unparsed.
	
	
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
while wut !='x':
	s.send(wut)
	recv_msg=s.recv(1024)
	if wut == 'r':
		recordclient(s)
	elif wut == "e":
		tc=raw_input("Please enter the name of test case to be executed(without '.py' or '.txt') :")
		#write code to make sure testcase exists
		execute(s,tc,ssh_client)
	wut=raw_input("Please enter 'r' to record or 'e' to execute a recorded test case or 'x' to exit connection:")


s.send(wut)
s.close()	#closes the socket, keep this at the last, or at the end of the loop


#----------------------------------------------------------------------------------------



		
	

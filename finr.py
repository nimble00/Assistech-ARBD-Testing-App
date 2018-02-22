import paramiko
from subprocess import call
import time
import sys
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.7.2',username='ubuntu',password='temppwd')

ftp_client=ssh_client.open_sftp()
ftp_client.put('/home/sudhi/COP/working_temporary/tcprecordserver.py','/home/ubuntu/tcprecordserver.py')
time.sleep(1)
ftp_client.put('/home/sudhi/COP/ser.sh','/home/ubuntu/ser.sh')
ftp_client.close()

print "SERVER INJECTED..."

time.sleep(1)

stdin,stdout,stderr=ssh_client.exec_command("chmod +x ser.sh")
print stdout.readlines()

'''stdin,stdout,stderr=ssh_client.exec_command('sudo -S ./ser.sh true')
stdin.write('temppwd\n')
print "stderr: ", stderr.readlines()
print stdout.readlines()

time.sleep(3)

print "SERVER LISTENING..."
call("python /home/sudhi/COP/working_temporary/tcprecordclient.py",shell=True)

stdin,stdout,stderr=ssh_client.exec_command("cd ..\ncd ..\ncd var/log/\nls -t | head -1")
logfile = stdout.readlines()
print stdout.readlines()
'''

'''
stdin,stdout,stderr=ssh_client.exec_command("tail -10 ")
logfile = stdout.readlines()
print stdout.readlines()'''

'''
ftp_client=ssh_client.open_sftp()
ftp_client.get('remotefileth','localfilepath')
ftp_client.close()
'''

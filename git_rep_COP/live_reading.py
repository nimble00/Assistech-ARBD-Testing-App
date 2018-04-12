import subprocess
import sys
from subprocess import PIPE
cmd1='ls -t /home/sudhi/COP/piping| head -1 '
p1 = subprocess.Popen(cmd1, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
				
chi=p1.communicate() 
		
llf=str(chi[0][:-1]) #llf=latest log file
print chi[0][:-1]

cmd2='tail -0f /home/sudhi/COP/piping/' + llf #'| grep  -E Keyboard.*event\|Current.*window\|BRF.*data'
		#cmd2='sudo sh -c "tail -0f /home/sudhi/COP/arbd.log_2018-03-12_12-33 | grep  -E Keyboard.*event\|Current.*window\|BRF.*data > /home/sudhi/COP/working_temporary/temp_log.txt" ' 	#make sure there is no space bw ' and sudo	
p2 = subprocess.Popen(cmd2, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)

for line in iter(lambda: p2.stdout.readline(),''):
		print line
					
		

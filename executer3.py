import os

#from executer import linker,ex
#j=linker('arbd_log_parsed.txt')

# grep sd arbdlogfiles/1/arbd.log_2017-12-12_09-28  


def linker(file):
	#file is a string
	
	'''This function produces a dictionary "link" from the log file.
	IMP NOTE: This function also produces a textfile log_parsed.txt.
	

	>>link is a list of lists with 0th element a number(the rank in which keyboard event was recieved), 1st element a str of "keyboard event recieved", from 2nd element str  which  has "Current window" and the last element a list of keys in the keyboard event line.
	Therefore link maps each keyboard event to zero, one or more than one current window line.
	The current window lines between keyboard event E1 and E2 are linked to E1.
	
	NOTE: The current window lines prior to the first key event(E1) is linked to the key '0000'(which is manually defined below)
	'''
	#link=[[0,"0000",'current window10','current window20',...,'current windown0',['K1','K2','K3']],[1,"Keyevent1",'current window11','current window2',...,'current windown2',['K1','K2','K3']],...]

	from executer3 import ex
	#file is the the unparsed log file name with path.
	cmnd = 'grep  -E Keyboard.*event\|Current.*window ' +str(file)+' > log_parsed.txt'
	os.system(cmnd)

	logp=open("log_parsed.txt","r")
	#to logp even unparsed file can be passed instead of log_parsed.txt
	link=[]
	link.append([0,"0000"])
	

	global l
	l=0
	for i in logp.readlines():
		if 'Current window' in i:
			link[l].append(i)
		elif 'Keyboard event received' in i:
			link[l].append(ex(link[l][1])) #make sure ex is imported

			l=l+1
			link.append([l,i])
	#readlines returns a list of strings, with each string equal to one line.
	link[len(link)-1].append(ex(link[l][1])) 
	return link




def ex(line):

#line is a str. ex parses the line to produce a list of keys(key_list)
#line="asdgKeyboard event: K1+K2+K3"  		key_list=['K1','K2','K3']	
		key_list=[]			
		j_1=line.split(": ")
		
			
		if len(j_1)==1 or j_1[-1]=='\n':
			key_list.append("No keyboard event recieved")
			
		else:
			j_2=j_1[-1].split("+")				
							
			s=j_2[-1][:-1]  #to remove "/n"
			j_2[-1]=s
			key_list=j_2
		return key_list





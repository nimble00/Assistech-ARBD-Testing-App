import os
import uinput
#from executer import linker,ex
#j=linker('arbd_log_parsed.txt')

# grep sd arbdlogfiles/1/arbd.log_2017-12-12_09-28  


def linker(fileh):
	#file is a string
	
	'''This function produces a dictionary "link" from the log file.
	IMP NOTE: This function also produces a textfile log_parsed.txt.
	IMP: make sure you in the defintion of linker you import other functions from the same executer file as linker.

	>>link is a list of lists with 0th element a number(the rank in which keyboard event was recieved), 1st element a str of "keyboard event recieved", from 2nd element str  which  has "Current window" and the last element a list of keys in the keyboard event line.
	Therefore link maps each keyboard event to zero, one or more than one current window line.
	The current window lines between keyboard event E1 and E2 are linked to E1.
	
	NOTE: The current window lines prior to the first key event(E1) is linked to the key '0000'(which is manually defined below)
	'''
	'''link=[  [0,"0000"     ,'0'   ,'current window10','current window20',...,'current windown0',['no_key']                               , 0]  ,
		   [1,"Keyevent1",'time','current window11','current window21',...,'current windown1',['k=uinput.KEY_K1','k=uinput.KEY_K2',...], timedifference],
		   [2,"Keyevent2",'time','current window12','current window22',...,'current windown2',['k=uinput.KEY_K1_2','k=uinput.KEY_K2_2',...], timedifference],		
					..........,
					..........,
		   [m,"Keyeventm",'time','current window1m','current window2m',...,'current windownm',['k=uinput.KEY_K1_m','k=uinput.KEY_K2_m',...], 0]                   ]'''

        #time is a str, time difference is int
	
	from executer5 import ex,timeparse,timedifference,di

	#file is the the unparsed log file name with path.
	#cmnd = 'grep  -E Keyboard.*event\|Current.*window ' +str(file)+' > log_parsed.txt'
	#os.system(cmnd)

	logp=open(fileh,"r")
	#to logp even unparsed file can be passed instead of log_parsed.txt
	link=[]
	link.append([0,"0000",'0:0:0'])
	

	global l
	l=0
        for i in logp.readlines():
		if 'Current window' in i:
			link[l].append(i)
		elif 'Keyboard event received' in i:
			link[l].append(ex(link[l][1])) #make sure ex is imported
			
			l=l+1
			link.append([l,i,timeparse(i)])
	logp.close()		
	#readlines returns a list of strings, with each string equal to one line.
	link[len(link)-1].append(ex(link[l][1])) 
	for i in range(0,len(link)):
		if i==0 or i==len(link)-1:
			link[i].append(0)
		else :
			link[i].append(timedifference(link[i][2],link[i+1][2]))
                               
	return link



def ex(line):

#line is a str. ex parses the line to produce a list of keys(key_list)
#line="asdgKeyboard event: K1+K2+K3"  		key_list=['uinput.KEY_K1','uinput.KEY_K2','No keyboard event received',..]	
		key_list=[]			
		j_1=line.split(": ")
		
			
		if len(j_1)==1 or j_1[-1]=='\n' :
			key_list.append("no_key")
			
		else:
			j_2=j_1[-1].split("+")				
							
			s=j_2[-1][:-1]  #to remove "/n"
			j_2[-1]=s
			
			for i in j_2:
					k=di(i)
					key_list.append(k)
		return key_list
def timeparse(line):
#line is a str. ex parses the line to produce a list of keys(key_list)
#line="asdgKeyboard event: K1+K2+K3"  		key_list=['K1','K2','K3']	
    t_1 = line.split(" ")
    return t_1[1][:-1]	

def timedifference(t1,t2):
    #print t1
    #print t2
    t_1 = t1.split(":")
    t_2 = t2.split(":")
    hour = int(t_2[0]) - int(t_1[0])
    minute = int(t_2[1])- int(t_1[1])
    second =  float(t_2[2]) - float(t_1[2])
    return (60*60*hour + 60*minute + second)
		
		
def di(i):
	#di takes 'l' returns a string ("k=uinput.KEY_L")
	#this means di or dict6 need not be defined in the server; but a uinput device has to be present in the server.IN the server in a loop of i we have to do exec(di(i)).
	'''	MANUALLY DEFINED:jf
	dict6[' ']: 'KEY_BASSBOOST'
	dict6['alt']='KEY_LEFTALT'
	dict6['enter']=dict6['return'] '''

	#{'J7': 'KEY_SHOP', 't2': 'KEY_CAMERA' , 't3': 'KEY_SOUND', 't0': 'KEY_PRINT', 'J3': 'KEY_SEARCH', 'J8': 'KEY_ALTERASE', 'J9': 'KEY_CANCEL', 'p2': 'KEY_PROG3', 'p3': 'KEY_PROG4', 'p1': 'KEY_PAUSECD', 'p6': 'KEY_CLOSE', 'p7': 'KEY_PLAY', 'p4': 'KEY_DASHBOARD', 'p5': 'KEY_SUSPEND', 'rjs_enter': 'KEY_CONNECT', 'J5': 'KEY_FINANCE', 'J6': 'KEY_SPORT', 'p9': 'KEY_BASSBOOST', 'J0': None, 'J1': 'KEY_EMAIL', 'J2': 'KEY_CHAT', 't1': 'KEY_HP', 'p8': 'KEY_FASTFORWARD'}
	dict6={'plusminus': 'KEY_KPPLUSMINUS', 'XF86AudioMute': 'KEY_MIN_INTERESTING', 'XF86MonBrightnessDown': 'KEY_BRIGHTNESSDOWN', 'less': 'KEY_102ND', 'Alt_R': 'KEY_RIGHTALT', 'Hangul_Hanja': 'KEY_HANJA', 'Hangul': 'KEY_HANGUEL', 'Caps_Lock': 'KEY_CAPSLOCK', 'comma': 'KEY_COMMA', 'NoSymbol': None, 'apostrophe': 'KEY_APOSTROPHE', 'XF86Reload': 'KEY_REFRESH', '1': 'KEY_1', 'XF86Battery': 'KEY_BATTERY', 'Control_R': 'KEY_RIGHTCTRL', 'KP_Down': 'KEY_KP2', 'Undo': 'KEY_UNDO', 'XF86AudioForward': 'KEY_FASTFORWARD', '0': 'KEY_0', 'KP_Insert': 'KEY_KP0', 'XF86Close': 'KEY_CLOSE', '8': 'KEY_8', 'SunFront': 'KEY_FRONT', 'Control_L': 'KEY_LEFTCTRL', 'XF86Send': 'KEY_SEND', '7': 'KEY_7', 'XF86WLAN': 'KEY_WLAN', 'F2': 'KEY_F2', 'XF86TouchpadOff': 'KEY_F23', 'XF86Sleep': 'KEY_SLEEP', 'b': 'KEY_B', 'XF86Search': 'KEY_SEARCH', 'XF86Save': 'KEY_SAVE', 'XF86KbdLightOnOff': 'KEY_KBDILLUMTOGGLE', 'XF86Launch1': 'KEY_PROG1', 'Help': 'KEY_HELP', 'Right': 'KEY_RIGHT', 'd': 'KEY_D', 'XF86MonBrightnessUp': 'KEY_BRIGHTNESSUP', 'h': 'KEY_H', 'Mode_switch': None, 'l': 'KEY_L', 'p': 'KEY_P', 'SunProps': 'KEY_PROPS', 't': 'KEY_T', 'Tab': 'KEY_TAB', 'F9': 'KEY_F9', 'x': 'KEY_X', 'XF86ScreenSaver': 'KEY_SCREENLOCK', 'XF86Phone': 'KEY_PHONE','alt':'KEY_LEFTALT', 'Alt_L': 'KEY_LEFTALT', 'parenright': 'KEY_KPRIGHTPAREN', 'XF86MailForward': 'KEY_FORWARDMAIL', 'End': 'KEY_END', 'XF86LaunchA': 'KEY_SCALE', 'XF86LaunchB': 'KEY_DASHBOARD', 'Next': 'KEY_PAGEDOWN', 'XF86Display': 'KEY_SWITCHVIDEOMODE', 'Print': 'KEY_PRINT', 'XF86AudioStop': 'KEY_STOPCD', 'KP_Decimal': 'KEY_KPCOMMA', 'Henkan_Mode': 'KEY_HENKAN', 'KP_Home': 'KEY_KP7', 'space': 'KEY_SPACE', 'XF86AudioMicMute': 'KEY_F20', 'XF86Bluetooth': 'KEY_BLUETOOTH', '4': 'KEY_4', 'XF86Calculator': 'KEY_CALC', 'Cancel': 'KEY_CANCEL', '3': 'KEY_3', 'XF86TouchpadToggle': 'KEY_F21', 'slash': 'KEY_SLASH', 'KP_Begin': 'KEY_KP5', 'KP_End': 'KEY_KP1', 'XF86Documents': 'KEY_DOCUMENTS', 'v': 'KEY_V', 'Up': 'KEY_UP', 'Prior': 'KEY_PAGEUP', 'XF86Back': 'KEY_BACK', 'F12': 'KEY_F12', 'F10': 'KEY_F10', 'F11': 'KEY_F11', 'Delete': 'KEY_DELETE', 'XF86Explorer': 'KEY_FILE', 'c': 'KEY_C', 'XF86MyComputer': 'KEY_COMPUTER', 'g': 'KEY_G', 'Redo': 'KEY_REDO', 'k': 'KEY_K', 'equal': 'KEY_EQUAL', 'o': 'KEY_O', 'Find': 'KEY_FIND', 'XF86Paste': 'KEY_PASTE', 'XF86Launch9': 'KEY_F18', 's': 'KEY_S', 'w': 'KEY_W', 'XF86Xfer': 'KEY_XFER', 'Home': 'KEY_HOME', 'Katakana': 'KEY_KATAKANA', 'XF86Launch3': 'KEY_PROG3', 'XF86Launch4': 'KEY_PROG4', 'XF86Launch5': 'KEY_F14', 'XF86Launch6': 'KEY_F15', 'XF86Reply': 'KEY_REPLY', 'BackSpace': 'KEY_BACKSPACE', 'Pause': 'KEY_PAUSE', 'XF86RotateWindows': 'KEY_DIRECTION', 'XF86AudioRecord': 'KEY_RECORD', 'XF86MenuKB': 'KEY_MENU', 'period': 'KEY_DOT', 'Hiragana': 'KEY_HIRAGANA', 'KP_Equal': 'KEY_KPEQUAL', 'parenleft': 'KEY_KPLEFTPAREN', 'XF86AudioNext': 'KEY_NEXTSONG', 'XF86Tools': 'KEY_F13', 'Shift_R': 'KEY_RIGHTSHIFT', 'KP_Divide': 'KEY_KPSLASH', 'KP_Prior': 'KEY_KP9', 'XF86AudioPause': 'KEY_PAUSECD', 'XF86Shop': 'KEY_SHOP', 'XF86New': 'KEY_NEW', 'XF86Open': 'KEY_OPEN', '2': 'KEY_2', 'XF86ScrollDown': 'KEY_SCROLLDOWN', 'Num_Lock': 'KEY_NUMLOCK', '6': 'KEY_6', 'Shift_L': 'KEY_LEFTSHIFT', 'XF86Go': 'KEY_CONNECT', 'XF86WakeUp': 'KEY_WAKEUP', 'XF86AudioMedia': 'KEY_MEDIA', 'KP_Subtract': 'KEY_KPMINUS', 'XF86TaskPane': 'KEY_CYCLEWINDOWS', 'f': 'KEY_F', 'bracketleft': 'KEY_LEFTBRACE', 'XF86Mail': 'KEY_EMAIL', 'XF86AudioPrev': 'KEY_PREVIOUSSONG', 'XF86DOS': 'KEY_MSDOS', 'Left': 'KEY_LEFT', 'KP_Left': 'KEY_KP4', 'F1': 'KEY_F1', 'ISO_Level3_Shift': None, 'F3': 'KEY_F3', 'F4': 'KEY_F4', 'F5': 'KEY_F5', 'F6': 'KEY_F6', 'F7': 'KEY_F7', 'F8': 'KEY_F8', 'XF86Finance': 'KEY_FINANCE', 'j': 'KEY_J', 'KP_Enter': 'KEY_KPENTER', 'n': 'KEY_N', 'Down': 'KEY_DOWN', 'r': 'KEY_R', 'XF86Copy': 'KEY_COPY', 'XF86HomePage': 'KEY_HOMEPAGE', 'z': 'KEY_Z', 'Scroll_Lock': 'KEY_SCROLLLOCK', 'minus': 'KEY_MINUS', 'XF86Game': 'KEY_SPORT', 'semicolon': 'KEY_SEMICOLON', 'KP_Next': 'KEY_KP3', 'Menu': 'KEY_COMPOSE', 'XF86Eject': 'KEY_EJECTCLOSECD', 'backslash': 'KEY_BACKSLASH', 'Linefeed': 'KEY_LINEFEED', 'XF86WebCam': 'KEY_CAMERA', 'KP_Add': 'KEY_KPPLUS', 'XF86AudioRaiseVolume': 'KEY_VOLUMEUP', 'XF86AudioLowerVolume': 'KEY_VOLUMEDOWN', 'XF86Launch8': 'KEY_F17', 'Muhenkan': 'KEY_MUHENKAN','enter': 'KEY_ENTER', 'Return': 'KEY_ENTER', 'KP_Up': 'KEY_KP8', 'XF86KbdBrightnessUp': 'KEY_KBDILLUMUP', 'XF86AudioPlay': 'KEY_PLAY', 'XF86Suspend': 'KEY_SUSPEND', 'XF86ScrollUp': 'KEY_SCROLLUP', '5': 'KEY_5', 'XF86Cut': 'KEY_CUT', '9': 'KEY_9', 'bracketright': 'KEY_RIGHTBRACE', 'Insert': 'KEY_INSERT', 'Hiragana_Katakana': 'KEY_KATAKANAHIRAGANA', 'Super_R': 'KEY_RIGHTMETA', 'Escape': 'KEY_ESC', 'XF86KbdBrightnessDown': 'KEY_KBDILLUMDOWN', 'KP_Right': 'KEY_KP6', 'XF86AudioRewind': 'KEY_REWIND', 'XF86TouchpadOn': 'KEY_F22', 'XF86PowerOff': 'KEY_POWER', 'Super_L': 'KEY_LEFTMETA', 'KP_Delete': 'KEY_KPDOT', 'XF86Launch2': 'KEY_PROG2', 'grave': 'KEY_GRAVE', 'a': 'KEY_A', 'XF86Messenger': 'KEY_CHAT', 'e': 'KEY_E', 'XF86WWW': 'KEY_WWW', 'i': 'KEY_I', 'KP_Multiply': 'KEY_KPASTERISK', 'm': 'KEY_M', 'q': 'KEY_Q', 'XF86Favorites': 'KEY_BOOKMARKS', 'u': 'KEY_U', 'y': 'KEY_Y', 'XF86Forward': 'KEY_FORWARD', 'XF86Launch7': 'KEY_F16','ljs_right': 'KEY_SHOP', 't2': 'KEY_CAMERA', 't3': 'KEY_SOUND', 't0': 'KEY_PRINT', 'rjs_left': 'KEY_SEARCH', 'ljs_left': 'KEY_ALTERASE', 'ljs_enter': 'KEY_CANCEL', 'd3': 'KEY_PROG3', 'd2': 'KEY_PROG4', 'd7': 'KEY_PAUSECD', 'd5': 'KEY_CLOSE', 'd6': 'KEY_PLAY', 'd1': 'KEY_DASHBOARD', 'd4': 'KEY_SUSPEND', 'rjs_enter': 'KEY_CONNECT', 'ljs_down': 'KEY_FINANCE', 'ljs_up': 'KEY_SPORT', " ": 'KEY_BASSBOOST', 'psp': 'KEY_BASSBOOST', 'J0': None, 'rjs_up': 'KEY_EMAIL', 'rjs_right': 'KEY_CHAT', 't1': 'KEY_HP', 'd8': 'KEY_FASTFORWARD', 'rjs_down':'KEY_QUESTION'}
	
	
	return "k=uinput."+dict6[i]	

        		


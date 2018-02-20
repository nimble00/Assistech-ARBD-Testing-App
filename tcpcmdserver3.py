import socket
import subprocess

#these two are not used anywhere as of now:
import sys
import os
#------------------------------------------------------------------------------------------------------------
import uinput
Keyboard = uinput.Device([uinput.KEY_RESERVED, uinput.KEY_1, uinput.KEY_2, uinput.KEY_3, uinput.KEY_4, uinput.KEY_5, uinput.KEY_6
,    uinput.KEY_7 #8
,    uinput.KEY_8 #9
,    uinput.KEY_9 #10
,    uinput.KEY_0 #11
,    uinput.KEY_MINUS #12
,    uinput.KEY_EQUAL #13
,    uinput.KEY_BACKSPACE #
,    uinput.KEY_TAB #
,    uinput.KEY_Q #
,    uinput.KEY_W #
,    uinput.KEY_E #
,    uinput.KEY_R #
,    uinput.KEY_T #
,    uinput.KEY_Y #
,    uinput.KEY_U #
,    uinput.KEY_I #
,    uinput.KEY_O #
,    uinput.KEY_P #
,    uinput.KEY_LEFTBRACE #
,    uinput.KEY_RIGHTBRACE #
,    uinput.KEY_ENTER #
,    uinput.KEY_LEFTCTRL #
,    uinput.KEY_A #
,    uinput.KEY_S #
,    uinput.KEY_D #
,    uinput.KEY_F #
,    uinput.KEY_G #
,    uinput.KEY_H #
,    uinput.KEY_J #
,    uinput.KEY_K #
,    uinput.KEY_L #
,    uinput.KEY_SEMICOLON #
,    uinput.KEY_APOSTROPHE #
,    uinput.KEY_GRAVE #
,    uinput.KEY_LEFTSHIFT #
,    uinput.KEY_BACKSLASH #
,    uinput.KEY_Z #
,    uinput.KEY_X #
,    uinput.KEY_C #
,    uinput.KEY_V #
,    uinput.KEY_B #
,    uinput.KEY_N #
,    uinput.KEY_M #
,    uinput.KEY_COMMA #
,    uinput.KEY_DOT #
,    uinput.KEY_SLASH
,    uinput.KEY_RIGHTSHIFT
,    uinput.KEY_KPASTERISK
,    uinput.KEY_LEFTALT
,    uinput.KEY_SPACE
,    uinput.KEY_CAPSLOCK
,    uinput.KEY_F1
,    uinput.KEY_F2
,    uinput.KEY_F3
,    uinput.KEY_F4
,    uinput.KEY_F5
,    uinput.KEY_F6
,    uinput.KEY_F7
,    uinput.KEY_F8
,    uinput.KEY_F9
,    uinput.KEY_F10
,    uinput.KEY_NUMLOCK
,    uinput.KEY_SCROLLLOCK
,    uinput.KEY_KP7
,    uinput.KEY_KP8
,    uinput.KEY_KP9
,    uinput.KEY_KPMINUS
,    uinput.KEY_KP4
,    uinput.KEY_KP5
,    uinput.KEY_KP6
,    uinput.KEY_KPPLUS
,    uinput.KEY_KP1
,    uinput.KEY_KP2
,    uinput.KEY_KP3
,    uinput.KEY_KP0
,    uinput.KEY_KPDOT
,    uinput.KEY_ZENKAKUHANKAKU
,    uinput.KEY_102ND
,    uinput.KEY_F11
,    uinput.KEY_F12
,    uinput.KEY_RO
,    uinput.KEY_KATAKANA
,    uinput.KEY_HIRAGANA
,    uinput.KEY_HENKAN
,    uinput.KEY_KATAKANAHIRAGANA
,    uinput.KEY_MUHENKAN
,    uinput.KEY_KPJPCOMMA
,    uinput.KEY_KPENTER
,    uinput.KEY_RIGHTCTRL
,    uinput.KEY_KPSLASH
,    uinput.KEY_SYSRQ
,    uinput.KEY_RIGHTALT
,    uinput.KEY_LINEFEED
,    uinput.KEY_HOME
,    uinput.KEY_UP
,    uinput.KEY_PAGEUP
,    uinput.KEY_LEFT
,    uinput.KEY_RIGHT
,    uinput.KEY_END
,    uinput.KEY_DOWN
,    uinput.KEY_PAGEDOWN
,    uinput.KEY_INSERT
,    uinput.KEY_DELETE
,    uinput.KEY_MACRO
,    uinput.KEY_MUTE
,    uinput.KEY_VOLUMEDOWN
,    uinput.KEY_VOLUMEUP
,    uinput.KEY_POWER
,    uinput.KEY_KPEQUAL
,    uinput.KEY_KPPLUSMINUS
,    uinput.KEY_PAUSE
,    uinput.KEY_SCALE
,    uinput.KEY_KPCOMMA
,    uinput.KEY_HANGEUL
,    uinput.KEY_HANGUEL
,    uinput.KEY_HANJA
,    uinput.KEY_YEN
,    uinput.KEY_LEFTMETA
,    uinput.KEY_RIGHTMETA
,    uinput.KEY_COMPOSE #127
,    uinput.KEY_F13 #183
,    uinput.KEY_F14
,    uinput.KEY_F15
,    uinput.KEY_F16
,    uinput.KEY_F17
,    uinput.KEY_F18
,    uinput.KEY_F19
,    uinput.KEY_F20
,    uinput.KEY_F21
,    uinput.KEY_F22
,    uinput.KEY_F23
,    uinput.KEY_F24
,    uinput.KEY_PLAYCD
,    uinput.KEY_PAUSECD
,    uinput.KEY_PROG3
,    uinput.KEY_PROG4
,    uinput.KEY_DASHBOARD
,    uinput.KEY_SUSPEND
,    uinput.KEY_CLOSE
,    uinput.KEY_PLAY
,    uinput.KEY_FASTFORWARD
,    uinput.KEY_BASSBOOST
,    uinput.KEY_PRINT
,    uinput.KEY_HP
,    uinput.KEY_CAMERA
,    uinput.KEY_SOUND
,    uinput.KEY_QUESTION
,    uinput.KEY_EMAIL
,    uinput.KEY_CHAT
,    uinput.KEY_SEARCH
,    uinput.KEY_CONNECT
,    uinput.KEY_FINANCE
,    uinput.KEY_SPORT
,    uinput.KEY_SHOP
,    uinput.KEY_ALTERASE
,    uinput.KEY_CANCEL
,    uinput.KEY_BRIGHTNESSDOWN
,    uinput.KEY_BRIGHTNESSUP #225
,    uinput.KEY_UNKNOWN #240
,    uinput.KEY_VIDEO_NEXT #241
,    uinput.KEY_VIDEO_PREV #242
#    uinput.KEY_
])

#------------------------------------------------------------------------------------------------------------------------------
def di(i):
	#{'J7': 'KEY_SHOP', 't2': 'KEY_CAMERA' , 't3': 'KEY_SOUND', 't0': 'KEY_PRINT', 'J3': 'KEY_SEARCH', 'J8': 'KEY_ALTERASE', 'J9': 'KEY_CANCEL', 'p2': 'KEY_PROG3', 'p3': 'KEY_PROG4', 'p1': 'KEY_PAUSECD', 'p6': 'KEY_CLOSE', 'p7': 'KEY_PLAY', 'p4': 'KEY_DASHBOARD', 'p5': 'KEY_SUSPEND', 'J4': 'KEY_CONNECT', 'J5': 'KEY_FINANCE', 'J6': 'KEY_SPORT', 'p9': 'KEY_BASSBOOST', 'J0': None, 'J1': 'KEY_EMAIL', 'J2': 'KEY_CHAT', 't1': 'KEY_HP', 'p8': 'KEY_FASTFORWARD'}
	dict6={'plusminus': 'KEY_KPPLUSMINUS', 'XF86AudioMute': 'KEY_MIN_INTERESTING', 'XF86MonBrightnessDown': 'KEY_BRIGHTNESSDOWN', 'less': 'KEY_102ND', 'Alt_R': 'KEY_RIGHTALT', 'Hangul_Hanja': 'KEY_HANJA', 'Hangul': 'KEY_HANGUEL', 'Caps_Lock': 'KEY_CAPSLOCK', 'comma': 'KEY_COMMA', 'NoSymbol': None, 'apostrophe': 'KEY_APOSTROPHE', 'XF86Reload': 'KEY_REFRESH', '1': 'KEY_1', 'XF86Battery': 'KEY_BATTERY', 'Control_R': 'KEY_RIGHTCTRL', 'KP_Down': 'KEY_KP2', 'Undo': 'KEY_UNDO', 'XF86AudioForward': 'KEY_FASTFORWARD', '0': 'KEY_0', 'KP_Insert': 'KEY_KP0', 'XF86Close': 'KEY_CLOSE', '8': 'KEY_8', 'SunFront': 'KEY_FRONT', 'Control_L': 'KEY_LEFTCTRL', 'XF86Send': 'KEY_SEND', '7': 'KEY_7', 'XF86WLAN': 'KEY_WLAN', 'F2': 'KEY_F2', 'XF86TouchpadOff': 'KEY_F23', 'XF86Sleep': 'KEY_SLEEP', 'b': 'KEY_B', 'XF86Search': 'KEY_SEARCH', 'XF86Save': 'KEY_SAVE', 'XF86KbdLightOnOff': 'KEY_KBDILLUMTOGGLE', 'XF86Launch1': 'KEY_PROG1', 'Help': 'KEY_HELP', 'Right': 'KEY_RIGHT', 'd': 'KEY_D', 'XF86MonBrightnessUp': 'KEY_BRIGHTNESSUP', 'h': 'KEY_H', 'Mode_switch': None, 'l': 'KEY_L', 'p': 'KEY_P', 'SunProps': 'KEY_PROPS', 't': 'KEY_T', 'Tab': 'KEY_TAB', 'F9': 'KEY_F9', 'x': 'KEY_X', 'XF86ScreenSaver': 'KEY_SCREENLOCK', 'XF86Phone': 'KEY_PHONE', 'Alt_L': 'KEY_LEFTALT', 'parenright': 'KEY_KPRIGHTPAREN', 'XF86MailForward': 'KEY_FORWARDMAIL', 'End': 'KEY_END', 'XF86LaunchA': 'KEY_SCALE', 'XF86LaunchB': 'KEY_DASHBOARD', 'Next': 'KEY_PAGEDOWN', 'XF86Display': 'KEY_SWITCHVIDEOMODE', 'Print': 'KEY_PRINT', 'XF86AudioStop': 'KEY_STOPCD', 'KP_Decimal': 'KEY_KPCOMMA', 'Henkan_Mode': 'KEY_HENKAN', 'KP_Home': 'KEY_KP7', 'space': 'KEY_SPACE', 'XF86AudioMicMute': 'KEY_F20', 'XF86Bluetooth': 'KEY_BLUETOOTH', '4': 'KEY_4', 'XF86Calculator': 'KEY_CALC', 'Cancel': 'KEY_CANCEL', '3': 'KEY_3', 'XF86TouchpadToggle': 'KEY_F21', 'slash': 'KEY_SLASH', 'KP_Begin': 'KEY_KP5', 'KP_End': 'KEY_KP1', 'XF86Documents': 'KEY_DOCUMENTS', 'v': 'KEY_V', 'Up': 'KEY_UP', 'Prior': 'KEY_PAGEUP', 'XF86Back': 'KEY_BACK', 'F12': 'KEY_F12', 'F10': 'KEY_F10', 'F11': 'KEY_F11', 'Delete': 'KEY_DELETE', 'XF86Explorer': 'KEY_FILE', 'c': 'KEY_C', 'XF86MyComputer': 'KEY_COMPUTER', 'g': 'KEY_G', 'Redo': 'KEY_REDO', 'k': 'KEY_K', 'equal': 'KEY_EQUAL', 'o': 'KEY_O', 'Find': 'KEY_FIND', 'XF86Paste': 'KEY_PASTE', 'XF86Launch9': 'KEY_F18', 's': 'KEY_S', 'w': 'KEY_W', 'XF86Xfer': 'KEY_XFER', 'Home': 'KEY_HOME', 'Katakana': 'KEY_KATAKANA', 'XF86Launch3': 'KEY_PROG3', 'XF86Launch4': 'KEY_PROG4', 'XF86Launch5': 'KEY_F14', 'XF86Launch6': 'KEY_F15', 'XF86Reply': 'KEY_REPLY', 'BackSpace': 'KEY_BACKSPACE', 'Pause': 'KEY_PAUSE', 'XF86RotateWindows': 'KEY_DIRECTION', 'XF86AudioRecord': 'KEY_RECORD', 'XF86MenuKB': 'KEY_MENU', 'period': 'KEY_DOT', 'Hiragana': 'KEY_HIRAGANA', 'KP_Equal': 'KEY_KPEQUAL', 'parenleft': 'KEY_KPLEFTPAREN', 'XF86AudioNext': 'KEY_NEXTSONG', 'XF86Tools': 'KEY_F13', 'Shift_R': 'KEY_RIGHTSHIFT', 'KP_Divide': 'KEY_KPSLASH', 'KP_Prior': 'KEY_KP9', 'XF86AudioPause': 'KEY_PAUSECD', 'XF86Shop': 'KEY_SHOP', 'XF86New': 'KEY_NEW', 'XF86Open': 'KEY_OPEN', '2': 'KEY_2', 'XF86ScrollDown': 'KEY_SCROLLDOWN', 'Num_Lock': 'KEY_NUMLOCK', '6': 'KEY_6', 'Shift_L': 'KEY_LEFTSHIFT', 'XF86Go': 'KEY_CONNECT', 'XF86WakeUp': 'KEY_WAKEUP', 'XF86AudioMedia': 'KEY_MEDIA', 'KP_Subtract': 'KEY_KPMINUS', 'XF86TaskPane': 'KEY_CYCLEWINDOWS', 'f': 'KEY_F', 'bracketleft': 'KEY_LEFTBRACE', 'XF86Mail': 'KEY_EMAIL', 'XF86AudioPrev': 'KEY_PREVIOUSSONG', 'XF86DOS': 'KEY_MSDOS', 'Left': 'KEY_LEFT', 'KP_Left': 'KEY_KP4', 'F1': 'KEY_F1', 'ISO_Level3_Shift': None, 'F3': 'KEY_F3', 'F4': 'KEY_F4', 'F5': 'KEY_F5', 'F6': 'KEY_F6', 'F7': 'KEY_F7', 'F8': 'KEY_F8', 'XF86Finance': 'KEY_FINANCE', 'j': 'KEY_J', 'KP_Enter': 'KEY_KPENTER', 'n': 'KEY_N', 'Down': 'KEY_DOWN', 'r': 'KEY_R', 'XF86Copy': 'KEY_COPY', 'XF86HomePage': 'KEY_HOMEPAGE', 'z': 'KEY_Z', 'Scroll_Lock': 'KEY_SCROLLLOCK', 'minus': 'KEY_MINUS', 'XF86Game': 'KEY_SPORT', 'semicolon': 'KEY_SEMICOLON', 'KP_Next': 'KEY_KP3', 'Menu': 'KEY_COMPOSE', 'XF86Eject': 'KEY_EJECTCLOSECD', 'backslash': 'KEY_BACKSLASH', 'Linefeed': 'KEY_LINEFEED', 'XF86WebCam': 'KEY_CAMERA', 'KP_Add': 'KEY_KPPLUS', 'XF86AudioRaiseVolume': 'KEY_VOLUMEUP', 'XF86AudioLowerVolume': 'KEY_VOLUMEDOWN', 'XF86Launch8': 'KEY_F17', 'Muhenkan': 'KEY_MUHENKAN', 'Return': 'KEY_ENTER', 'KP_Up': 'KEY_KP8', 'XF86KbdBrightnessUp': 'KEY_KBDILLUMUP', 'XF86AudioPlay': 'KEY_PLAY', 'XF86Suspend': 'KEY_SUSPEND', 'XF86ScrollUp': 'KEY_SCROLLUP', '5': 'KEY_5', 'XF86Cut': 'KEY_CUT', '9': 'KEY_9', 'bracketright': 'KEY_RIGHTBRACE', 'Insert': 'KEY_INSERT', 'Hiragana_Katakana': 'KEY_KATAKANAHIRAGANA', 'Super_R': 'KEY_RIGHTMETA', 'Escape': 'KEY_ESC', 'XF86KbdBrightnessDown': 'KEY_KBDILLUMDOWN', 'KP_Right': 'KEY_KP6', 'XF86AudioRewind': 'KEY_REWIND', 'XF86TouchpadOn': 'KEY_F22', 'XF86PowerOff': 'KEY_POWER', 'Super_L': 'KEY_LEFTMETA', 'KP_Delete': 'KEY_KPDOT', 'XF86Launch2': 'KEY_PROG2', 'grave': 'KEY_GRAVE', 'a': 'KEY_A', 'XF86Messenger': 'KEY_CHAT', 'e': 'KEY_E', 'XF86WWW': 'KEY_WWW', 'i': 'KEY_I', 'KP_Multiply': 'KEY_KPASTERISK', 'm': 'KEY_M', 'q': 'KEY_Q', 'XF86Favorites': 'KEY_BOOKMARKS', 'u': 'KEY_U', 'y': 'KEY_Y', 'XF86Forward': 'KEY_FORWARD', 'XF86Launch7': 'KEY_F16','J7': 'KEY_SHOP', 't2': 'KEY_CAMERA', 't3': 'KEY_SOUND', 't0': 'KEY_PRINT', 'J3': 'KEY_SEARCH', 'J8': 'KEY_ALTERASE', 'J9': 'KEY_CANCEL', 'd3': 'KEY_PROG3', 'd2': 'KEY_PROG4', 'd7': 'KEY_PAUSECD', 'd5': 'KEY_CLOSE', 'd6': 'KEY_PLAY', 'd1': 'KEY_DASHBOARD', 'd4': 'KEY_SUSPEND', 'J4': 'KEY_CONNECT', 'J5': 'KEY_FINANCE', 'J6': 'KEY_SPORT', 'psp': 'KEY_BASSBOOST', 'J0': None, 'J1': 'KEY_EMAIL', 'J2': 'KEY_CHAT', 't1': 'KEY_HP', 'd8': 'KEY_FASTFORWARD'}
	
	
	return dict6[i]
#----------------------------------------------------------------------------------------------------------------------------------

def Main():
	print" SERVER TURNED ON"
	s=socket.socket()
	host=''
	port=2300
	s.bind((host,port))
	s.listen(1)
	c,addr=s.accept()
	print "Connection from:" + str(addr)
	#commands is the list of list, containing all commands executed	
	commands=[]
	global l
	l=0
	while l==0:
	    command=c.recv(1024)
		# command will be of the form "['K1','K2',..]"   , command is a string
 	    if not command:
	   		break
	    elif str(command)=="stop":
			c.send("The server socket is closed.")
			c.close()
			l+=1
			print "The client disconnected."
	    else:
			print "Command passed:" + str(command)
			

#-------------------------------------------------------------------------------------------------------------------

			try:			
				#this is the output execution and output recording part
				
				exec("command_list="+command)
				#command_list is a list of the form ['K1','K2',..]
				combo=[]
				for i in command_list:
					s=di(i)
					exec("k=uinput."+s)
					combo.append(k)
				Keyboard.emit_combo(combo)
				print "Keyboard event recieved"
				
			
			except Exception as e:
				print "An error occured execution."
				output="An error occured in output recording/execution ;Error in recording :"+ e.__doc__ +", "+"Error message:"+ e.message

			else:
				output="Keyboard event executed"
				print "Keyboard event executed"

#-------------------------------------------------------------------------------------------------------------------
						
			c.send(output)
			print "Waiting for next command"
	

if __name__ == '__main__':
	Main()

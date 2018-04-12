import socket
import subprocess
from subprocess import PIPE,Popen,call
import time

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

#-------------------------------------------------------------------------------------------------------------------
def sassy(link):
	for j in link:
		
		try :
			command_list= j[-2]  #command_list is a list of the form ['k=uinput.KEY_K1','k=uinput.KEY_K2',...]
			delta=j[-i]			
			combo=[]
			for i in command_list:
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
		except Exception as e:
			#print "An error occured in execution."
			output="An error occured in execution; Error"+ e.__doc__ +", "+"Error message:"+ e.message
#link=[]	
#sassy(link)


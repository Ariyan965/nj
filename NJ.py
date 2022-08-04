import os,time,platform
print('\n\x1b[1;37m[•] Checking Update...');time.sleep(0.5)
os.system('git pull')
os.system('xdg-open https://www.facebook.com/groups/351076900316263/permalink/374959374594682/')
logo = ("""\033[1;37m    
                             
         ,--.        ,---._  
       ,--.'|      .-- -.' \ 
   ,--,:  : |      |    |   :
,`--.'`|  ' :      :    ;   |
|   :  :  | |      :        |
:   |   \ | :      |    :   :
|   : '  '; |      :         
'   ' ;.    ;      |    ;   |
|   | | \   |  ___ l         
'   : |  ; .'/    /\    J   :
|   | '`--' /  ../  `..-    ,
'   : |     \    \         ; 
;   |.'      \    \      ,'  
'---'         "---....--'    
                             
❤
(!)══════════════════════════════════════════
(!) Author   : Ariyan
(!) Guthub   : Ariyan Ahmed Nazmul
(!) Facebook :Ariyan\_ :* 3:) :* 3:) :* 3:) :* Ariyan
(!) Type     : Free
(!) Version  : 1.2.0
\033[1;37m(!)══════════════════════════════════════════""")
if not os.path.isfile('😃.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/AKING110/Data/main/AKING32.so > AKING32.so')
if not os.path.isfile('BD.so'):
	os.system('clear')
	print(logo)
	print('[√] installing Files ')
	os.system('curl -L https://raw.githubusercontent.com/AKING110/Data/main/BD.so > BD.so')
def Run():
	bit = platform.architecture()[0]
	os.system('clear')
	print(logo)
	print('[•] Choose Your Country For Cloning\n\033[1;37m(!)══════════════════════════════════════════')
	print('[1] Pak Cloning \n[2] BD Cloning\n[0] Exit')
	Aking = input('[•] Choose : ')
	if Aking =='1':
		if bit =='32bit':
			import AKING32
		elif bit =='64bit':
			import AKING
	elif Aking =='2':
		if bit =='32bit':
			import BD32
		elif bit =='64bit':
			import BD
Run()

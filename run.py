#!/usr/bin/env python3

import os
import sys
import time

memuos = ('''\033[1;33;40m
              
               |!| MEMU SYSTEM |!|
            [1] UBUNTU
            [2] KALI LINUX
            [3] TERMUX
            [4] GOOGLE SHELL
            [5] WINDOWS
           [99] EXIT

''')

memusystem = ('''\033[1;33;40m
 
               |!| MEMU TOOL |!|
            [1] SETUP
            [2] CONSOLE
            [3] UPDATE
            [4] CR
            [5] EEXI

''')

cr=('''\033[0;32m

╦═╗ ╦╦ ╦╔═╗╔═╗╦╔═╦ ╦╔═╗╦ ╦
╠╦╝ ║╠═╣╠═╣║  ╠╩╗╚╦╝║ ║║ ║
╩╚═╚╝╩ ╩╩ ╩╚═╝╩ ╩ ╩ ╚═╝╚═╝ o
=================================
Project จัดทำโดย Sakol Thaneerat ได้ดัดเเปลง ทำเพื่อเป็น Tool ในการใช้ได้ง่ายขึ้น 

''')

xr=("______________________________________________________")

def lowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2.0/90)
def exit():
  os.system("exit")

lowprint(memuos)

memusysytem = input("NUMBER : ")

if memusysytem == '1':

  os.system("clear")

  lowprint(memusystem)
  
  x = input("NUMBER : ")

  if x == "1":
    os.system("sudo apt install python python2 python3;sudo apt install python3-pip")
    os.system("pip install python-obfuscator")
    os.system("python3 run.py")

  if x == "2":
    y = input("INPUT FILE PYTHON : ")
    os.system("pyobfuscate -i %s -r True" %(y))
    os.system("python3 run.py")

  if x == "3":
    os.system("git pull https://github.com/sakol289/pyobf")
    os.system("python3 run.py")

  if x == "4":
    lowprint(cr)
    lowprint(xr)
    input("PRESS ENTER : ")
    os.system("python3 run.py")

  if x == "5":
    exit()

if memusysytem == '2':

  os.system(("clear"))

  lowprint(memusystem)

  x = input("NUMBER : ")

  if x == "1":
    os.system("sudo apt install python python2 python3;sudo apt install python3-pip")
    os.system("pip install python-obfuscator")
    os.system("python3 run.py")

  if x == "2":
    y = input("INPUT FILE PYTHON : ")
    os.system("pyobfuscate -i %s -r True" %(y))
    os.system("python3 run.py")

  if x == "3":
    os.system("git pull https://github.com/sakol289/pyobf")
    os.system("python3 run.py")

  if x == "4":
    lowprint(cr)
    lowprint(xr)
    input("PRESS ENTER : ")
    os.system("python3 run.py")

  if x == "5":
    exit()

if memusysytem == '3':

  os.system("clear")

  lowprint(memusystem)

  x = input("NUMBER : ")

  if x == "1":
    os.system("sudo apt install python python2 python3;sudo apt install python3-pip")
    os.system("pip install python-obfuscator")
    os.system("python3 run.py")

  if x == "2":
    y = input("INPUT FILE PYTHON : ")
    os.system("pyobfuscate -i %s -r True" %(y))   
    os.system("python3 run.py")

  if x == "3":
    os.system("git pull https://github.com/sakol289/pyobf")
    os.system("python3 run.py")

  if x == "4":
    lowprint(cr)
    lowprint(xr)
    input("PRESS ENTER : ")
    os.system("python3 run.py")

  if x == "5":
    exit()

if memusysytem == '4':

  os.system("clear")

  lowprint(memusystem)

  x = input("NUMBER : ")

  if x == "1":
    os.system("sudo apt install python python2 python3;sudo apt install python3-pip")
    os.system("pip install python-obfuscator")
    os.system("python3 run.py")

  if x == "2":
    y = input("INPUT FILE PYTHON : ")
    os.system("pyobfuscate -i %s -r True" %(y)) 
    os.system("python3 run.py")

  if x == "3":
    os.system("git pull https://github.com/sakol289/pyobf")
    os.system("python3 run.py")

  if x == "4":
    lowprint(cr)
    lowprint(xr)
    input("PRESS ENTER : ")
    os.system("python3 run.py")

  if x == "5":
    exit()

if memusysytem == "5":
  os.system("cls")

  lowprint(memusystem)

  x = input("NUMBER : ")

  if x == "1":
    os.system("start \"\" https://www.python.org/downloads/")
    os.system("pip install python-obfuscator")
    os.system("python3 run.py")

  if x == "2":
    y = input("INPUT FILE PYTHON : ")
    os.system("pyobfuscate -i %s -r True" %(y))
    os.system("python3 run.py")
       
  if x == "3":
    os.system("git pull https://github.com/sakol289/pyobf")

  if x == "4":
    lowprint(cr)
    lowprint(xr)
    input("PRESS ENTER : ")
    os.system("python3 run.py")

  if x == "5":
    exit()

if input == "99":
  exit()

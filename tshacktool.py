import os 
import time
from colorama import Fore
from module import handler


asciiBanner = Fore.RED + """
 _____ ____  _   _            _    _____           _  __     _____  _ 
|_   _/ ___|| | | | __ _  ___| | _|_   _|__   ___ | | \ \   / / _ \/ |
  | | \___ \| |_| |/ _` |/ __| |/ / | |/ _ \ / _ \| |  \ \ / / | | | |
  | |  ___) |  _  | (_| | (__|   <  | | (_) | (_) | |   \ V /| |_| | |
  |_| |____/|_| |_|\__,_|\___|_|\_\ |_|\___/ \___/|_|    \_/(_)___/|_|
                                                                      
          Neo | https://github.com/isthisneo | Türk Siber Hack
"""

toolList = Fore.LIGHTGREEN_EX + """
[1] Port scanner                              [2] Ip Tracker
[3] DDoS Flood                                [99] Help  \n\n"""

plus = asciiBanner + "\n\n" + toolList

os.system("clear")

print(plus)

tools = ["1","2","3","99"]

choices = ["Y", "N", "y", "n"]

portScanner = tools[0]
ipTracker = tools[1]
ddoS = tools[2]
helps = tools[3]

while True:
    toolChoose = input(Fore.WHITE + "Hangi toolu kullanmak istersiniz> ")
    # PORTSCANNER #
    if toolChoose == '1':
        handler.portscanner()
        tryportscanner = input(Fore.LIGHTGREEN_EX + '\n\nProgram kapatılsın mı ? [Y/N] ')
        if tryportscanner == 'y':
            print(Fore.LIGHTBLUE_EX + '\nProgram kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'Y':
            print(Fore.LIGHTBLUE_EX + '\nProgram kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryportscanner == 'n':
            break
        if tryportscanner == 'N':
            break
    # PORTSCANNER #
    
    # IP TRACKER #
    if toolChoose ==  '2':
        handler.iptracker()
        tryiptracker = input(Fore.LIGHTGREEN_EX + '\n\nProgram kapatılsın mı ? [Y/N] ')
        if tryiptracker == 'y':
            print(Fore.LIGHTBLUE_EX + '\nProgram kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryiptracker == 'Y':
            print(Fore.LIGHTBLUE_EX + '\nProgram kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryiptracker == 'n':
            break
        if tryiptracker == 'N':
            break
    # IP TRACKER #

    # DDOS TOOL # 
    if toolChoose == '3':
        handler.DDoS()
        tryddos = input(Fore.LIGHTGREEN_EX + '\n\nProgram kapatılsın mı ? [Y/N] ')
        if tryddos == 'y':
            print(Fore.LIGHTBLUE_EX + '\nProgram kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryddos == 'Y':
            print(Fore.LIGHTBLUE_EX + '\nProgram kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryddos == 'n':
            break
        if tryddos == 'N':
            break
    # DDOS TOOL #

    # HELP #
    if toolChoose == '99':
        os.system('clear')

        # PORT SCANNER HELP #

        print(Fore.LIGHTBLUE_EX + '\n\nAuthor : Neo\nGitHub : https://github.com/isthisneo\n')
        print(Fore.LIGHTGREEN_EX + 'Port scanner : \n\nPort scanner Neo tarafından kodlanan website\niçerisindeki açık portları gösteren bir programdır.')

        # PORT SCANNER HELP #

        # IP TRACKER HELP #

        print(Fore.LIGHTGREEN_EX + 'IP Tracker : \n\nIP Tracker Neo tarafından kodlanan bir programdır.\nIP Tracker programı IP adresinin ülkesini,şehrini vs. Gösterir')

        # IP TRACKER HELP

        # DDOS HELP #
        
        print(Fore.LIGHTGREEN_EX + 'DDoS : \n\nDDoS programımız websitenin pingini yükseltip belirli bir süre sonra\nWeb siteye erişimi engeller. (Program TCP Flood DDoS`tur.)')

        # DDOS HELP #

        tryhelp = input(Fore.LIGHTGREEN_EX + '\n\nProgram kapatılsın mı ? [Y/N] ')
        if tryhelp == 'y':
            print('Program kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryhelp == 'Y':
            print('Program kapatılıyor')
            time.sleep(5)
            os.system("clear")
            print(plus)
        if tryhelp == 'n':
            break
        if tryhelp == 'N':
            break

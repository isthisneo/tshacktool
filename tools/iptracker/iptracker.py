import time
import requests
import json
from colorama import Fore

asciiBanner = """
  ___________ __  __   ____         ______                __            
 /_  __/ ___// / / /  /  _/___     /_  __/________ ______/ /_____  _____
  / /  \__ \/ /_/ /   / // __ \     / / / ___/ __ `/ ___/ //_/ _ \/ ___/
 / /  ___/ / __  /  _/ // /_/ /    / / / /  / /_/ / /__/ ,< /  __/ /    
/_/  /____/_/ /_/  /___/ .___/    /_/ /_/   \__,_/\___/_/|_|\___/_/     
                      /_/                                              
        Neo | https://github.com/isthisneo | Türk Siber Hack
"""

print(Fore.LIGHTGREEN_EX + asciiBanner)

ip = input(Fore.LIGHTMAGENTA_EX + "Target IP> ")
api = "http://ip-api.com/json/"

res = requests.get(api + ip)


data = res.json()

print(Fore.LIGHTBLACK_EX + f"""
IP : {data['query']}
Ülke : {data['country']}
Şehir : {data['city']}
Ülke kodu : {data['countryCode']}
Saat dilimi : {data['timezone']}
LAT : {data['lat']}
LON : {data['lon']}
Servis Sağlayıcısı : {data['org']}""")
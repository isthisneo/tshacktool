import socket
import threading
import concurrent.futures
from colorama import Fore
import time

asciiBanner = Fore.RED + """
 _____ ____    ____            _     ____                                  
|_   _/ ___|  |  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
  | | \___ \  | |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  | |  ___) | |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
  |_| |____/  |_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|  
                Neo | https://github.com/isthisneo | Türk Siber Hack
"""
print(asciiBanner)

print_lock = threading.Lock()

ip = input(Fore.LIGHTMAGENTA_EX + "Enter the IP to scan> ")


def scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        with print_lock:
            print(Fore.LIGHTYELLOW_EX + "Port " + f"[{port}]" + " is open.")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)

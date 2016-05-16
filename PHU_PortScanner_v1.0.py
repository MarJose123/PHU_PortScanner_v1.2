#!/usr/bin/env python
import socket
import ipaddress
import sys
import platform
from datetime import datetime



def logo():
    print("\033[1;32;40m                             ____  _   _ _   _ \033[0;37;40m")
    print("\033[1;32;40m                            |  _ \| | | | | | | \033[0;37;40m")
    print("\033[1;32;40m                            | |_) | |_| | | | | \033[0;37;40m")
    print("\033[1;32;40m                            |  __/|  _  | |_| | \033[0;37;40m")
    print("\033[1;32;40m                            |_|   |_| |_|\___/ \033[0;37;40m")
    print("\033[5;32;40m                             PortScanner v1.2   \033[0;37;40m")




def start():
    print("\033[5;32;40m-\033[0;37;40m" * 20)
    print("\033[1;32;40mPlease wait, scanning remote host \033[0;37;40m", remoteServerIP)
    print("\033[5;32;40m-\033[0;37;40m" * 20)

    try:
        ##62000
        for port in list ([22,80,443,21,100,23,1604,0,101,102,104,8080,1234,1900,123,27960,27015,1024,3072,27665,65000,27665,1524,1900,19,161,27015,17,69,3072,1024,27444,31335,27665,1434,
                           1,5,7,18,20,29,37,42,43,49,53,69,70,79,103,109,110,115,118,119,137,139,143,150,156,161,179,190,194,197,396,444,4444,445,458,546,547,563,569,1080]):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("\033[1;32;40mPort\033[0;37;40m \033[1;31;40m{}:\033[0;37;40m \033[1;34;46m Open \033[0;37;40m".format(port))
            sock.close()

    except KeyboardInterrupt:
     sys.exit("\033[1;30;41mYou pressed Ctrl+C \033[0;37;40m")

    except socket.gaierror:
     sys.exit("\033[1;30;41m Hostname could not be resolved. Exiting \033[0;37;40m")

    except socket.error:
     sys.exit("\033[1;30;41m Couldn't connect to server \033[0;37;40m")




logo()
try:
    remoteServer = input("\033[1;32;40mEnter  host to scan: (example: 127.0.0.1)\033[0;37;40m")
    remoteServerIP = socket.gethostbyname(remoteServer)
except socket.error as e:
    sys.exit("\033[1;30;41mInvalid Input!, Exiting..\033[0;37;40m")

t1 = datetime.now()
start()

t2 = datetime.now()
total = t2 - t1
print("\033[1;31;40m Scanning Completed in: \033[0;37;40m", total)
print("\033[1;31;40m Created by: ~Ph03N1X \033[0;37;40m")
print("\033[1;31;40m www.github.com/Whoami213 \033[0;37;40m")
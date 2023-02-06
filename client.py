import socket
import os
import subprocess
import time as y
import time


s = socket.socket()
#i have tried using ip got from whatsmyip and thorugh LAN ip as well but unable to perform anything
#it works fine with LAN ip which we get through ipconfig but for WAN it doest have a look plz
host = '192.168.1.190'
port = 9999

def recv():
        try:
            data = s.recv(1048)
            p=str(data.decode("utf-8"))
            print("\nTAHIR: " + p)
        except socket.error as e:
            print(" NO NEW MESSAGE ")
def reply():
    print("TYPE A MESSAGE: ")
    cmd=input()
    s.send(str.encode(cmd))
    print("Message sent")

m=0
print("\t PLEASE WAIT CONNECTING TO SERVER.......")
while True:
    try:
        if m==0:
            s.connect((host, port))
            s.settimeout(0.5)
            print("\n \t\t \t CONNECTED SUCESSFULLY WITH SERVER ")
            m=m+1
        else:
            x=input("\nNO NEW MESSAGES PRESS ENTER TO CHECK FOR NEW MESSAGES OR TYPE R ANYTIME TO REPLY OR SEND MSG TO SERVER: ")
            if x=='r' or x=='R':
                reply()
            recv()
    except Exception as p:
        print(str(p))
        time.sleep(3)
        continue
















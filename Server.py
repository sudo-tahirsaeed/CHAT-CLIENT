import socket
import sys
from tkinter import*
import os
import time

# Create a Socket ( connect two computers)
def create_socket():
    try:

        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        s.bind((host, port))
        s.listen(10)
        print("Binding port Waiting for client to connect.... ")
    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address=s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    while True:
        x = input("\nNO NEW MESSAGES PRESS ENTER TO CHECK FOR NEW MESSAGES OR TYPE R ANYTIME TO REPLY OR SEND MSG TO SERVER: ")
        if x == 'R' or x == 'r':
            try:
                conn.settimeout(0.5)
                data = str(conn.recv(2048), "utf-8")
                p = data
                print("\nClient: " + p)
            except:
                   p2=1+1
            try:
                print("\nTYPE A MESSAGE: ")
                cmd = input()
                conn.send(str.encode(cmd))
                print("Message sent")
            except ConnectionResetError as a:
                print(" \n\tClient has been disconnected Message cant be send Thanks !   ")


        else:
                try:
                    conn.settimeout(0.5)
                    data = str(conn.recv(2048),"utf-8")
                    p = data
                    print("Client: " + p)

                except socket.timeout as sa:
                    print("No New Message")
                except ConnectionResetError as e:
                    print(" \n\tClient has been disconnected Message cant be send or received Thanks !   ")


    #conn.close()


create_socket()
bind_socket()
socket_accept()











#!/usr/bin/env python
# coding: utf-8

import socket
class Client:

    def __init__(self, host='localhost', port=15557):
        self.host = host
        self.port = port

    def connectTcp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # SOCK_STREAM -> TCP
        try:
            error = self.s.connect_ex((self.host, self.port))
            print ("Connected with TCP protocol (error="+str(error))
        except socket.error as msg:
            print(msg)

    def connectUdp(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # SOCK_DGRAM -> UDP
        self.s.connect((self.host, self.port))
        print ("Connected with UDP protocol")

    def send(self, message="Hello"):
        # pour python3 seulement
        self.s.send(bytes(message, 'UTF-8'))
        # si python2, alors utiliser la ligne suivante:
        # self.s.send(message)
        print("Sent message \""+message+"\"")

    def disconnect(self):
        self.s.close()
        print ("Disconnected")


i=0
c = {}
while(i < 10):
    c[i] = Client()
    c[i].connectTcp()
    c[i].send("Bonjour")
    c[i].disconnect()
    print("client number "+str(i))
    i=i+1

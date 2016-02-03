#!/usr/bin/env python
# coding: utf-8

import socket
import time
import threading

class Server:

    def __init__(self, host='', port=15557, maxConnexions=1):
        self.host = host
        self.port = port
        self.maxConnexions = maxConnexions

    def handleConnexion(self, client, address):
        print ("connected"+format( address ))
        response = client.recv(255) # réception d'une requète client
        if response != "":
            print (response)

    def startTcp(self):
        # AF_INET pour
        # SOCK_STREAM signifie TCP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.host, self.port))
        print ("serveur ecoute sur le port " + str(self.port))
        self.s.listen(1)    # maximum de demandes en attente dans la pile
        time.sleep(10)
        i=0
        while True:
                try:
                    client, address = self.s.accept()   # acceptation d'une demande de connexion
                    threading.Thread(target=self.handleConnexion, args=(client, address)).start()
                except socket.error as msg:
                    print(msg)

        print ("Close")
        client.close()

    def startUdp(self):
        # AF_INET pour
        # SOCK_DGRAM signifie UDP
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind((self.host, self.port))
        # boucle infinie pour serveur
        print ("serveur ecoute sur le port " + str(self.port))
        while True:
                data, addr = self.s.recvfrom(255)
                if data != "":
                    print (data)

        print ("Close")
        client.close()

    def stop(self):
        self.s.close()

server = Server()
server.startTcp()
server.stop()

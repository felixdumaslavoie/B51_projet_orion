# -*- coding: utf-8 -*-
import sys
import socket
import xmlrpc.client

               
class Controleur():
    def __init__(self):
        self.serveur=None
        self.monip=self.trouverIP() # la fonction pour retourner mon ip
        self.connecterserveur()
        self.menu()
        
    def menu(self):
        rep=input("Parlez à votre serveur! (o ou n)")
        if rep=="o":
            repnom= input("Inscrire votre nom svp ")
            repserveur=self.serveur.testServeur(repnom)
            print("Le serveur vous répond: ",repserveur)
            self.menu()
        else:
            print("Nous fermons le serveur dans ce cas!")
            self.quitter()
            
    def trouverIP(self): # fonction pour trouver le IP en 'pignant' gmail
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # on cree un socket
        s.connect(("gmail.com",80))    # on envoie le ping
        monip=s.getsockname()[0] # on analyse la reponse qui contient l'IP en position 0 
        s.close() # ferme le socket
        return monip
    
    def connecterserveur(self):
        ipserveur=self.monip 
        ad="http://"+ipserveur+":9999"
        self.serveur=xmlrpc.client.ServerProxy(ad)
            
    def quitter(self):
        if self.serveur:
            self.serveur.jequitte(self.monnom)
        self.vue.root.destroy()
            

        
if __name__=="__main__":
    c=Controleur()
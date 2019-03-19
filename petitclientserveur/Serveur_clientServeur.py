# -*- encoding: utf-8 -*-
from xmlrpc.server import SimpleXMLRPCServer
import sys
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
monip=s.getsockname()[0]
print("MON IP SERVEUR",monip)
s.close()

daemon=SimpleXMLRPCServer((monip, 9999)) 
        
                
class ControleurServeur(object):
    def __init__(self):
        self.derniervisiteur="Personne"
        
    def testServeur(self,nom="Personne"):
        if self.derniervisiteur=="Personne":
            msg="Personne n'est venu"
        else:
            msg=self.derniervisiteur+" est venu me voir"
            
        self.derniervisiteur=nom
        return msg
    
    def quitter(self):
        t=Timer(1,self.fermer)
        t.start()
        return "ferme"
    
    def fermer(self):
        print("FERMETURE DU SERVEUR")
        daemon.shutdown()

controleurServeur=ControleurServeur()
daemon.register_instance(controleurServeur)  
 
print("Serveur Pyro actif sous le nom \'controleurServeur\'")
daemon.serve_forever()


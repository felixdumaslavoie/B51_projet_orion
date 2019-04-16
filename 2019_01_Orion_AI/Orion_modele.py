 # -*- coding: utf-8 -*-
import os,os.path
import random
from Id import Id
from helper import Helper as hlp
from couleurs import *

#modif arbitraire
class Galaxie():
    def __init__(self,parent):
        self.bordure = 0
        self.listeX = []
        self.listeY = []
        self.parent = parent

        dir_path = os.path.dirname(os.path.realpath(__file__))
        # needed pour compatibilité entre vscode et eclipse

        self.txtNomEtoile = open(dir_path + "/nom_etoiles.txt","r")
        self.listeNomEtoile = self.txtNomEtoile.readlines()
        self.nbSysSolaire=150
        self.listeSysSolaire=[]

        for i in range(self.parent.largeur-2):
            self.listeX.append(i)

        for i in range(self.parent.hauteur-2):
            self.listeY.append(i)

        for i in range(self.nbSysSolaire):
            x=random.choice(self.listeX)
            self.listeX.remove(x)
            if x-1 in self.listeX:
                self.listeX.remove(x-1)
            if x+1 in self.listeX:
                self.listeX.remove(x+1)

            y=random.choice(self.listeY)
            self.listeY.remove(y)
            if y-1 in self.listeY:
                self.listeY.remove(y-1)
            if y+1 in self.listeY:
                self.listeY.remove(y+1)

            #TODO: S'assurer que les coordonnées et noms générés sont uniques.
            nom = self.listeNomEtoile.pop(random.randrange(len(self.listeNomEtoile)-1))
            s = SystemeSolaire(self,x,y,nom)
            self.listeSysSolaire.append(s)
            print("Étoile " + nom + " créée " + str(x) + " " + str(y))

class SystemeSolaire():
    def __init__(self,parent,x,y,nom):
        self.id=Id.prochainid()
        self.bordure = 0
        self.parent = parent
        self.nometoile = nom
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,7) #taille de l'étoile dans la vue de la galaxie
        self.nbdeplanete=random.randrange(2, 12)
        self.listePlanete = []
        for i in range(self.nbdeplanete):
            x=random.randrange(self.parent.parent.largeur-(2*self.bordure))+self.bordure
            y=random.randrange(self.parent.parent.hauteur-(2*self.bordure))+self.bordure
            p = Planete(self,x,y)
            self.listePlanete.append(p)

class Planete():
    couleurs={""}
    def __init__(self,parent,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,12)
        self.charbon=random.randrange(6)
        self.zinc=random.randrange(5)
        self.deuterium=random.randrange(10)
        self.fertile=random.randrange(1)
        self.listeStructure=[]*self.taille ## Chaque planète à une liste de bâtiments avec l'emplacement de chaque bâtiment
        self.ressource=[self.charbon,self.zinc,self.deuterium]
        self.viePlanete1=self.viePlanete()
        
        #self.couleur=self.listeNomCouleur[random.randrange(len(self.listeNomCouleur)-1)]

        self.couleur=random.choice(COULEURS);

    def viePlanete(self):
        if not self.listeStructure:
            self.viePlanete1=0
        else:
            for i in listeStructure[i]:
                self.viePlanete1+=self.listeStructure[i].vie
        return self.viePlanete1

    def estFertile(self):
        return self.fertile

class Structure():
                #nom structure, vie, cout, maintenance, exctraction
    Usine_Civile=["Usine_Civile",100,150,1,0]
    Usine_Militaire=["Usine_Militaire",200,225,2,0]
    Raffinerie_Diamant=["Raffinerie_Diamant",80,350,6,2]
    Raffinerie_Charbon=["Raffinerie_Charbon",50,150,2,3]
    Raffinerie_Isotope=["Raffinerie_Isotope",175,250,3,2]
    Ferme={"Ferme",75,50,1,2}
    Capitale={"Capitale",300,5000,10,100}

    def __init__(self,nom,x,y):
        self.nomStructure="VIDE"
        self.proprietaire=nom
        self.joueur
        self.x=x
        self.y=y

    def extractionStructure(self):
        for i in self.parent.listeStructure[i]:
            if self.parent.ressource[i]>0:
                if self.parent.ressource[i]<self.extraction:
                    self.extraction==self.parent.ressource[i]
                self.parent.ressource[i]-=self.extraction


    def maintenanceStructure(self):
        for i in self.parent.listeStructure[i]:
            self.credit-=self.maintenance

class UsineCivile(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Usine_Civile[0]
        self.cout=Structure.Usine_Civile[1]
        self.maintenance=Structure.Usine_Civile[2]
        self.production=Structure.Usine_Civile[3]

class UsineMilitaire(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Usine_Militaire[0]
        self.cout=Structure.Usine_Militaire[1]
        self.maintenance=Structure.Usine_Militaire[2]
        self.production=Structure.Usine_Militaire[3]

class RaffinerieDiamant(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Raffinerie_Diamant[0]
        self.cout=Structure.Raffinerie_Diamant[1]
        self.maintenance=Structure.Raffinerie_Diamant[2]
        self.production=Structure.Raffinerie_Diamant[3]

class RaffinerieCharbon(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Raffinerie_Charbon[0]
        self.cout=Structure.Raffinerie_Charbon[1]
        self.maintenance=Structure.Raffinerie_Charbon[2]
        self.production=Structure.Raffinerie_Charbon[3]

class RaffinerieIsotope(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Raffinerie_Isotope[0]
        self.cout=Structure.Raffinerie_Isotope[1]
        self.maintenance=Structure.Raffinerie_Isotope[2]
        self.production=Structure.Raffinerie_Isotope[3]

class Ferme(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Ferme[0]
        self.cout=Structure.Ferme[1]
        self.maintenance=Structure.Ferme[2]
        self.production=Structure.Ferme[3]

class Capitale(Structure):
    def __init__(self,nom,x,y,nomStructure):
        super().__init__(nom,x,y) # Constructeur de la classe structure
        self.nomStructure=Structure.Capitale[0]
        self.cout=Structure.Capitale[1]
        self.maintenance=Structure.Capitale[2]
        self.production=Structure.Capitale[3]

class Vaisseau():
    def __init__(self,nom,x,y, nomVaisseau="Vaisseau_Militaire"):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.cible=None
        self.nomVaisseau=nomVaisseau

        if nomVaisseau=="Vaisseau_Militaire":
            self.cargo=0
            self.energie=400
            self.vitesse=1

        if nomVaisseau=="Vaisseau_Civil":
            self.cargo=100
            self.energie=100
            self.vitesse=0

    def avancer(self):
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            ang=hlp.calcAngle(self.x,self.y,x,y)
            x1,y1=hlp.getAngledPoint(ang,self.vitesse,self.x,self.y)
            self.x,self.y=x1,y1 #int(x1),int(y1)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                print("RESSOURCES...",self.cible.id,self.proprietaire)
                self.cible.proprietaire=self.proprietaire
                #tempo=input("Continuersvp")
                self.cible=None
                print("Change cible")
        else:
            print("PAS DE CIBLE")

    def avancer1(self):
        if self.cible:
            x=self.cible.x
            if self.x>x:
                self.x-=self.vitesse
            elif self.x<x:
                self.x+=self.vitesse

            y=self.cible.y
            if self.y>y:
                self.y-=self.vitesse
            elif self.y<y:
                self.y+=self.vitesse
            if abs(self.x-x)<(2*self.cible.taille) and abs(self.y-y)<(2*self.cible.taille):
                self.cible=None


class Joueur():
    def __init__(self,parent,nom,planetemere,couleur):
        self.id=Id.prochainid()
        self.parent=parent
        self.nom=nom
        self.planetemere=planetemere
        self.planetemere.proprietaire=self.nom
        self.couleur=couleur
        self.planetescontrolees=[planetemere]
        self.flotte=[]
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerflotte":self.ciblerflotte}
        self.credit=1000
        self.nourriture=1000
        self.deuterium=5

    def creervaisseau(self,params):
        #planete,cible,type=params
        #is type=="explorer":

        v=Vaisseau(self.nom,self.planetemere.x+10,self.planetemere.y)
        print("Vaisseau",v.id, v.nomVaisseau, v.cargo, v.energie, v.vitesse)
        self.flotte.append(v)

    def creerStructure(self,nom,x,y,nomStructure,planete):
        t=Structure(self, nom,x,y,nomStructure)
        self.planete.listeStructure.append(t)

    #===========================================================================
    # def economie(self):
    #     for i in self.planetescontrolees:
    #         for j in i.listeStructure:
    #             j.extractionStructure
    #===========================================================================

    def ciblerflotte(self,ids):
        idori,iddesti=ids
        for i in self.flotte:
            if i.id== int(idori):
                for j in self.parent.Galaxie.listeSysSolaire:
                    if j.id== int(iddesti):
                        i.cible=j
                        print("GOT TARGET")
                        return


    def prochaineaction(self):
        for i in self.flotte:
            if i.cible:
                i.avancer()
            #else:
            #    i.cible=random.choice(self.parent.planetes)

    def prochaineaction2(self):
        for i in self.flotte:
            i.avancer()

# IA- nouvelle classe de joueur
class IA(Joueur):
    def __init__(self,parent,nom,planetemere,couleur):
        Joueur.__init__(self, parent, nom, planetemere, couleur)
        self.tempo=random.randrange(100)+20


# SQUELLETTE DE L'IA PASSIVE

#      ...ELLE CONSTRUIT DES BÂTIMENTS SUR SA PLANÈTE MÈRE
#       ...Pour éventuellement construire des cargos et
#       ...coloniser une nouvelle planète

    def prochaineaction(self):

        # si assez d'argent
        # construit un bâtiment sur la planète mère
        if self.flotte:
            for i in self.flotte:
                if i.cible:
                    i.avancer()
                else:
                    i.cible=random.choice(self.parent.Galaxie.listeSysSolaire)
        else:
            self.creervaisseau(0)

class Modele():
    def __init__(self,parent,joueurs):
        self.parent=parent
        self.largeur=800 #self.parent.vue.root.winfo_screenwidth()
        self.hauteur=600 #self.parent.vue.root.winfo_screenheight()
        self.joueurs={}
        self.ias=[]
        self.actionsafaire={}
        self.terrain=[]
        self.creerterrain()
        self.Galaxie = Galaxie(self)
        self.assignerplanetemere(joueurs, 2)

    def creerterrain(self):
        self.terrain=[]
        for i in range(10):
            ligne=[]
            for j in range(10):
                n=random.randrange(5)
                if n==0:
                    ligne.append(1)
                else:
                    ligne.append(0)
            self.terrain.append(ligne)

    def assignerplanetemere(self,joueurs,ias=0):
        np=len(joueurs)+ias
        planes=[]
        while np:
            #s=random.choice(self.Galaxie.listeSysSolaire)
            s=self.Galaxie.listeSysSolaire[0]  # TEST SYS_SOLAIRE FAIRE MEME CHOSE DANS VUE
            p=random.choice(s.listePlanete)
            if p not in planes:
                planes.append(p)
                #self.planetes.remove(p)
                np-=1
        couleurs=["red","blue","lightgreen","yellow",
                  "lightblue","pink","gold","purple"]
        for i in joueurs:
            self.joueurs[i]=Joueur(self,i,planes.pop(0),couleurs.pop(0))

        # IA- creation des ias - max 2
        couleursia=["orange","green"]
        for i in range(ias):
            self.ias.append(IA(self,"IA_"+str(i),planes.pop(0),couleursia.pop(0)))


    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for i in self.actionsafaire[cadre]:
                #print(i)
                self.joueurs[i[0]].actions[i[1]](i[2])
                """
                print("4- le modele distribue les actions au divers participants")
                print("4...- en executant l'action qui est identifie par i[1] le dico")
                print("4...- qui est dans l'attribut actions",i[0],i[1],i[2])
                print("NOTE: ici on applique immediatement cette action car elle consiste soit")
                print("NOTE... a changer la vitesse (accelere/arrete) soit l'angle de l'auto")
                print("NOTE... dans ce cas-ci faire la prochaine action (le prochain for en bas)")
                print("NOTE... c'est seulement changer la position de l'auto si sa vitesse est non-nul")
                """
            del self.actionsafaire[cadre]

        for i in self.joueurs:
            self.joueurs[i].prochaineaction()

        # IA- appelle prochaine action
        for i in self.ias:
            i.prochaineaction()

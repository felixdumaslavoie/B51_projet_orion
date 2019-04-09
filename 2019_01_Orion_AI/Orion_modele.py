 # -*- coding: utf-8 -*-
import os,os.path
import random
from Id import Id
from helper import Helper as hlp

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
        self.nbSysSolaire=200
        self.listeSysSolaire=[]

        for i in range(self.parent.largeur-2):
            self.listeX.append(i)

        for i in range(self.parent.hauteur-2):
            self.listeY.append(i)

        for i in range(self.nbSysSolaire):
            #x=random.randrange(self.parent.largeur-(2*self.bordure))+self.bordure
            x=random.choice(self.listeX)
            self.listeX.remove(x)
            #===================================================================
            # if x-2 in self.listeX:
            #     self.listeX.remove(x-2)
            #===================================================================
            if x-1 in self.listeX:
                self.listeX.remove(x-1)
            if x+1 in self.listeX:
                self.listeX.remove(x+1)
            #===================================================================
            # if x+2 in self.listeX:
            #     self.listeX.remove(x+2)
            #===================================================================

            #y=random.randrange(self.parent.hauteur-(2*self.bordure))+self.bordure
            y=random.choice(self.listeY)
            self.listeY.remove(y)
            #===================================================================
            # if y-2 in self.listeY:
            #     self.listeY.remove(y-2)
            #===================================================================
            if y-1 in self.listeY:
                self.listeY.remove(y-1)
            if y+1 in self.listeY:
                self.listeY.remove(y+1)
            #===================================================================
            # if y+2 in self.listeY:
            #     self.listeY.remove(y+2)
            #===================================================================
            
            #TODO: S'assurer que les coordonnées et noms générés sont uniques.
            nom = self.listeNomEtoile.pop(random.randrange(len(self.listeNomEtoile)-1))
            s = SystemeSolaire(self,x,y,nom)
            self.listeSysSolaire.append(s)
            print("Étoile " + nom + " créée " + str(x) + " " + str(y))
			
class SystemeSolaire():
    def __init__(self,parent,x,y,nom):
        self.bordure = 0
        self.parent = parent
        self.nometoile = nom
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,7) #taille de l'étoile dans la vue de la galaxie
        self.nbdeplanete=random.randrange(3, 12)
        self.listePlanete = []
        for i in range(self.nbdeplanete):
            x=random.randrange(self.parent.parent.largeur-(2*self.bordure))+self.bordure
            y=random.randrange(self.parent.parent.hauteur-(2*self.bordure))+self.bordure
            p = Planete(self,x,y)
            self.listePlanete.append(p)

class Planete():
    def __init__(self,parent,x,y):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,6)
        self.charbon=random.randrange(6)
        self.zinc=random.randrange(5)
        self.deuterium=random.randrange(10)
        self.fertile=random.randrange(1)
        self.listeStructure=[]*self.taille ## Chaque planète à une liste de bâtiments avec l'emplacement de chaque bâtiment
        self.ressource=[self.charbon,self.zinc,self.deuterium]
        self.viePlanete1=self.viePlanete()

    def viePlanete(self):
        if not self.listeStructure:
            self.viePlanete1=0
        else:
            for i in listeStructure[i]:
                self.viePlanete1+=self.listeStructure[i].vie
        return self.viePlanete1


    def estFertile(self):
        return self.fertile

    def creerStructure(self,x,y,nomStructure):
        t=Structure(self,x,y,nomStructure)

class Structure():
    def __init__(self,nom,x,y,nomStructure):
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.nomStructure=nomStructure

        if nomStructure=="Usine_Civile":
            self.vie=100
            self.cout=150
            self.maintenance=1
            self.extraction=0
        if nomStructure=="Usine_Militaire":
            self.vie=200
            self.cout=225
            self.maintenance=2
            self.extraction=0
        if nomStructure=="Raffinerie_Diamant":
            self.vie=80
            self.cout=350
            self.maintenance=6
            self.extraction=2
        if nomStructure=="Raffinerie_Charbon":
            self.vie=50
            self.cout=150
            self.maintenance=2
            self.extraction=3
        if nomStructure=="Raffinerie_Isotope":
            self.vie=175
            self.cout=250
            self.maintenance=3
            self.extraction=2
        if nomStructure=="Ferme":
            self.vie=75
            self.cout=50
            self.maintenance=1
            self.production=2

        

    def extractionStructure(self):
        for i in Planete.listeStructure[i]:
            if self.ressource[i]>0:
                if ressource[i]<self.extraction:
                    self.extraction==self.ressource[i]
                self.ressource[i]-=self.extraction

    def maintenanceStructure(self):
        for i in Planete.listeStructure[i]:
            self.credit-=self.maintenance

   




class Vaisseau():
    def __init__(self,nom,x,y):
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.cargo=0
        self.energie=100
        self.vitesse=2
        self.cible=None

    def avancer(self):
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            ang=hlp.calcAngle(self.x,self.y,x,y)
            x1,y1=hlp.getAngledPoint(ang,self.vitesse,self.x,self.y)
            self.x,self.y=x1,y1 #int(x1),int(y1)
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                print("RESSOURCES...",self.cible.id,self.cible.ressource,self.cible.proprietaire,self.cible.viePlanete1)
                self.cible.proprietaire=self.proprietaire
                #tempo=input("Continuersvp")
                self.cible=None
                #print("Change cible")
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

    def creervaisseau(self,params):
        #planete,cible,type=params
        #is type=="explorer":
        v=Vaisseau(self.nom,self.planetemere.x+10,self.planetemere.y)
        print("Vaisseau",v.id)
        self.flotte.append(v)

    def ciblerflotte(self,ids):
        idori,iddesti=ids
        for i in self.flotte:
            if i.id== int(idori):
                for j in self.parent.planetes:
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

    def prochaineaction(self):
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
            s=random.choice(self.Galaxie.listeSysSolaire)
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

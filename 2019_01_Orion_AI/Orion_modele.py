 # -*- coding: utf-8 -*-
import os,os.path
import random
import math
from Id import Id
from helper import Helper as hlp
from couleurs import *
import math
from numpy.distutils.fcompiler import none

class Galaxie():
    def __init__(self,parent):
        self.bordure = 0
        self.listeX = []
        self.listeY = []
        self.parent = parent

        dir_path = os.path.dirname(os.path.realpath(__file__))

        self.txtNomEtoile = open(dir_path + "/nom_etoiles.txt","r")
        self.txtNomPlanete = open(dir_path + "/nom_planetes.txt","r")
        self.listeNomEtoile = self.txtNomEtoile.readlines()
        self.listeNomPlanete = self.txtNomPlanete.readlines()
        self.nbSysSolaire=2
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

            nom = self.listeNomEtoile.pop(random.randrange(len(self.listeNomEtoile)-1))
            s = SystemeSolaire(self,x,y,nom)
            self.listeSysSolaire.append(s)

class SystemeSolaire():
    def __init__(self,parent,x,y,nom):
        self.id=Id.prochainid()
        self.bordure = 0
        self.parent = parent
        self.nometoile = nom
        self.proprietaire="inconnu"
        self.x=x
        self.y=y
        self.taille=random.randrange(4,7)
        self.nbdeplanete=random.randrange(5, 12)
        self.listePlanete = []
        self.couleur = "grey80"
        for i in range(self.nbdeplanete):
            self.nom = self.parent.listeNomPlanete[random.randrange(len(self.parent.listeNomPlanete)-1)]
            x=random.randrange(self.parent.parent.largeur-(2*self.bordure))+self.bordure
            y=random.randrange(self.parent.parent.hauteur-(2*self.bordure))+self.bordure
            p = Planete(self,x,y, self.nom)
            self.listePlanete.append(p)

class Planete():
    couleurs={""}
    pointDepart={200,100}

    def __init__(self,parent,x,y, nom):
        self.id=Id.prochainid()
        self.proprietaire="inconnu"
        self.parent=parent
        self.nom=nom
        self.x=x
        self.y=y
        self.taille=random.randrange(4,12)
        self.charbon=random.randrange(6000)
        self.zinc=random.randrange(3000)
        self.diamant=random.randrange(100)
        self.fertile=random.randrange(1)
        self.listeStructure=[]
        self.emplacementsDispo=[]*self.taille
        self.tailleAffichage=50*self.taille


        largeur=self.parent.parent.parent.largeur/2
        hauteur=self.parent.parent.parent.hauteur/2

        t1=self.tailleAffichage/2

        x1,y1= hlp.getAngledPoint(math.radians(225),t1,largeur,hauteur)
        x2,y2= hlp.getAngledPoint(math.radians(45),t1,largeur,hauteur)

        nPos=self.taille
        paires=[]
        self.distanceMinEmplacements=50

        while nPos:
            xR1 = random.randrange(int(x1),int(x2))
            yR1 = random.randrange(int(y1),int(y2))
            if [xR1,yR1] not in paires:
                dist=1
                for i in paires:
                    d=hlp.calcDistance(xR1,yR1, i[0],i[1])

                    if d < self.distanceMinEmplacements:
                        dist=0
                if dist:
                    paires.append([xR1,yR1])
                    nPos-=1

        self.emplacementsDispo=paires

        self.ressource=[self.charbon,self.zinc,self.diamant]
        self.viePlanete1=self.viePlanete()
        self.couleur=random.choice(COULEURS)


    def viePlanete(self):
        if not self.listeStructure:
            self.viePlanete1=0
        else:
            for i in listeStructure[i]:
                self.viePlanete1+=self.listeStructure[i].vie
        return self.viePlanete1

    def ajouterBatiment(self,x,y,nomBatiment):
        structure = None
        for i in self.emplacementsDispo:
            if x == i[0] and y == i[1]:
                structure = EmplacementsSurPlanete(i[0],i[1],nomBatiment)
                self.listeStructure.append(structure)
                self.emplacementsDispo.remove(i)
                break


class EmplacementsSurPlanete():
    def __init__(self,x,y,structure):
        self.x = x
        self.y = y
        self.structure=str(structure)
        self.couleur ="grey"
        self.nomStructure=structure
        if self.structure=="Usine Civile":
            self.couleur="tan1"
        elif self.structure=="Usine Militaire":
            self.couleur="blue"
        elif self.structure=="Raffinerie (Diamant)":
            self.couleur="cyan"
        elif self.structure=="Raffinerie (Charbon)":
            self.couleur="gray25"
        elif self.structure=="Raffinerie (Isotope)":
            self.couleur="RoyalBlue1"
        elif self.structure=="Ferme":
            self.couleur="brown4"
        elif self.structure=="Capitale":
            self.couleur="yellow"


class Structure():
    #nom structure, vie, cout, maintenance, extraction
    Usine_Civile=["Usine_Civile",100,150,1,0]
    Usine_Militaire=["Usine_Militaire",200,225,2,0]
    Raffinerie_Diamant=["Raffinerie_Diamant",80,350,6,24]
    Raffinerie_Charbon=["Raffinerie_Charbon",50,150,2,6]
    Raffinerie_Isotope=["Raffinerie_Isotope",175,250,3,18]
    Ferme=["Ferme",75,50,1,2]
    Capitale=["Capitale",300,5000,10,100]


    def __init__(self,joueur,nomstruct,planete,x,y):
        self.nomStructure=nomstruct
        self.joueur=joueur
        self.x=x
        self.y=y
        self.planete = planete

    def maintenanceStructure(self):
        for i in self.parent.listeStructure[i]:
            self.credit-=self.maintenance

class UsineCivile(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Usine_Civile[0]
        self.cout=Structure.Usine_Civile[2]
        self.maintenance=Structure.Usine_Civile[3]
        self.production=Structure.Usine_Civile[4]
        self.couleur = "tan1"

class UsineMilitaire(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Usine_Militaire[0]
        self.cout=Structure.Usine_Militaire[2]
        self.maintenance=Structure.Usine_Militaire[3]
        self.production=Structure.Usine_Militaire[4]
        self.couleur = "blue"

class RaffinerieDiamant(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Raffinerie_Diamant[0]
        self.cout=Structure.Raffinerie_Diamant[2]
        self.maintenance=Structure.Raffinerie_Diamant[3]
        self.production=Structure.Raffinerie_Diamant[4]
        self.couleur = "cyan"

class RaffinerieCharbon(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Raffinerie_Charbon[0]
        self.cout=Structure.Raffinerie_Charbon[2]
        self.maintenance=Structure.Raffinerie_Charbon[3]
        self.production=Structure.Raffinerie_Charbon[4]
        self.couleur = "gray25"

class RaffinerieIsotope(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Raffinerie_Isotope[0]
        self.cout=Structure.Raffinerie_Isotope[2]
        self.maintenance=Structure.Raffinerie_Isotope[3]
        self.production=Structure.Raffinerie_Isotope[4]
        self.couleur = "RoyalBlue1"

class Ferme(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Ferme[0]
        self.cout=Structure.Ferme[2]
        self.maintenance=Structure.Ferme[3]
        self.production=Structure.Ferme[4]
        self.couleur = "brown4"

class Capitale(Structure):
    def __init__(self,joueur,idplanete,nomstruct,x,y):
        super().__init__(joueur,idplanete,nomstruct,x,y)
        self.nomStructure=Structure.Capitale[0]
        self.cout=Structure.Capitale[2]
        self.maintenance=Structure.Capitale[3]
        self.production=Structure.Capitale[4]
        self.couleur = "yellow"




class Vaisseau():
    def __init__(self,parent,nom,x,y,solaireMere, nomVaisseau):
        self.parent=parent
        self.id=Id.prochainid()
        self.proprietaire=nom
        self.x=x
        self.y=y
        self.solaire=solaireMere
        self.espaceCourant = solaireMere
        self.cible=None
        self.vaisseauCible = None
        self.nomVaisseau=nomVaisseau
        self.projectile=[]
        self.cargo=0
        self.energie=0
        self.vitesse=0
        self.range=0


    def avancer(self):
        if self.cible:
            x=self.cible.x
            y=self.cible.y
            ang=hlp.calcAngle(self.x,self.y,x,y)
            x1,y1=hlp.getAngledPoint(ang,self.vitesse,self.x,self.y)
            self.x,self.y=x1,y1
            if hlp.calcDistance(self.x,self.y,x,y) <=self.vitesse:
                if type(self.cible).__name__=="Planete":
                    if len(self.cible.listeStructure)==0:
                        self.cible.proprietaire=self.proprietaire
                        self.parent.parent.parent.reclamerplanete(self.cible.id,self.proprietaire)
                self.cible=None

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

class VaisseauCanon(Vaisseau):
    def __init__(self,parent,nom,x,y,solaireMere, nomVaisseau="Vaisseau Canon"):
        super().__init__(parent,nom,x,y,solaireMere, nomVaisseau)
        self.cargo=0
        self.energie=400
        self.vitesse=5
        self.range=200
        self.cout=100

class VaisseauEclaireur(Vaisseau):
    def __init__(self,parent,nom,x,y,solaireMere, nomVaisseau="Vaisseau Eclaireur"):
        super().__init__(parent,nom,x,y,solaireMere, nomVaisseau)
        self.cargo=0
        self.energie=400
        self.vitesse=10
        self.range=200
        self.cout=300

class VaisseauTank(Vaisseau):
    def __init__(self,parent,nom,x,y,solaireMere, nomVaisseau="Vaisseau Tank"):
        super().__init__(parent,nom,x,y,solaireMere, nomVaisseau)
        self.cargo=0
        self.energie=400
        self.vitesse=1
        self.range=400
        self.cout=300

class VaisseauLaser(Vaisseau):
    def __init__(self,parent,nom,x,y,solaireMere, nomVaisseau="Vaisseau Laser"):
        super().__init__(parent,nom,x,y,solaireMere, nomVaisseau)
        self.cargo=0
        self.energie=400
        self.vitesse=1
        self.range=400
        self.cout=200

class VaisseauSniper(Vaisseau):
    def __init__(self,parent,nom,x,y,solaireMere, nomVaisseau="Vaisseau Sniper"):
        super().__init__(parent,nom,x,y,solaireMere, nomVaisseau)
        self.cargo=0
        self.energie=400
        self.vitesse=1
        self.range=400
        self.cout=200

class Joueur():
    def __init__(self,parent,nom,planetemere,couleur):
        self.id=Id.prochainid()
        self.parent=parent
        self.nom=nom
        self.planetemere=planetemere
        self.planetemere.proprietaire=self.nom
        self.couleur=couleur
        self.planetemere.couleur = couleur
        self.flotteSystemeSolaire=[]
        self.flotteGalaxie=[]
        self.planeteVisiter=[planetemere]
        self.systemeVisiter=[]
        self.planetescontrolees=[planetemere]
        self.bufferSelection = []
        self.listeStructure = []
        self.profits = 0
        self.actions={"creervaisseau":self.creervaisseau,
                      "ciblerflotte":self.ciblerflotte,
                      "creerStructure":self.creerStructure,
                      "envoyermessage":self.envoyermessage,
                      "cibleretoile":self.cibleretoile,
                      "changervuevaisseau":self.changerVueVaisseau,
                      "avancementTechno":self.avancementTechno,
                      "reclamerplanete":self.reclamerplanete}

        self.structures={"Usine Civile":UsineCivile,
                         "Usine Militaire":UsineMilitaire,
                         "Raffinerie (Diamant)":RaffinerieDiamant,
                         "Raffinerie (Charbon)":RaffinerieCharbon,
                         "Raffinerie (Isotope)":RaffinerieIsotope,
                         "Ferme":Ferme,
                         "Capitale":Capitale}

        self.vaisseaux={"Vaisseau Canon":VaisseauCanon,
                         "Vaisseau Eclaireur":VaisseauEclaireur,
                         "Vaisseau Tank":VaisseauTank,
                         "Vaisseau Laser":VaisseauLaser,
                         "Vaisseau Sniper":VaisseauSniper}

        self.cooldownRessource = 100

        self.credit=6000
        self.nourriture=1000
        self.deuterium=5
        self.timer=0
        self.messages=[]
        self.maintenance=0

    def changerVueVaisseau(self,info):
        idvais,idEspace,idSoleil=info
        for i in self.flotteSystemeSolaire:
            if i.id==int(idvais):
                self.vais=i

        if self.vais.espaceCourant is not None:
            self.vais.espaceCourant=None
            self.vais.x=self.vais.solaire.x
            self.vais.y=self.vais.solaire.y
            return
        elif (self.vais.espaceCourant==None):
            self.vais.espaceCourant=self.vais.solaire
            self.vais.x=100
            self.vais.y=100
            return


    def envoyermessage(self, params):
        envoyeur, recipiendaire, msg = params
        self.messages.append([envoyeur,recipiendaire,msg])


    def setbuffer(self,identificateur):
        for i in self.parent.Galaxie.listeSysSolaire:
            if int(i.id) == int(identificateur):
                self.bufferSelection.insert(0, i)
                return
            for j in i.listePlanete:
                if int(j.id) == int(identificateur):
                    self.bufferSelection.insert(0, j)
                    return

    def creervaisseau(self,params):
        nomvais=params
        vaisseau=self.vaisseaux[nomvais](self,self.nom,self.planetemere.x+10,self.planetemere.y,self.planetemere.parent)
        self.flotteSystemeSolaire.append(vaisseau)

    def creerStructure(self,params):
        nomjoueur,nomstruct,idplanete,x,y=params
        planete = None


        for i in (self.parent.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idplanete):
                    planete=j

        structure=self.structures[nomstruct](nomjoueur,nomstruct,planete,x,y)
        self.listeStructure.append(structure)
        planete.listeStructure.append(structure)

        planete.ajouterBatiment(x,y,nomstruct)
        if self.parent.parent.vue.vues:
            self.parent.parent.vue.vues["Planete"].afficheStructure(idplanete)

        if self.credit>=structure.cout:
            self.credit-=structure.cout

            self.listeStructure.append(structure)
            planete.listeStructure.append(structure)

            planete.ajouterBatiment(x,y,nomstruct)
            if self.parent.parent.vue.vues:
                self.parent.parent.vue.vues["Planete"].afficheStructure(idplanete)

        else:
            print("Vous n'avez pas assez de crédits pour construire cette structure")


    def updaterRessources(self):

        self.timer+=1
        self.profits = 0

        coutNourriture = 0
        coutCredit=0
        coutDeuterium = 0

        if self.timer >= self.cooldownRessource:

            for i in self.listeStructure:
                self.maintenance+=i.maintenance

            for i in self.listeStructure:
                typeRess = i.nomStructure[11:14]
                if typeRess == "Dia":
                    if i.planete.diamant >= 1:
                        self.profits += i.production
                        i.planete.diamant-=1
                if typeRess == "Cha":
                    if i.planete.charbon >= 3:
                        self.profits+= i.production
                        i.planete.charbon-=3
                if  typeRess == "Iso":
                    if i.planete.zinc >= 2:
                        self.profits+= i.production
                        i.planete.zinc-=2

                typeStruct = i.nomStructure[0:10]
                if typeStruct == "Raffinerie":
                    self.profits += i.production

            self.credit+=self.profits
            self.credit-=coutCredit
            self.timer = 0

    def ciblerflotte(self,ids):
        idori,iddesti=ids
        for i in self.flotteSystemeSolaire:
            if i.id== int(idori):
                for j in i.solaire.listePlanete:
                    if j.id== int(iddesti):
                        i.cible=j
                        return

    def cibleretoile(self,ids):
        idori,iddesti=ids
        for i in self.flotteSystemeSolaire:
            if i.id== int(idori):
                for j in self.parent.Galaxie.listeSysSolaire:
                    if j.id== int(float(iddesti)):
                        i.cible=j
                        i.solaire=j
                        return

    def prochaineaction(self):
        for i in self.flotteSystemeSolaire:
            if i.cible:
                i.avancer()

    def prochaineaction2(self):
        for i in self.flotteSystemeSolaire:
            i.avancer()

    def avancementTechno(self,nomAvancement):
        self.avanc = nomAvancement[0]
        if self.avanc == "Bonus production":
            self.cooldownRessource = 95
            self.parent.parent.vue.disableBtnAvac1()
        elif self.avanc == "Bonus production x 2":
            self.cooldownRessource = 85
            self.parent.parent.vue.disableBtnAvac2()
        elif self.avanc == "Bonus production x 4":
            self.parent.parent.vue.disableBtnAvac4()
            self.cooldownRessource = 55
        elif self.avanc == "Couts Reduit":
            self.parent.parent.vue.disableBtnAvac3()
        elif self.avanc == "Couts Reduit x 2":
            self.parent.parent.vue.disableBtnAvac5()
        elif self.avanc == "Vaisseau Canon":
            pass
        elif self.avanc == "Vaisseau Eclaireur":
            pass
        elif self.avanc == "Vaisseau Tank":
            pass
        elif self.avanc == "Vaisseau Laser":
            pass
        elif self.avanc == "Vaisseau Sniper":
            pass


    def reclamerplanete(self,idplanete,proprietaire):
        self.vue.vues["Solaire"].changerProprietaire(idplanete,coul)

class IA(Joueur):
    def __init__(self,parent,nom,planetemere,couleur):
        Joueur.__init__(self, parent, nom, planetemere, couleur)
        self.couleur = couleur
        self.compteurChoix = 0
        self.compteurChangementVue = 0
        self.tempo=random.randrange(100)+20


    def prochaineaction(self):

        if self.couleur == "orange":
            self.compteurChoix +=1

            if self.compteurChoix == 750:
                self.compteurChoix = 0
                choice = random.randrange(0,100)
                self.compteurChangementVue += 1
                self.prendreChoix(choice)

            if self.compteurChangementVue == 1: # changement de vue d'un vaisseau
                self.compteurChangementVue = 0
                if self.flotteSystemeSolaire:
                    i = random.choice(self.flotteSystemeSolaire)
                    self.changerVueVaisseau([i.id,i.espaceCourant,i.solaire.id])
                    i.cible = None

            if self.flotteSystemeSolaire: # changement de cible
                for i in self.flotteSystemeSolaire:
                    if i.cible == None:
                        if i.espaceCourant:
                            i.cible=random.choice(i.solaire.listePlanete)
                        if i.espaceCourant == None:
                            i.cible=random.choice(i.solaire.parent.listeSysSolaire)

        if self.couleur == "green":
            self.compteurChoix +=1

            if self.compteurChoix == 750:
                self.compteurChoix = 0
                choice = random.randrange(0,100)
                self.compteurChangementVue += 1
                self.prendreChoix(choice)

            if self.compteurChangementVue == 3:
                self.compteurChangementVue = 0
                if self.flotteSystemeSolaire:
                    i = random.choice(self.flotteSystemeSolaire)
                    self.changerVueVaisseau([i.id,i.espaceCourant,i.solaire.id])
                    i.cible = None

            if self.flotteSystemeSolaire:
                for i in self.flotteSystemeSolaire:
                    if i.cible == None:
                        if i.espaceCourant:
                            i.cible=random.choice(i.solaire.listePlanete)
                        if i.espaceCourant == None:
                            i.cible=random.choice(i.solaire.parent.listeSysSolaire)

 ################################################################################################################
#################################################################################################################
#################################################################################################################

        if self.flotteSystemeSolaire:
            for i in self.flotteSystemeSolaire:
                if i.cible:
                    i.avancer()


    def prendreChoix(self,choixNumber):
        if choixNumber <= 50:
            self.creervaisseau("Vaisseau Canon") # crée un vaisseau
        elif choixNumber == 99:
            num = random.randrange(5,15)
            for x in range(0,num) :
                self.creervaisseau("Vaisseau Eclaireur")
        elif choixNumber >= 90 & choixNumber <=98:
            self.creervaisseau("Vaisseau Tank")
            self.creervaisseau("Vaisseau Tank")
        elif choixNumber >= 75 & choixNumber < 90:
            self.creervaisseau("Vaisseau Laser")
        elif choixNumber > 50 & choixNumber < 75:
            self.creervaisseau("Vaisseau Sniper")


class Modele():
    def __init__(self,parent,joueurs):
        self.parent=parent
        self.largeur=800
        self.hauteur=600
        self.joueurs={}
        self.listeObjCliquable = []
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
                np-=1
        couleurs=["red","blue","lightgreen","yellow",
                  "lightblue","pink","gold","purple"]
        for i in joueurs:
            planes[0].proprietaire = i

            self.joueurs[i]=Joueur(self,i,planes.pop(0),couleurs.pop(0))
            choixEmplacement = random.choice(self.joueurs[i].planetemere.emplacementsDispo)
            self.joueurs[i].planetemere.emplacementsDispo.remove(choixEmplacement)
            self.joueurs[i].creerStructure([self.joueurs[i],"Capitale",self.joueurs[i].planetemere.id,choixEmplacement[0],choixEmplacement[1]])

        # IA- creation des ias - max 2
        couleursia=["orange","green"]
        for i in range(ias):
            self.ias.append(IA(self,"IA_"+str(i),planes.pop(0),couleursia.pop(0)))


    def prochaineaction(self,cadre):
        if cadre in self.actionsafaire:
            for i in self.actionsafaire[cadre]:
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
            self.joueurs[i].updaterRessources()
            self.joueurs[i].prochaineaction()

        # IA- appelle prochaine action
        for i in self.ias:
            i.prochaineaction()


batiments={"Usine_Civile":["Usine_Civile",100,150,1,0,UsineCivile],
           "Usine_Militaire":["Usine_Militaire",200,225,2,0,UsineMilitaire],
           "Raffinerie_Diamant":["Raffinerie_Diamant",80,350,6,2,RaffinerieDiamant],
           "Raffinerie_Charbon":["Raffinerie_Charbon",50,150,2,3,RaffinerieCharbon],
           "Raffinerie_Isotope":["Raffinerie_Isotope",175,250,3,2,RaffinerieIsotope],
           "Ferme":["Ferme",75,50,1,2,Ferme],
           "Capitale":["Capitale",300,5000,10,100,Capitale]}

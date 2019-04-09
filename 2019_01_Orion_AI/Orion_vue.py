# -*- coding: utf-8 -*-
from tkinter import *

import random
import os,os.path

class Vue():
    def __init__(self,parent,ip,nom):
        self.parent=parent
        self.root=Tk()
        self.largeur=640
        self.hauteur=480
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.terrain=[]
        self.cadreactif=None
        self.maselection=None
        self.root.title(os.path.basename(sys.argv[0]))
        self.modele=None
        self.nom=""
        self.cadreapp=Frame(self.root,width=800,height=600)
        self.cadreapp.grid(row=0, column=0)
        self.creercadresplash(ip,nom)
        self.creercadrelobby()
        self.changecadre(self.cadresplash)

    def fermerfenetre(self):
        self.parent.fermefenetre()

    def changecadre(self,cadre):
        if self.cadreactif:
            self.cadreactif.grid_forget()
        self.cadreactif=cadre
        self.cadreactif.grid(row=1, column=0)
    def changevue(self,vue):
        if self.vueactif:
            self.vueactif.grid_forget()
        self.vueactif=cadre
        self.vueactif.grid(row=1, column=0)


    def creercadresplash(self,ip,nom):
        self.cadresplash=Frame(self.cadreapp)
        self.canevassplash=Canvas(self.cadresplash,width=640,height=480,bg="gray38")
        self.canevassplash.grid(row=0, column=0)
        self.nomsplash=Entry(bg="pink")
        self.nomsplash.insert(0, nom)
        self.ipsplash=Entry(bg="pink")
        self.ipsplash.insert(0, ip)
        labip=Label(text=ip,bg="red",borderwidth=0,relief=RIDGE)
        btncreerpartie=Button(text="Creer partie",bg="pink",command=self.creerpartie)
        btnconnecterpartie=Button(text="Connecter partie",bg="pink",command=self.connecterpartie)
        self.canevassplash.create_window(200,200,window=self.nomsplash,width=100,height=30)
        self.canevassplash.create_window(200,250,window=self.ipsplash,width=100,height=30)
        self.canevassplash.create_window(200,300,window=labip,width=100,height=30)
        self.canevassplash.create_window(200,350,window=btncreerpartie,width=100,height=30)
        self.canevassplash.create_window(200,400,window=btnconnecterpartie,width=100,height=30)

    def creercadrelobby(self):
        self.cadrelobby=Frame(self.cadreapp)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="lightblue")
        self.canevaslobby.grid(row=0, column=0)
        self.listelobby=Listbox(bg="red",borderwidth=0,relief=FLAT)
        self.nbetoile=Entry(bg="pink")
        self.nbetoile.insert(0, 100)
        self.largeespace=Entry(bg="pink")
        self.largeespace.insert(0, 1000)
        self.hautespace=Entry(bg="pink")
        self.hautespace.insert(0, 800)
        btnlancerpartie=Button(text="Lancer partie",bg="pink",command=self.lancerpartie)
        self.canevaslobby.create_window(440,240,window=self.listelobby,width=200,height=400)
        self.canevaslobby.create_window(200,200,window=self.largeespace,width=100,height=30)
        self.canevaslobby.create_window(200,250,window=self.hautespace,width=100,height=30)
        self.canevaslobby.create_window(200,300,window=self.nbetoile,width=100,height=30)
        self.canevaslobby.create_window(200,400,window=btnlancerpartie,width=100,height=30)

    def connecterpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby)
            print("BOUCLEATTENTE de CONNECTER")
            self.parent.boucleattente()

    def creerpartie(self):
        nom=self.nomsplash.get()
        ip=self.ipsplash.get()
        if nom and ip:
            self.parent.creerpartie()
            self.parent.inscrirejoueur()
            self.changecadre(self.cadrelobby)
            print("BOUCLEATTENTE de CREER")
            self.parent.boucleattente()

    def lancerpartie(self):
        self.parent.lancerpartie()

    def affichelisteparticipants(self,lj):
        self.listelobby.delete(0,END)
        self.listelobby.insert(0,lj)

    def creercadreinfojoueur(self,cadre):
        pass


    def creeraffichercadrepartie(self,mod):
        self.nom=self.parent.monnom
        self.mod=mod
        self.cadrepartie=Frame(self.cadreapp)
        self.cadrejeu=Frame(self.cadrepartie)
        self.cadrejeu.grid(row=1, column=0)


        #G.grid(row=1, column=0)
        #S.grid(row=1, column=0)
        #P.grid(row=1, column=0)


        self.cadreinfojoueur=Frame(self.cadrepartie,height=100, width=800, bg="blue",padx = 200)
        self.cadreinfojoueur.grid(row=0, column=0, columnspan = 5)

        self.labcouleur=Label(self.cadreinfojoueur,text="couleur:",padx = 100)
        self.labcouleur.grid(row=0,column=0)
        self.idcouleur=Label(self.cadreinfojoueur, bg=mod.joueurs[self.nom].couleur )
        self.idcouleur.grid(row=0,column=1)
        self.btndiplomatie=Button(self.cadreinfojoueur,text="Diplomatie")
        self.btndiplomatie.grid(row=0,column=3)
        # une fois cadre Diplomatie cree  ajouter command=self.changercadre(self.canevasDiplomatie)
        self.labcouttotal=Label(self.cadreinfojoueur,text="cout total:")
        self.labcouttotal.grid(row=0,column=4, sticky="EW")
        # faut creer cout de maintenance total avant bg=mod.joueurs[self.nom].cout
        self.nbcouttotal=Label(self.cadreinfojoueur,text="-" )
        self.nbcouttotal.grid(row=0,column=5)
        self.btnarbretech=Button(self.cadreinfojoueur,text="Arbre Technologique")
        # une fois cadre Arbre Tech cree  ajouter command=self.changercadre(self.canevasArbreTech)
        self.btnarbretech.grid(row=0,column=6)

        self.labcredit=Label(self.cadreinfojoueur, text="credit:")
        self.labcredit.grid(row=1,column=0)
        # faut creer credits avant text=mod.joueurs[self.nom].credit
        self.nbcredit=Label(self.cadreinfojoueur, text="-")
        self.nbcredit.grid(row=1,column=1)
        self.labnourriture= Label(self.cadreinfojoueur, text="nourriture:")
        self.labnourriture.grid(row=1,column=2)
        # faut creer nourriture avant text=mod.joueurs[self.nom].nourriture
        self.nbnourriture=Label(self.cadreinfojoueur, text="-")
        self.nbnourriture.grid(row=1,column=3)
        self.labdeuterium= Label(self.cadreinfojoueur, text="deuterium:")
        self.labdeuterium.grid(row=1,column=4)
        # faut creer deuterium avant text=mod.joueurs[self.nom].deuterium
        self.nbdeuterium=Label(self.cadreinfojoueur, text="-")
        self.nbdeuterium.grid(row=1,column=5)
        self.labmoral= Label(self.cadreinfojoueur, text="moral:")
        self.labmoral.grid(row=1,column=6)
        # faut creer moral avant text=mod.joueurs[self.nom].moral
        self.nbmoral=Label(self.cadreinfojoueur, text="-")
        self.nbmoral.grid(row=1,column=7)

        #self.cadreinfojoueur.columnconfigure(0, weight=1)
        #self.cadreinfojoueur.columnconfigure(1, weight=1)
        #self.cadreinfojoueur.columnconfigure(2, weight=1)

         # cadre jeu = la vue actuel
        self.canevas=Canvas(self.cadrejeu,width=800,height=600,scrollregion=(0,0,mod.largeur,mod.hauteur),bg="grey11") #INUTILE

        #Canevas vue Galaxie / vue de base
        self.canevasGalaxie=Canvas(self.cadrejeu,width=800,height=600,scrollregion=(0,0,mod.largeur,mod.hauteur),bg="grey11")
        #self.canevasSolaire=Canvas(self.cadrejeu,width=800,height=600,scrollregion=(0,0,mod.largeur,mod.hauteur),bg="grey11")
        #self.canevasPlanete=Canvas(self.cadrejeu,width=800,height=600,scrollregion=(0,0,mod.largeur,mod.hauteur),bg="grey11")

        #Canevas vue Galaxie
        self.canevasGalaxie.grid(row=1, column=0)

        #Caneveas vue Solaire

        #self.canevasSolaire.grid(row=1, column=0)

        # Canevas vue Planete
        #self.canevasPlanete.grid(row=1, column=0)

        self.cadreoutils=Frame(self.cadrepartie,width=200,height=200,bg="darkgrey")
        self.cadreoutils.grid(row=1, column=1)

        self.cadreinfo=Frame(self.cadreoutils,width=200,height=200,bg="darkgrey")
        self.cadreinfo.grid(row=0, column=1)
        self.cadreinfogen=Frame(self.cadreinfo,width=200,height=200,bg="grey50")
        self.cadreinfogen.grid(row=0, column=1)

        self.labid=Label(self.cadreinfogen,text=self.nom,fg=mod.joueurs[self.nom].couleur)
        self.labid.bind("<Button>",self.afficherplanemetemereGalaxie)
        self.labid.grid(row=0, column=1)

        self.cadreinfochoix=Frame(self.cadreinfo,height=200,width=200,bg="grey30")
        self.cadreinfochoix.grid(row=0, column=1)

        self.btncreervaisseau=Button(self.cadreinfo,text="Vaisseau",command=self.creervaisseau)
        self.lbselectecible=Label(self.cadreinfo,text="Choisir cible",bg="darkgrey")

        #modif arbitraire

        self.cadreminimap=Frame(self.cadreoutils,height=200,width=200,bg="black")
        self.canevasMini=Canvas(self.cadreminimap,width=200,height=200,bg="pink")
        self.canevasMini.bind("<Button>",self.moveCanevas)
        self.canevasMini.grid(row=0, column=1)
        self.cadreminimap.grid(row=2, column=1)

        self.cadrechangervues=Frame(self.cadreoutils,height=100,width=200, bg="SeaGreen1")
        self.cadrechangervues.grid(row=3,column=1)



        self.afficherdecorGalaxie(mod)
        #self.afficherdecorSolaire(mod)
        #self.afficherdecorPlanete(mod)

        self.changecadre(self.cadrepartie)

    def moveCanevas(self,evt):

        x=evt.x
        y=evt.y
        px=self.mod.largeur/x/100
        py=self.mod.hauteur/y/100
        self.canevasGalaxie.xview(MOVETO,px)
        self.canevasGalaxie.yview(MOVETO,py)
        print("SCROLL",px,py)

    def afficherdecorGalaxie(self,mod):

        self.mod=mod

        for i in range(len(mod.Galaxie.listeSysSolaire)):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasGalaxie.create_oval(x,y,x+1,y+1,fill="white",tags=("fond",))

        for i in mod.Galaxie.listeSysSolaire:
            t=i.taille
            self.canevasGalaxie.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill="grey80",
                                     tags=(i.proprietaire,"planete",str(i.id)))
        for i in mod.joueurs.keys():
            for j in mod.joueurs[i].planetescontrolees:
                t=j.taille
                self.canevasGalaxie.create_oval(j.x-t,j.y-t,j.x+t,j.y+t,fill=mod.joueurs[i].couleur,
                                     tags=(j.proprietaire,"planete",str(j.id),"possession"))
        # dessine IAs

        for i in mod.ias:
            for j in i.planetescontrolees:
                t=j.taille
                self.canevasGalaxie.create_oval(j.x-t,j.y-t,j.x+t,j.y+t,fill=i.couleur,
                                     tags=(j.proprietaire,"planete",str(j.id),"possession"))

        self.afficherpartie(mod)

    def _create_circle(self, x, y, r):
        return self.canevasSolaire.create_oval(x-r, y-r, x+r, y+r,fill="yellow",tags=("soleil"))

    def afficherdecorSolaire(self,mod):

        self.mod=mod

        for i in range(len(mod.Galaxie.listeSysSolaire)):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasSolaire.create_oval(x,y,x+1,y+1,fill="white",tags=("fond"))


        self._create_circle(self.largeur/1.5,self.hauteur/1.5,75)



        self.afficherpartie(mod)

    def afficherdecorPlanete(self,mod):
        self.mod = mod

        for i in range(len(mod.planetes)*3):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasPlanete.create_oval(x,y,x+1,y+1,fill="white",tags=("fond",))

        # affichage de la planete selectionner
        x = 200
        y = 100
        r = 300
        self.canevasPlanete.create_oval(x, y, x+r, y+r,fill="green2",tags=("planeteMere"))




        self.afficherpartie(mod)

    def afficherplanemetemereGalaxie(self,evt):
        j=self.mod.joueurs[self.nom]
        couleur=j.couleur
        x=j.planetemere.x
        y=j.planetemere.y
        t=10
        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                 tags=("planetemere","marqueur"))
    def creervaisseau(self):
        print("Creer vaisseau")
        self.parent.creervaisseau()
        self.maselection=None
        self.canevasGalaxie.delete("marqueur")
        self.btncreervaisseau.grid_forget()

    def afficherpartie(self,mod):
        self.canevasGalaxie.delete("artefact")

        if self.maselection!=None:
            joueur=mod.joueurs[self.maselection[0]]
            if self.maselection[1]=="planete":
                for i in joueur.planetescontrolees:
                    if i.id == int(self.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevasGalaxie.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.nom].couleur,
                                                 tags=("select","marqueur"))
            elif self.maselection[1]=="flotte":
                for i in joueur.flotte:
                    if i.id == int(self.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevasGalaxie.create_rectangle(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.nom].couleur,
                                                 tags=("select","marqueur"))
        #else:
        #    self.canevas.delete("marqueur")


        for i in mod.joueurs.keys():
            i=mod.joueurs[i]
            for j in i.flotte:
                self.canevasGalaxie.create_rectangle(j.x-3,j.y-3,j.x+3,j.y+3,fill=i.couleur,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact"))

                #self.canevas.create_rectangle(j.x,j.y,image=self.imgs["vaiss"],
                #                     tags=(j.proprietaire,"flotte",str(j.id),"artefact"))


        for i in mod.ias:
            for j in i.flotte:
                self.canevasGalaxie.create_rectangle(j.x-3,j.y-3,j.x+3,j.y+3,fill=i.couleur,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact"))

    def cliquecosmos(self,evt):
        self.btncreervaisseau.grid_forget()
        t=self.canevasGalaxie.gettags(CURRENT)
        if t and t[0]==self.nom:
            #self.maselection=self.canevas.find_withtag(CURRENT)#[0]
            self.maselection=[self.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
            print(self.maselection)
            if t[1] == "planete":
                self.montreplaneteselection()
            elif t[1] == "flotte":
                self.montreflotteselection()
        elif "planete" in t and t[0]!=self.nom:
            if self.maselection:
                pass # attribuer cette planete a la cible de la flotte selectionne
                self.parent.ciblerflotte(self.maselection[2],t[2])
            print("Cette planete ne vous appartient pas - elle est a ",t[0])
            self.maselection=None
            self.lbselectecible.grid_forget()
            self.canevasGalaxie.delete("marqueur")
        else:
            print("Region inconnue")
            self.maselection=None
            self.lbselectecible.grid_forget()
            self.canevasGalaxie.delete("marqueur")

    def montreplaneteselection(self):
        self.btncreervaisseau.grid(row=1, column=1)
    def montreflotteselection(self):
        self.lbselectecible.grid(row=0, column=0)

    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)

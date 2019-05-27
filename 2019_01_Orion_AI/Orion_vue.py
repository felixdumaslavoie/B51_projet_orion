# -*- coding: utf-8 -*-
from tkinter import *
import random
import os,os.path
import time
import resizeImage
from PIL import Image, ImageTk
from helper import Helper as hlp



class Vue():
    def __init__(self,parent,ip,nom):
        self.parent=parent
        self.root=Tk()
        self.largeur=800
        self.hauteur=800
        self.root.protocol("WM_DELETE_WINDOW", self.fermerfenetre)
        self.terrain=[]
        self.vues=None
        self.cadreactif=None
        self.maselection=None
        self.root.title(os.path.basename(sys.argv[0]))
        self.modele=None
        self.nom=""
        self.cadreapp=Frame(self.root,width=1000,height=800)
        self.cadreapp.grid(row=1, column=0)
        self.creercadresplash(ip,nom)
        self.creercadrelobby()
        self.changecadre(self.cadresplash)
        self.cadreoutilsgeneral=Frame(self.root)
        self.labgeneral=Label(self.cadreoutilsgeneral)
        self.labgeneral.grid(row = 1, column =0)
        self.ip=ip
        self.vueactive=None
        self.vueEnFonction=0
        self.arbretechEcoState = 0
        self.arbretechMilitState = 0

        self.cadrepartie=Frame(self.cadreapp)
        self.cadrejeu=Canvas(self.cadrepartie,width=self.largeur,height=self.hauteur,scrollregion=(0,0,1000,1000))


        self.cadreoutils=Frame(self.cadrepartie,width=200,height=200,bg="darkgrey")
        self.cadreinfo=Frame(self.cadreoutils,width=200,height=200,bg="light cyan")
        self.cadreArbreTechno=Canvas(self.cadreoutils,width=350,height=200, bg = "green2")

        self.cadreBouton=Frame(self.cadreoutils,width=200,height=200,bg="medium spring green")

        self.couleurinfo="gray"
        self.couleurbouton="gray33"
        self.labfont="Helvetica",20,"bold"
        self.infofont="Helvetica",10,"bold"
        self.cadrejeu.grid(row=1, column=0, rowspan=2)
        self.mod=None

    def toggleBtnTechno(self,evt):
        if self.cadreArbreTechno.winfo_ismapped():
            self.cadreArbreTechno.grid_forget()
        else:
            self.cadreArbreTechno.grid(row=0, column =0)
            self.createElemTech()

    def changementdevue(self,evt):
        nom=evt.widget.cget("text")
        self.changevueactive(self.vues[nom])

    def changevueactive(self,vue):
        if self.vueactive:
            self.vueactive.cadrespatial.grid_forget()
            self.vueactive.cadreinfo.grid_forget()

        self.vueactive=vue
        self.vueactive.cadrespatial.grid()
        self.vueactive.cadreinfo.grid(row = 1, column =0 )

    def combinedactions(self):
        self.planete=self.mod.joueurs[self.nom].planetemere
        self.mod.joueurs[self.nom].bufferSysSolaire = self.planete.parent
        self.vues["Solaire"].afficherInfosSystemSolaire(self.mod,self.planete.parent.id)

        self.vues["Solaire"].afficherSystemeSolaire(self.mod,self.planete.parent.id)
        self.changevueactive(self.vues["Solaire"])

    def fermerfenetre(self):
        self.parent.fermefenetre()

    def changecadre(self,cadre):
        if self.cadreactif:
            self.cadreactif.grid_forget()
        self.cadreactif=cadre
        self.cadreactif.grid(row=1, column=0)



    def creercadresplash(self,ip,nom):
        self.cadresplash=Frame(self.cadreapp)
        self.canevassplash=Canvas(self.cadresplash,width=640,height=480,bg="midnight blue")
        self.canevassplash.grid(row=0, column=0)
        self.nomjeu=Label(self.cadresplash,text="ORION",bg="midnightblue", fg="lavender", font=("Helvetica", 40, "bold"))
        self.nomjoueur=Label(self.cadresplash, text="NOM DU JOUEUR", bg="midnightblue", fg="lavender", font=("Helvetica", 16,"bold"))
        self.adresseipserveur=Label(self.cadresplash, text="IP DU SERVEUR", bg="midnightblue", fg="lavender", font=("Helvetica", 16, "bold"))
        self.tonadresseip=Label(self.cadresplash, text="TON ADRESSE IP", bg="midnightblue", fg="lavender", font=("Helvetica", 16, "bold"))
        self.nomsplash=Entry(bg="pink")
        self.nomsplash.insert(0, nom)
        self.ipsplash=Entry(bg="pink")
        self.ipsplash.insert(0, ip)
        labip=Label(text=ip,bg="red",borderwidth=0,relief=RIDGE)
        btncreerpartie=Button(text="Créer partie",bg="pink",command=self.creerpartie, font=("Helvetica", 16,"bold"))
        btnconnecterpartie=Button(text="Connecter partie",bg="pink",command=self.connecterpartie, font=("Helvetica",16,"bold"))
        self.canevassplash.create_window(320,40, window=self.nomjeu, width=200, height=60)
        self.canevassplash.create_window(320,120,window=self.nomjoueur, width=200, height=30)
        self.canevassplash.create_window(320,160,window=self.nomsplash,width=200,height=30)
        self.canevassplash.create_window(320,200,window=self.adresseipserveur, width=200, height=30)
        self.canevassplash.create_window(320,240,window=self.ipsplash,width=200,height=30)
        self.canevassplash.create_window(320,280,window=self.tonadresseip, width=200, height=30)
        self.canevassplash.create_window(320,320,window=labip,width=200,height=30)
        self.canevassplash.create_window(320,370,window=btncreerpartie,width=200,height=45)
        self.canevassplash.create_window(320,425,window=btnconnecterpartie,width=200,height=45)

    def creercadrelobby(self):
        self.cadrelobby=Frame(self.cadreapp)
        self.canevaslobby=Canvas(self.cadrelobby,width=640,height=480,bg="DarkOrchid4")
        self.canevaslobby.grid(row=0, column=0)
        self.listelobby=Listbox(bg="goldenrod",borderwidth=0,relief=FLAT)
        self.nomlobby=Label(self.cadrelobby, text="LOBBY", bg="DarkOrchid4", fg="lavender", font=("Helvetica",40,"bold"))
        self.lbllargeurespace=Label(self.cadrelobby, text="LARGEUR ESPACE", bg="DarkOrchid4", fg="lavender", font=("Helvetica",16,"bold"))
        self.lblhauteurespace=Label(self.cadrelobby, text="HAUTEUR ESPACE", bg="DarkOrchid4", fg="lavender", font=("Helvetica",16,"bold"))
        self.lblnbetoile=Label(self.cadrelobby, text="NOMBRE ETOILE", bg="DarkOrchid4", fg="lavender", font=("Helvetica",16,"bold"))
        self.nbetoile=Entry(bg="pink")
        self.nbetoile.insert(0, 100)
        self.largeespace=Entry(bg="pink")
        self.largeespace.insert(0, 1000)
        self.hautespace=Entry(bg="pink")
        self.hautespace.insert(0, 800)
        btnlancerpartie=Button(text="Lancer partie",bg="pink",command=self.lancerpartie, font=("Helvetica",16,"bold"))
        self.canevaslobby.create_window(320,50, window=self.nomlobby, width=200, height=60)
        self.canevaslobby.create_window(160,180,window=self.lbllargeurespace,width=200,height=30)
        self.canevaslobby.create_window(160,220,window=self.largeespace,width=100,height=30)
        self.canevaslobby.create_window(160,260, window=self.lblhauteurespace, width=200, height=60)
        self.canevaslobby.create_window(160,300,window=self.hautespace,width=100,height=30)
        self.canevaslobby.create_window(480,180, window=self.lblnbetoile, width=200, height=30)
        self.canevaslobby.create_window(480,220,window=self.nbetoile,width=100,height=30)
        self.canevaslobby.create_window(480,300,window=btnlancerpartie,width=180,height=60)
        self.canevaslobby.create_window(320,420,window=self.listelobby,width=480,height=80)

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

    def creerCadreInfoJoueur(self,cadre,mod):
        self.cadre = cadre
        self.mod = mod

        self.labcouleur=Label(self.cadre,text="Couleur:",bg=self.couleurinfo, font=self.infofont)
        self.idcouleur=Label(self.cadre, bg=self.mod.joueurs[self.nom].couleur )

        self.labcouttotal=Label(self.cadre,text="Cout Total:",bg=self.couleurinfo, font=self.infofont)
        self.nbcouttotal=Label(self.cadre,text=self.mod.joueurs[self.nom].maintenance ,bg=self.couleurinfo, font=self.infofont)

        self.btnarbretech=Button(self.cadre,text="Tech & Vaisseaux",bg=self.couleurinfo, font=("Helvetica",12,"bold"))
        self.btnarbretech.bind("<Button-1>",self.toggleBtnTechno)

        self.labcredit=Label(self.cadre, text="Credit:",bg=self.couleurinfo, font=self.infofont)
        self.nbcredit=Label(self.cadre, text=self.mod.joueurs[self.nom].credit,bg=self.couleurinfo, font=self.infofont)

        self.labnourriture= Label(self.cadre, text="Nourriture:",bg=self.couleurinfo, font=self.infofont)
        self.nbnourriture=Label(self.cadre, text=self.mod.joueurs[self.nom].nourriture,bg=self.couleurinfo, font=self.infofont)

        self.labdeuterium= Label(self.cadre, text="Deuterium:",bg=self.couleurinfo, font=self.infofont)
        self.nbdeuterium=Label(self.cadre, text=self.mod.joueurs[self.nom].deuterium,bg=self.couleurinfo, font=self.infofont)

        self.labmoral= Label(self.cadre, text="Moral:",bg=self.couleurinfo, font=self.infofont)
        self.nbmoral=Label(self.cadre, text="-",bg=self.couleurinfo, font=self.infofont)

        #self.labespacement=Label(self.cadreinfojoueur, text="              ", bg=self.couleurinfo)
        self.labaffichagevue=Label(self.cadreinfojoueur, text="Vues", bg=self.couleurbouton, font=self.labfont)

        self.bgalaxie=Button(self.cadreinfojoueur,text="Galaxie",bg=self.couleurbouton, font=self.infofont)
        self.bsolaire=Button(self.cadreinfojoueur,text="Solaire",bg=self.couleurbouton, font=self.infofont)
        self.bplanete=Button(self.cadreinfojoueur,text="Planete",bg=self.couleurbouton, font=self.infofont)
        self.bsolairemere=Button(self.cadreinfojoueur,text="SolaireMere",bg=self.couleurbouton, font=self.infofont)

        self.gridCadreInfoJoueur(self.cadre,self.mod)

    def gridCadreInfoJoueur(self,cadre,mod):
        self.cadre = cadre
        self.mod = mod

        self.labcouleur.grid(row=0,column=0)
        self.idcouleur.grid(row=0,column=1, sticky=W+E)
        self.labcouttotal.grid(row=0,column=2)
        self.nbcouttotal.grid(row=0,column=3)
        # ajout text var
        self.labcredit.grid(row=0,column=6)
        self.nbcredit.grid(row=0,column=7)
        self.labnourriture.grid(row=0,column=8)
        self.nbnourriture.grid(row=0,column=9)
        self.labdeuterium.grid(row=0,column=4)
        self.nbdeuterium.grid(row=0,column=5)
        self.labmoral.grid(row=0,column=10)
        self.nbmoral.grid(row=0,column=11)
        #self.labaffichagevue.grid(row=1, column=3, columnspan=1, sticky=W+E)
        #self.labespacement.grid(row=5, column=0, columnspan=3, sticky=W+E)
        # boutons
        self.btnarbretech.grid(row=1,column=9, columnspan=2, sticky=W+E)
        self.bgalaxie.grid(row = 1, column =1, sticky=W+E)
        self.bsolaire.grid(row = 1, column =3, sticky=W+E)
        self.bplanete.grid(row = 1, column =5, sticky=W+E)
        self.bsolairemere.grid(row=1,column=7, sticky=W+E)
        self.bsolairemere.config(state=NORMAL, command = lambda : self.combinedactions())

    def creeraffichercadrepartie(self,mod):
        self.nom=self.parent.monnom
        self.mod=mod
        self.cadreoutilsgeneral.grid()
        self.vues={"Galaxie":VueGalaxie(self.cadrejeu,self),
					"Planete":VuePlanete(self.cadrejeu,self),
					"Solaire":VueSolaire(self.cadrejeu,self)}
        self.changevueactive(self.vues["Solaire"])
        self.vueactive.cadrespatial.grid()

        self.cadreinfojoueur=Frame(self.cadrepartie,height=100, width=800, bg="gray")
        self.cadreMessagerie=Frame(self.cadrepartie,height=100, width=400, bg="pink")
        self.cadreinfojoueur.grid(row=0, column=0, sticky=W+E)
        self.cadreMessagerie.grid(row=0, column=1, rowspan=2, sticky=N)


        self.creerCadreInfoJoueur(self.cadreinfojoueur,self.mod)

        self.bgalaxie.bind("<Button>",self.changementdevue)

        self.cadreoutils.grid(row=2, column=1)

        self.lbselectecible=Label(self.cadreinfo,text="Choisir cible",bg="darkgrey")


        # création des objets de Messagerie
        self.labMessagerie=Label(self.cadreMessagerie,text="Messagerie", font=self.infofont)
        self.afficherMenuJoueur()
        self.listeMessage=Listbox(self.cadreMessagerie, fg="blue",width=45)
        self.scrollMessage=Scrollbar(self.cadreMessagerie, orient=VERTICAL)
        self.entryMessage=Entry(self.cadreMessagerie)
        self.envoiMessage=Button(self.cadreMessagerie,text="Envoyer", command=self.envoyerMessage, width=10)


        #self.labDiplomatie=Label(self.cadreinfojoueur, text="Diplomatie", font=self.labfont)
        #self.btnAlliance=Button(self.cadreinfojoueur, text="Alliance", bg="blue", font=self.infofont)
        #self.btnGuerre=Button(self.cadreinfojoueur, text="Guerre", bg="red", font=self.infofont)
        #self.btnAllianceGuerriere=Button(self.cadreinfojoueur, text="Pacte Guerre",bg="green", font=self.infofont)
        #self.btnPaix=Button(self.cadreinfojoueur, text="Paix", bg="white", font=self.infofont)


        self.labMessagerie.grid(row=0, columnspan=2, sticky=W+E)
        self.listeMessage.grid(row=1, column=0, sticky=W+E)
        self.scrollMessage.grid(row=1, column=1, sticky=W+E+N+S)
        self.entryMessage.grid(row=3, column=0, sticky=W+E+N+S)
        self.envoiMessage.grid(row=3, column=1, sticky=W)


        #self.labDiplomatie.grid(row=2, column=4,sticky=W+E)
        #self.btnAlliance.grid(row=2, column=5, sticky=W+E)
        #self.btnGuerre.grid(row=2, column=6, sticky=W+E)
        #self.btnAllianceGuerriere.grid(row=2, column=7, sticky=W+E)
        #self.btnPaix.grid(row=2, column=8,sticky=W+E)


    def choix(self, *args):
        print(self.tkvar.get())

    def afficherMenuJoueur(self):
        self.tkvar = StringVar(self.root)
        self.tkvar.trace("w", self.choix)
        nomJoueur=self.tkvar.get()

        listenomjoueur=["Tous"]+ list(self.mod.joueurs.keys())

        self.tkvar.set("Tous")
        self.menu = OptionMenu(self.cadreMessagerie, self.tkvar, *listenomjoueur)

        self.menu.grid(row=2, columnspan=2, sticky=W+E)



        self.changecadre(self.cadrepartie)


    def envoyerMessage(self):
        message = self.entryMessage.get()
        recipiendaire = self.tkvar.get()
        envoyeur=self.parent.monnom
        if message and recipiendaire:
            self.parent.envoyermessage(envoyeur, recipiendaire, message)
            self.tkvar.set("")



    def afficherpartie(self,mod,idsolaire):

        self.afficheMessage(mod)
        self.vues["Galaxie"].afficherpartieGalaxie(mod)
        self.vues["Solaire"].afficherVaisseau(mod)
        self.vues["Solaire"].afficherSystemeSolaire(mod,idsolaire)


        if self.parent.egoserveur == 1 and self.parent.attente == 0:
            self.parent.actualiserGalaxie()


        self.vues["Solaire"].afficherSystemeSolaire(mod,idsolaire)
        self.vues["Solaire"].afficherVaisseau(mod)
    def afficheMessage(self,mod):
        for i in mod.joueurs.keys():
            pass

        nom=self.parent.monnom
        joueur = mod.joueurs[nom]
        msgs = joueur.messages



        self.listeMessage.delete(0, END)

        for i in msgs:
            msg=i[0]+", "+i[1]+": "+i[2]
            self.listeMessage.insert(END, msg)




    def creervaisseau(self,widg,nomVais):
        nomVais1=nomVais
        self.parent.creervaisseau(nomVais1)
        self.maselection=None
        self.vues["Solaire"].canevasSolaire.delete("marqueur")




    def createElemTech(self):
        self.btnAvacfont=font=("Helvetica",10,"bold")
        self.btnEco=Button(self.cadreArbreTechno,text="Economie",height=1, width = 14, bg = "light gray", font=self.btnAvacfont)
        self.btnMilit=Button(self.cadreArbreTechno,text="Militaire",height=1, width = 14, bg = "light gray", font=self.btnAvacfont)

        self.cadreArbreTechno.create_window(0, 0, anchor=NW, window=self.btnEco, tags=("onglet", "Eco"))
        self.cadreArbreTechno.create_window(100, 0, anchor=NW, window=self.btnMilit, tags=("onglet", "Milit"))

        self.btnAvac1 = Button(self.cadreArbreTechno, text = "Bonus production", font=self.btnAvacfont, height =1 , width = 14,bg = "azure", state= NORMAL )
        self.btnAvac2 = Button(self.cadreArbreTechno, text = "Bonus production x 2", font=self.btnAvacfont, height =1 , width = 16,bg = "azure", state= NORMAL )
        self.btnAvac3 = Button(self.cadreArbreTechno, text = "Couts Reduit", font=self.btnAvacfont, height =1 , width = 16,bg = "azure", state= NORMAL )
        self.btnAvac4 = Button(self.cadreArbreTechno, text = "Bonus production x 4", font=self.btnAvacfont, height =1 , width = 16,bg = "azure", state= NORMAL )
        self.btnAvac5 = Button(self.cadreArbreTechno, text = "Couts Reduit x 2", font=self.btnAvacfont, height =1 , width = 16,bg = "azure", state= NORMAL )

        self.cadreArbreTechno.create_window(60,110,window = self.btnAvac1, tags = "Avac1")
        self.cadreArbreTechno.create_window(130,70,window = self.btnAvac2, tags = "Avac2")
        self.cadreArbreTechno.create_window(130,150,window = self.btnAvac3, tags = "Avac3")
        self.cadreArbreTechno.create_window(270,70,window = self.btnAvac4, tags = "Avac4")
        self.cadreArbreTechno.create_window(270,150,window = self.btnAvac5, tags = "Avac5")

        self.cadreArbreTechno.create_line(105,100,145,75)
        self.cadreArbreTechno.create_line(190,68,270,68)
        self.cadreArbreTechno.create_line(70,105,150,135)
        self.cadreArbreTechno.create_line(190,150,270,150)

        self.btnEco.bind("<Button>", self.actionOngletEco)
        self.btnMilit.bind("<Button>", self.actionOngletMilit)


        self.btnAvac1.bind("<Button>", self.actionElemTech)
        self.btnAvac2.bind("<Button>", self.actionElemTech)
        self.btnAvac3.bind("<Button>", self.actionElemTech)
        self.btnAvac4.bind("<Button>", self.actionElemTech)
        self.btnAvac5.bind("<Button>", self.actionElemTech)

        self.actionOngletEco(self)

    def actionOngletEco(self,event):
        self.ongletActif = "economie"
        self.btnAvac1.config(text = "Bonus production")
        self.btnAvac2.config(text = "Bonus production x 2")
        self.btnAvac3.config(text = "Couts Reduit")
        self.btnAvac4.config(text = "Bonus production x 4")
        self.btnAvac5.config(text = "Couts Reduit x 2")

    def actionOngletMilit(self,event):
        self.ongletActif = "Militaire"
        self.btnVaisfont=font=("Helvetica",10,"bold")
        self.btnAvac1.config(text = "Vaisseau Canon",font=self.btnVaisfont, command= lambda: self.gridhelper(self.vues["Solaire"].newVais1,17,0))
        self.btnAvac2.config(text = "Vaisseau Eclaireur",font=self.btnVaisfont,command= lambda: self.gridhelper(self.vues["Solaire"].newVais2,17,1))
        self.btnAvac3.config(text = "Vaisseau Tank",font=self.btnVaisfont,command= lambda: self.gridhelper(self.vues["Solaire"].newVais3,17,2))
        self.btnAvac4.config(text = "Vaisseau Laser",font=self.btnVaisfont,command= lambda: self.gridhelper(self.vues["Solaire"].newVais4,18,0))
        self.btnAvac5.config(text = "Vaisseau Sniper",font=self.btnVaisfont,command= lambda: self.gridhelper(self.vues["Solaire"].newVais5,18,1))

        if self.arbretechMilitState == 0:
            self.btnAvac1.config(state = NORMAL,bg = "azure")
            self.btnAvac2.config(state = NORMAL,bg = "azure")
            self.btnAvac3.config(state = NORMAL,bg = "azure")
            self.btnAvac4.config(state = NORMAL,bg = "azure")
            self.btnAvac5.config(state = NORMAL,bg = "azure")

        if self.arbretechMilitState == 1:
            self.btnAvac2.config(state = NORMAL,bg = "azure")
            self.btnAvac3.config(state = NORMAL,bg = "azure")
            self.btnAvac4.config(state = NORMAL,bg = "azure")
            self.btnAvac5.config(state = NORMAL,bg = "azure")

        if self.arbretechMilitState == 2:
            self.btnAvac3.config(state = NORMAL,bg = "azure")
            self.btnAvac4.config(state = NORMAL,bg = "azure")
            self.btnAvac5.config(state = NORMAL,bg = "azure")

        if self.arbretechMilitState == 3:
            self.btnAvac2.config(state = NORMAL,bg = "azure")
            self.btnAvac4.config(state = NORMAL,bg = "azure")
            self.btnAvac5.config(state = NORMAL,bg = "azure")

        if self.arbretechMilitState == 4:
            self.btnAvac3.config(state = NORMAL,bg = "azure")
            self.btnAvac5.config(state = NORMAL,bg = "azure")

        if self.arbretechMilitState == 5:
            self.btnAvac2.config(state = NORMAL,bg = "azure")
            self.btnAvac4.config(state = NORMAL,bg = "azure")


    def gridhelper(self, button,arow,acolumn):
        button.grid(row=arow,column=acolumn)

    def actionOngletScience(self,event):
        self.ongletActif = "Science"

        self.btnAvac1.config(text = "PlaceHolder")
        self.btnAvac2.config(text = "PlaceHolder")
        self.btnAvac3.config(text = "PlaceHolder")
        self.btnAvac4.config(text = "PlaceHolder")
        self.btnAvac5.config(text = "PlaceHolder")

    def disableBtnAvac1(self):
        self.btnAvac1.config(state = DISABLED, bg="gray20")

    def disableBtnAvac2(self):
        self.btnAvac1.config(state = DISABLED, bg="gray20")
        self.btnAvac2.config(state = DISABLED, bg="gray20")

    def disableBtnAvac3(self):
        self.btnAvac1.config(state = DISABLED, bg="gray20")
        self.btnAvac3.config(state = DISABLED, bg="gray20")

    def disableBtnAvac4(self):
        self.btnAvac1.config(state = DISABLED, bg="gray20")
        self.btnAvac2.config(state = DISABLED, bg="gray20")
        self.btnAvac4.config(state = DISABLED, bg="gray20")

    def disableBtnAvac5(self):
        self.btnAvac1.config(state = DISABLED, bg="gray20")
        self.btnAvac3.config(state = DISABLED, bg="gray20")
        self.btnAvac5.config(state = DISABLED, bg="gray20")

    def actionElemTech(self,event):
        avancement = event.widget.cget("text")
        etat = event.widget.cget("state")
        if avancement:
            if etat == "normal":
                self.parent.avancementTechno(avancement)

    def CliqueVuePlanete(self,canvas,mod,SysSolaire,idPlanete):
        self.canvas = canvas
        self.mod = mod
        self.SystemeSolaire=SysSolaire
        t=self.canvas.gettags(CURRENT)
        if t:
            if self.canvas == self.vues["Planete"].canevasPlanete:
                self.vues["Planete"].afficherInfosPlanete(self.mod,int(idPlanete))

                self.vues["Solaire"].afficherSystemeSolaire(self.mod,self.SystemeSolaire.id)
                self.bsolaire.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Solaire"]) )

    def CliqueVueSySsolaire(self,canvas,mod):
        self.canvas = canvas
        self.mod = mod

        t=self.canvas.gettags(CURRENT)
        if t:
            if self.canvas == self.vues["Solaire"].canevasSolaire:
                if t[1] == "planeteMere":
                    self.vues["Solaire"].cliqueSolaire(CURRENT)

                    self.vues["Solaire"].afficherInfosPlanete(self.mod,int(t[2]))
                    self.vues["Planete"].afficherPlanete(self.mod,int(t[2]))
                    self.bplanete.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Planete"]) )
                elif t[1]=="flotte":
                    self.vues["Solaire"].cliqueSolaire(CURRENT)
                    self.vues["Solaire"].versGalaxie.config(state=ACTIVE, command = lambda  : self.vues["Solaire"].envoyerVersGalaxie(t,self.mod))
                elif t[1]=="planete":
                    self.vues["Solaire"].cliqueSolaire(CURRENT)
                    self.vues["Solaire"].afficherInfosPlanete(self.mod,int(t[2]))
                elif t[1] is not None:
                    self.vues["Solaire"].afficherInfosPlanete(self.mod,int(t[2]))
                    self.vues["Planete"].afficherPlanete(self.mod,int(t[2]))

                    self.bplanete.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Planete"]) )

                self.mod.joueurs[self.nom].setbuffer(t[2])


    def CliqueVueGalaxie(self,canvas,mod):
        self.canvas = canvas
        self.mod = mod
        s=self.canvas.gettags(CURRENT)
        if s:
            if self.canvas == self.vues["Galaxie"].canevasGalaxie:
                if s[0] == "etoile":
                    self.vues["Galaxie"].afficherInfosSystemSolaire(self.mod,int(s[1]))

                    self.vues["Solaire"].afficherSystemeSolaire(self.mod,int(s[1]))
                    self.vues["Galaxie"].afficherpartieGalaxie(self.mod)
                    self.bsolaire.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Solaire"]) )
                    self.mod.joueurs[self.nom].setbuffer(s[1])
                    self.mod.joueurs[self.nom].setSysSolaireBuffer(s[1])
                    self.vues["Galaxie"].cliquecosmos(CURRENT)

                elif s[1]=="flotte":
                    self.vues["Galaxie"].cliquecosmos(CURRENT)
                    self.vues["Galaxie"].versSoleil.config(state=ACTIVE, command = lambda  : self.vues["Galaxie"].envoyerVersSoleil(s,self.mod))

    def updateInfosJoueur(self,mod):
        self.nbnourriture.config(text=self.mod.joueurs[self.nom].nourriture)
        self.nbcredit.config(text=self.mod.joueurs[self.nom].credit)
        self.nbdeuterium.config(text=self.mod.joueurs[self.nom].deuterium)

class VueSolaire():
    def __init__(self,fen,parent):

        self.cadrejeu=fen
        self.parent=parent
        self.cadrespatial=Frame(self.cadrejeu)
        self.cadreinfo=Frame(self.parent.cadreoutils)
        self.canevasSolaire=Canvas(self.cadrespatial,width=self.parent.largeur,height=self.parent.hauteur,bg="grey11")

        self.canevasSolaire.bind( "<Button-1>", lambda event, canvas = self.canevasSolaire : self.parent.CliqueVueSySsolaire(canvas,self.parent.modele))
        self.canevasSolaire.grid(row = 0, column =1)
        self.couleurs = ["RoyalBlue3","light coral", "cadet blue", "cyan",
                        "navajo white", "blue violet", "aquamarine2", "forest green",
                        "SeaGreen1", "plum2" ]

        self.planeteNom=Label(self.cadreinfo)
        self.planeteId=Label(self.cadreinfo)
        self.planeteProprio=Label(self.cadreinfo)
        self.planeteTaille=Label(self.cadreinfo)
        self.planeteCharbon = Label(self.cadreinfo)
        self.planeteZinc = Label(self.cadreinfo)
        self.planeteDeuterium = Label(self.cadreinfo)
        self.planeteFertile = Label(self.cadreinfo)
        self.sysSolaireNom = Label(self.cadreinfo)
        self.variationNomSysSolaire = StringVar()
        self.sysSolaireNom.grid(row = 0, column =0, sticky=W+E)
        self.boutonsVais=[]

        curwd = os.path.dirname(os.path.realpath(__file__))

        self.vaisCanonMenu=resizeImage.resizeImage("m",50,curwd+"\\images\\vaisseauCanon.png")
        self.vaisEclaireurMenu=resizeImage.resizeImage("m",50,curwd+"\\images\\vaisseauEclaireur.png")
        self.vaisLaserMenu=resizeImage.resizeImage("m",50,curwd+"\\images\\vaisseauLaser.png")
        self.vaisSniperMenu=resizeImage.resizeImage("m",50,curwd+"\\images\\vaisseauSniper.png")
        self.vaisTankMenu=resizeImage.resizeImage("m",50,curwd+"\\images\\vaisseauTank.png")
        self.vaisCanonCan=resizeImage.resizeImage("C",30,curwd+"\\images\\vaisseauCanon.png")
        self.vaisEclaireurCan=resizeImage.resizeImage("C",30,curwd+"\\images\\vaisseauEclaireur.png")
        self.vaisLaserCan=resizeImage.resizeImage("C",30,curwd+"\\images\\vaisseauLaser.png")
        self.vaisSniperCan=resizeImage.resizeImage("C",30,curwd+"\\images\\vaisseauSniper.png")
        self.vaisTankCan=resizeImage.resizeImage("C",30,curwd+"\\images\\vaisseauTank.png")

        self.newVais1 = Button(self.cadreinfo,image=self.vaisCanonMenu,text="Vaisseau Canon",bg="DeepSkyBlue2")
        self.newVais2 = Button(self.cadreinfo,image=self.vaisEclaireurMenu,text="Vaisseau Eclaireur",bg="DeepSkyBlue2" )
        self.newVais3 = Button(self.cadreinfo,image=self.vaisTankMenu,text="Vaisseau Tank",bg="DeepSkyBlue2")
        self.newVais4 = Button(self.cadreinfo,image=self.vaisLaserMenu,text="Vaisseau Laser",bg="DeepSkyBlue2")
        self.newVais5 = Button(self.cadreinfo,image=self.vaisSniperMenu,text="Vaisseau Sniper",bg="DeepSkyBlue2")


        self.newVais1.bind( "<Button-1>", self.selectvaisseau)
        self.newVais2.bind( "<Button-1>", self.selectvaisseau)
        self.newVais3.bind( "<Button-1>", self.selectvaisseau)
        self.newVais4.bind("<Button-1>", self.selectvaisseau )
        self.newVais5.bind( "<Button-1>", self.selectvaisseau)


        self.versGalaxie = Button(self.cadreinfo,text="Vers la Galaxie",bg="DeepSkyBlue2", command=self.envoyerVersGalaxie, font=("Helvetica",12,"bold"))
        self.maselection2=None

    def gridhelper(self, button,arow,acolumn):
        button.grid(row=arow,column=acolumn)

    def selectvaisseau(self,evt):
        w=evt.widget
        typev=w.cget("text")
        self.parent.creervaisseau(w,typev)


    def envoyerVersGalaxie(self,t,mod):
        self.mod=mod
        self.t=t

        self.parent.parent.changerVueVaisseau(t[2],t[4],t[5])

    def afficherdecorSolaire(self,mod,idSolaire):
        self.mod = mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire
        self.unSysSolaire = self.listeSysSolaire[0]
        self.planete= self.mod.joueurs[self.parent.nom].planetemere
        self.unSysSolaire=self.planete.parent

        for syssolaire in self.listeSysSolaire:
            if syssolaire.id==idSolaire:
                for i in syssolaire.listeObjArrierePlan:
                    self.canevasSolaire.create_oval(i[0],i[1],i[0]+1,i[1]+1,fill="white",tags=(None,"fond",None,None))
        #curwd = os.path.dirname(os.path.realpath(__file__))

        #image = resizeImage.resizeImage("",600,curwd+"\\images\\galaxy-png-date-2000.jpg")
        #self.canevasSolaire.create_image(10, 10, image = image, anchor = NW)

        self.canevasSolaire.config(bg="midnight blue")

        #for i in range(random.randrange(10,20)):
          #  x=random.randrange(mod.largeur)
          #  y=random.randrange(mod.hauteur)
          #  self.canevasSolaire.create_rectangle(x,y,x+8,y+8, fill="light gray", tags=(None,"asteroide",None,None))

        self._create_circle(self.parent.largeur*0.5,self.parent.hauteur*0.5,75)

        #self.parent.CliqueVueSySsolaire(self.canevasSolaire,mod)


        self.afficherVaisseau(mod)
        self.afficherProjectile(mod)


    def _create_circle(self, x, y, r):
        return self.canevasSolaire.create_oval(x-r, y-r, x+r, y+r,fill="yellow",tags=(None,"soleil",None,None))


    def afficherSystemeSolaire(self,modele,idSolaire):
        self.modele=modele
        self.id=idSolaire
        self.canevasSolaire.delete("all")
        self.afficherdecorSolaire(self.modele,idSolaire)

        for a in (self.modele.Galaxie.listeSysSolaire):

            if (a.id == idSolaire):
                self.systemeSolaire=a
        for i in self.systemeSolaire.listePlanete:
            t=i.taille*4
            if(i.proprietaire=="inconnu"):
                self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill=i.couleur,tags=("Inconnu","planete",str(i.id),None))
            elif(i.proprietaire is not None):
                player = None
                for k in self.mod.ias:
                    if(k.nom == i.proprietaire):
                        player = k
                        self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill=player.couleur,tags=(i.proprietaire,"planeteMere",str(i.id),"possession"))
                for j in self.mod.joueurs:
                    if(modele.joueurs[j].nom == i.proprietaire):
                        player = j
                        self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill=modele.joueurs[player].couleur,tags=(i.proprietaire,"planeteMere",str(i.id),"possession"))

        self.parent.CliqueVueSySsolaire(self.canevasSolaire,self.modele)


    def afficherInfosSystemSolaire(self, modele, idSysteme):


        self.modele=modele
        for i in (self.modele.Galaxie.listeSysSolaire):
            if (i.id == idSysteme):
                self.systeme=i
        self.variationNomSysSolaire.set("Nom Sys : " + str(self.systeme.nometoile))
        self.sysSolaireNom.config(bg="white", textvariable=self.variationNomSysSolaire, font=("Helvetica",10,"bold") )

    def afficherVaisseau(self,modele):
        self.canevasSolaire.delete("artefact")
        for i in modele.joueurs.keys():
            i=modele.joueurs[i]

            for j in i.flotteSystemeSolaire:
                if(j.espaceCourant):
                    if(j.espaceCourant.id ==self.id):
                        if(j.etat=="vivant"):
                            if (j.nomVaisseau=="Vaisseau Canon"):
                                self.canevasSolaire.create_image(j.x,j.y,image=self.vaisCanonCan,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",str(j.espaceCourant.id),str(j.solaire.id)))
                            elif (j.nomVaisseau=="Vaisseau Eclaireur"):
                                self.canevasSolaire.create_image(j.x,j.y,image=self.vaisEclaireurCan,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",str(j.espaceCourant.id),str(j.solaire.id)))
                            elif (j.nomVaisseau=="Vaisseau Laser"):
                                self.canevasSolaire.create_image(j.x,j.y,image=self.vaisLaserCan,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",str(j.espaceCourant.id),str(j.solaire.id)))
                            elif (j.nomVaisseau=="Vaisseau Sniper"):
                                self.canevasSolaire.create_image(j.x,j.y,image=self.vaisSniperCan,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",str(j.espaceCourant.id),str(j.solaire.id)))
                            elif (j.nomVaisseau=="Vaisseau Tank"):
                                self.canevasSolaire.create_image(j.x,j.y,image=self.vaisTankCan,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",str(j.espaceCourant.id),str(j.solaire.id)))

                    for p in j.projectile:
                        debutx,debuty=hlp.getAngledPoint(p.angle,15,p.x,p.y)
                        self.canevasSolaire.create_line(p.x,p.y,debutx,debuty,
                                    fill="royalblue",tags=("artefact","projectile",None,None,None,None),width=3)

        for i in modele.ias:
            for j in i.flotteSystemeSolaire:
                if(j.espaceCourant):
                    if(j.espaceCourant.id ==self.id):
                        if(j.etat=="vivant"):
                            self.canevasSolaire.create_rectangle(j.x-3,j.y-3,j.x+3,j.y+3,fill=i.couleur,
                                        tags=(j.proprietaire,"flotte",str(j.id),"artefact",str(j.espaceCourant.id),str(j.solaire.id)))
                    for p in j.projectiles:
                        debutx,debuty=hlp.getAngledPoint(p.angle,15,p.x,p.y)
                        self.canevasSolaire.create_line(p.x,p.y,debutx,debuty,
                                    fill="royalblue",tags=("artefact","projectile",None,None,None,None),width=3)


    def afficherProjectile(self,modele):
        pass


    def afficherInfosPlanete(self, modele, idPlanete):

        self.parent.bplanete.config(state = "disabled")
        self.modele=modele
        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j


        self.variationCharbon = StringVar()
        self.variationZinc = StringVar()
        self.variationDeuterium = StringVar()
        self.variationFertile = StringVar()

        self.variationCharbon.set("Charbon : " + str(int(self.planete.charbon)))
        self.variationZinc.set("Zinc : " + str(int(self.planete.zinc)))
        self.variationDeuterium.set("Diamant : " + str(int(self.planete.diamant)))
        self.variationFertile.set("Fertile : " + str(int(self.planete.fertile)))

        self.planeteinfofont=font=("Helvetica",10,"bold")
        self.planeteNom.config( bg="grey", text="Nom: "+ str(self.planete.nom), font=self.planeteinfofont)
        self.planeteId.config( bg="white", text="Id: "+ str(self.planete.id), font=self.planeteinfofont)
        self.planeteProprio.config( bg="white", text="Propriétaire: "+ self.planete.proprietaire, font=self.planeteinfofont)
        self.planeteTaille.config( bg="white", text="Taille: "+ str(self.planete.taille), font=self.planeteinfofont)
        self.planeteCharbon.config( bg="white", textvariable=self.variationCharbon, font=self.planeteinfofont)
        self.planeteZinc.config( bg="white",textvariable=self.variationZinc, font=self.planeteinfofont)
        self.planeteDeuterium.config(bg="white",textvariable=self.variationDeuterium, font=self.planeteinfofont)
        self.planeteFertile.config(bg="white",textvariable=self.variationFertile, font=self.planeteinfofont)


        self.planeteNom.grid(row=1, column=0, sticky=W+E)
        self.planeteId.grid(row=2, column=0, sticky=W+E)
        self.planeteProprio.grid(row=11, column=0, sticky=W+E)
        self.planeteTaille.grid(row=12, column=0, sticky=W+E)
        self.planeteCharbon.grid(row=13, column=0, sticky=W+E)
        self.planeteZinc.grid(row=14, column=0, sticky=W+E)
        self.planeteDeuterium.grid(row=15, column=0, sticky=W+E)
        self.planeteFertile.grid(row=16, column=0, sticky=W+E)


        self.versGalaxie.grid(row=19,column=0, sticky=W+E)

    def changerProprietaire(self,idplanete,couleur):

        for i in self.canevasSolaire.find_all():
            if self.canevasSolaire.gettags(i)[2] == str(idplanete):
                self.canevasSolaire.itemconfig(i, fill=couleur)

    def cliqueSolaire(self,evt):

        t=self.canevasSolaire.gettags(CURRENT)
        if t and t[0]==self.parent.nom:

            self.maselection=[self.parent.nom,t[1],t[2]]

            if "planeteMere" not in t:
                self.maselection2=[self.parent.nom,t[1],t[2]]
            if t[1] == "planete":
                self.montreplaneteselection()
            elif t[1] == "flotte":
                pass

            elif "planeteMere" in t and t[0]==self.parent.nom and self.maselection2:
                self.parent.parent.ciblerflotte(self.maselection2[2],t[2])
          #      self.parent.parent.ciblerflotte(self.maselection2[2],t[2])
                self.maselection2=None
        elif "planeteMere" in t and t[0]!=self.parent.nom:
                self.parent.parent.ciblerflotte(self.maselection[2],t[2])
        elif "planete" in t and t[0]!=self.parent.nom:
            if self.maselection:
                pass
                self.parent.parent.ciblerflotte(self.maselection[2],t[2])
            self.maselection=None
            self.canevasSolaire.delete("marqueur")
        elif "flotte" in t :
            self.maselection=None
        else:
            self.maselection=None
            self.canevasSolaire.delete("marqueur")

    def montreplaneteselection(self):
        self.newVais1.grid(row=7,column=0)
        self.newVais2.grid(row=7,column=1)
        self.newVais3.grid(row=6,column=2)
        self.newVais4.grid(row=8,column=0)
        self.newVais5.grid(row=8,column=1)



class VuePlanete():
    def __init__(self,fen,parent):
        self.cadrejeu=fen
        self.parent=parent
        self.cadrespatial=Frame(self.cadrejeu)
        self.cadreinfo=Frame(self.parent.cadreoutils)
        self.canevasPlanete=Canvas(self.cadrespatial,width=self.parent.largeur,height=self.parent.hauteur,bg="grey11")
        self.canevasPlanete.grid(row = 0, column =1)
        self.cadreStruct = Frame(self.cadreinfo)

        self.planeteNom=Label(self.cadreinfo)
        self.planeteProprio=Label(self.cadreinfo)
        self.planeteTaille=Label(self.cadreinfo)
        self.planeteCharbon = Label(self.cadreinfo)
        self.planeteZinc = Label(self.cadreinfo)
        self.planeteDeuterium = Label(self.cadreinfo)
        self.planeteFertile = Label(self.cadreinfo)

        curwd = os.path.dirname(os.path.realpath(__file__))

        self.raffinerieCharbonMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\raffinerieCharbon.png")
        self.raffinerieDiamantMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\raffinerieDiamant1.png")
        self.raffinerieIsotopeMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\raffinerieIsotope.png")
        self.usineCivileMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\usineCivile.png")
        self.usineMilitaireMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\usineMilitairekra.png")
        self.capitaleMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\capital.png")
        self.fermeMenu=resizeImage.resizeImage("M",50,curwd+"\\images\\ferme.png")

        self.raffinerieCharbonCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\raffinerieCharbon.png")
        self.raffinerieDiamantCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\raffinerieDiamant1.png")
        self.raffinerieIsotopeCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\raffinerieIsotope.png")
        self.usineCivileCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\usineCivile.png")
        self.usineMilitaireCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\usineMilitairekra.png")
        self.capitaleCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\capital.png")
        self.fermeCanvas=resizeImage.resizeImage("C",100,curwd+"\\images\\ferme.png")





    def afficherdecorPlanete1(self,mod):
        self.mod = mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire
        self.unSysSolaire = random.choice(self.listeSysSolaire)

    #Fonction originale:
    def afficherdecorPlanete(self,mod):
        self.mod = mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire
        self.unSysSolaire = random.choice(self.listeSysSolaire)
        for i in range(random.randrange(24, 156)):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasPlanete.create_oval(x,y,x+1,y+1,fill="white",tags=("fond"))


    def afficherInfosPlanete(self, modele, idPlanete):

        self.modele=modele

        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j

        self.variationCharbon = StringVar()
        self.variationZinc = StringVar()
        self.variationDeuterium = StringVar()
        self.variationFertile = StringVar()

        self.variationCharbon.set("Charbon : " + str(int(self.planete.charbon)))
        self.variationZinc.set("Zinc : " + str(int(self.planete.zinc)))
        self.variationDeuterium.set("Deuterium : " + str(int(self.planete.deuterium)))
        self.variationFertile.set("Fertile : " + str(int(self.planete.fertile)))

        self.planeteNom.config( bg="white", text="Id: "+ str(self.planete.id))
        self.planeteProprio.config( bg="white", text="Propriétaire: "+ self.planete.proprietaire)
        self.planeteTaille.config( bg="white", text="Taille: "+ str(self.planete.taille))
        self.planeteCharbon.config( bg="white", textvariable=self.variationCharbon )
        self.planeteZinc.config( bg="white",textvariable=self.variationZinc)
        self.planeteDeuterium.config(bg="white",textvariable=self.variationDeuterium)
        self.planeteFertile.config(bg="white",textvariable=self.variationFertile)

        self.planeteNom.grid(row=0, column=0)
        self.planeteProprio.grid(row=1, column=0)
        self.planeteTaille.grid(row=2, column=0)
        self.planeteCharbon.grid(row=3, column=0)
        self.planeteZinc.grid(row=4, column=0)
        self.planeteDeuterium.grid(row=5, column=0)
        self.planeteFertile.grid(row=6, column=0)



    def afficherPlanete(self,modele,idPlanete):

        self.modele=modele
        self.id=idPlanete
        self.canevasPlanete.delete("all")
        self.afficherdecorPlanete(self.modele)


        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j

        demiTaille=self.planete.tailleAffichage/2


        cx=self.mod.largeur/2
        cy=self.mod.hauteur/2
        x1=cx - demiTaille
        x2=cx + demiTaille
        y1=cy - demiTaille
        y2=cy + demiTaille
        self.canevasPlanete.create_oval(x1, y1, x2, y2, fill=self.planete.couleur,tags=("planeteMere",id, self.planete.taille))

        self.afficheEmplacement(self.planete)
        self.afficheStructure(self.planete.id)

        self.canevasPlanete.bind( "<Button-1>", self.cliqueEmplacement)


    def cliqueEmplacement(self,evt=0):
        tagsPlanete=self.canevasPlanete.gettags("current")
        if tagsPlanete:
            if tagsPlanete[0] == "emplacement":
                self.menuStructPlanete()
                self.emplacementSelectionne=tagsPlanete
            if tagsPlanete[0] != "emplacement":
                self.cadreStruct.grid_forget()
        else:
            self.cadreStruct.grid_forget()



    def afficherPlanete2(self,modele,idPlanete):
        self.modele=modele
        self.id=idPlanete
        self.canevasPlanete.delete("all")
        self.afficherdecorPlanete(self.modele)
        x=200
        y=100
        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j

        taille=self.planete.taille*50
        self.canevasPlanete.create_oval(x, y, x+taille, y+taille,fill=self.planete.couleur ,tags=("planeteMere",id, taille))

        self.canevasPlanete.bind( "<Button-1>", lambda event, canvas = self.canevasPlanete : self.parent.CliqueVuePlanete(canvas,self.parent.modele,self.planete.parent,self.id))

    def menuStructPlanete(self):
        self.createFrameStruct()
        self.showFrameStruct()
        self.cadreStruct.config(bg = "dark turquoise")

        self.cadreStruct.grid(row=2, column = 0)

    def createFrameStruct(self):
        self.buttonfont=  font=("Helvetica",10,"bold")
        self.buttonUsineCiv = Button(self.cadreStruct, font=self.buttonfont, text = "Usine Civile",height = 2, width = 15)
        self.buttonUsineMili = Button(self.cadreStruct, font=self.buttonfont, text = "Usine Militaire",height = 2, width = 15)
        self.buttonRaffDia = Button(self.cadreStruct, font=self.buttonfont, text = "Raffinerie (Diamant)",height = 2, width = 15)
        self.buttonRaffChar = Button(self.cadreStruct, font=self.buttonfont, text = "Raffinerie (Charbon)",height = 2, width = 15)
        self.buttonRaffIso = Button(self.cadreStruct, font=self.buttonfont, text = "Raffinerie (Isotope)",height = 2, width = 15)
        self.buttonFerme = Button(self.cadreStruct, font=self.buttonfont, text = "Ferme",height = 2, width = 15)
        self.buttonCapitale = Button(self.cadreStruct, font=self.buttonfont, text = "Capitale",height = 2, width = 15)

        self.buttonUsineCiv.bind("<Button>",self.creerStructure)
        self.buttonUsineMili.bind("<Button>",self.creerStructure)
        self.buttonRaffDia.bind("<Button>",self.creerStructure)
        self.buttonRaffChar.bind("<Button>",self.creerStructure)
        self.buttonRaffIso.bind("<Button>",self.creerStructure)
        self.buttonFerme.bind("<Button>",self.creerStructure)
        self.buttonCapitale.bind("<Button>",self.creerStructure)

    def showFrameStruct(self):
        self.buttonUsineCiv.grid(row=1 , column = 0)
        self.buttonUsineMili.grid(row=2 , column = 0)
        self.buttonRaffDia.grid(row=1 , column = 1)
        self.buttonRaffChar.grid(row=2 , column = 1)
        self.buttonRaffIso.grid(row=3 , column = 1)
        self.buttonFerme.grid(row=3 , column = 0)
        self.buttonCapitale.grid(row=4 , column = 0, columnspan = 2, sticky=W+E)

    def hideFrameStruct(self):
        self.cadreStruct.grid_forget()


    def creerStructure(self,evt):
        j = self.modele.joueurs[self.parent.parent.monnom]
        id = j.bufferSelection[0].id
        nom=evt.widget.cget("text")
        x=int(self.emplacementSelectionne[2])
        y=int(self.emplacementSelectionne[3])
        self.parent.parent.creerStructure(j.nom,nom,id,x,y)


    def afficheEmplacement(self,planete):
        for i in planete.emplacementsDispo:
            t=5
            self.canevasPlanete.create_rectangle(i[0]-t, i[1]-t,  i[0] + t, i[1] + t, fill="red",tags=("emplacement", str(planete.id), str(i[0]),str(i[1])))


    def afficheStructure(self,idplanete):
        self.idplante = idplanete
        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == self.idplante):
                    self.planete=j

        if len(self.planete.listeStructure) > 0:
            for i in self.planete.listeStructure:
                self.x = i.x - 5
                self.y = i.y - 5
                self.diametre =10
                if(i.nomStructure=="Raffinerie (Charbon)"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.raffinerieCharbonCanvas, tags=("batiment_construit"))
                elif(i.nomStructure=="Raffinerie (Diamant)"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.raffinerieDiamantCanvas, tags=("batiment_construit"))
                elif(i.nomStructure=="Raffinerie (Isotope)"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.raffinerieIsotopeCanvas, tags=("batiment_construit"))
                elif(i.nomStructure=="Usine Militaire"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.usineMilitaireCanvas, tags=("batiment_construit"))
                elif(i.nomStructure=="Usine Civile"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.usineCivileCanvas, tags=("batiment_construit"))
                elif(i.nomStructure=="Capitale"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.capitaleCanvas, tags=("batiment_construit"))
                elif(i.nomStructure=="Ferme"):
                    self.canevasPlanete.create_image(self.x,self.y,image= self.fermeCanvas, tags=("batiment_construit"))

                #self.canevasPlanete.create_rectangle(self.x, self.y, self.x + self.diametre, self.y + self.diametre, fill=i.couleur, tags=("batiment_construit"))


class VueGalaxie():

    def __init__(self,fen,parent):

        self.cadrejeu=fen
        self.parent=parent
        self.cadrespatial=Frame(self.cadrejeu)
        self.cadreinfo=Frame(self.parent.cadreoutils)
        self.canevasGalaxie=Canvas(self.cadrespatial,width=self.parent.largeur,height=self.parent.hauteur,bg="grey11")
        self.canevasGalaxie.grid(row = 0, column = 0)

        self.canevasGalaxie.bind( "<Button-1>", lambda event, canvas = self.canevasGalaxie : self.parent.CliqueVueGalaxie(canvas,self.parent.modele))
        self.sysSolaireNom = Label(self.cadreinfo)
        self.mod=parent.mod
        self.sysSolaireNom.grid(row = 0, column =0)
        self.versSoleil = Button(self.cadreinfo,text="Vers la Soleil",bg="DeepSkyBlue2", command=self.envoyerVersSoleil)

        curwd = os.path.dirname(os.path.realpath(__file__))

        self.vaisCanonG=resizeImage.resizeImage("G",20,curwd+"\\images\\vaisseauCanon.png")
        self.vaisEclaireurG=resizeImage.resizeImage("G",20,curwd+"\\images\\vaisseauEclaireur.png")
        self.vaisLaserG=resizeImage.resizeImage("G",20,curwd+"\\images\\vaisseauLaser.png")
        self.vaisSniperG=resizeImage.resizeImage("G",20,curwd+"\\images\\vaisseauSniper.png")
        self.vaisTankG=resizeImage.resizeImage("G",20,curwd+"\\images\\vaisseauTank.png")

    def envoyerVersSoleil(self,t,mod):
        self.mod=mod
        self.t=t
        self.etoile=None
        self.vaisseau=None

        self.parent.parent.changerVueVaisseau(t[2],t[4],t[5])


    def afficherdecorGalaxie(self,mod):
        self.mod =mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire


        for i in self.listeSysSolaire:
            t=i.taille
            self.canevasGalaxie.create_oval(i.x-t, i.y-t,i.x+t,i.y+t,fill=i.couleur, tags=("etoile", str(i.id)))

        self.afficherpartieGalaxie(mod)

    def afficherInfosSystemSolaire(self, modele, idSysteme):

        self.modele=modele
        for i in (self.modele.Galaxie.listeSysSolaire):
            if (i.id == idSysteme):
                self.systeme=i

        self.variationNomSysSolaire = StringVar()
        self.variationNomSysSolaire.set("Système : " + str(self.systeme.nometoile))
        self.sysSolaireNom.config(bg="white", textvariable=self.variationNomSysSolaire)
        self.versSoleil.grid(row=1,column=0)



    def afficherplanemetemereGalaxie(self,evt):
        j=self.mod.joueurs[self.parent.nom]
        couleur=j.couleur
        x=j.planetemere.x
        y=j.planetemere.y
        t=10
        self.canevasGalaxie.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                tags=("planetemere","marqueur"))
    def cliquecosmos(self,evt):
        t=self.canevasGalaxie.gettags(CURRENT)
        if t and t[0]==self.parent.nom:
            self.parent.maselection=[self.parent.nom,t[1],t[2]]
            if t[1] == "etoile":
                self.montreplaneteselection()
            elif t[1] == "flotte":
                self.montreflotteselection()
        elif "etoile" in t and t[0]!=self.parent.nom:
            if self.parent.maselection:
                self.parent.parent.cibleretoile(self.parent.maselection[2],t[1])
            self.parent.maselection=None
            self.parent.lbselectecible.grid_forget()
            self.canevasGalaxie.delete("marqueur")
        else:
            self.parent.maselection=None
            self.parent.lbselectecible.grid_forget()
            self.canevasGalaxie.delete("marqueur")

    def montreplaneteselection(self):
        self.parent.btncreervaisseau.grid(row=1, column=1)
    def montreflotteselection(self):
        self.parent.lbselectecible.grid(row=0, column=0)

    def afficherartefacts(self,joueurs):
        pass

    def afficherpartieGalaxie(self,mod):
        self.canevasGalaxie.delete("artefact")

        if self.parent.maselection!=None:
            joueur=mod.joueurs[self.parent.maselection[0]]
            if self.parent.maselection[1]=="etoile":
                for i in joueur.planetescontrolees:
                    if i.id == int(self.parent.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevasGalaxie.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.parent.nom].couleur,
                                                 tags=("select","marqueur"))
            elif self.parent.maselection[1]=="flotte":
                for i in joueur.flotteSystemeSolaire:
                    if i.id == int(self.parent.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10

                        self.canevasGalaxie.create_rectangle((i.x-10)-t,(i.y-10)-t,(i.x-4)+t,(i.y-4)+t,dash=(2,2),outline=mod.joueurs[self.parent.nom].couleur,
                                                 tags=("select","marqueur"))

        for i in mod.joueurs.keys():
            i=mod.joueurs[i]
            for j in i.flotteSystemeSolaire:
                if(j.espaceCourant==None):
                    if (j.nomVaisseau=="Vaisseau Canon"):
                             self.canevasGalaxie.create_image(j.x-10,j.y-10,image=self.vaisCanonG,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",None,str(j.solaire.id)))
                    elif (j.nomVaisseau=="Vaisseau Eclaireur"):
                             self.canevasGalaxie.create_image(j.x-10,j.y-10,image=self.vaisEclaireurG,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",None,str(j.solaire.id)))
                    elif (j.nomVaisseau=="Vaisseau Laser"):
                             self.canevasGalaxie.create_image(j.x-10,j.y-10,image=self.vaisLaserG,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",None,str(j.solaire.id)))
                    elif (j.nomVaisseau=="Vaisseau Sniper"):
                             self.canevasGalaxie.create_image(j.x-10,j.y-10,image=self.vaisSniperG,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",None,str(j.solaire.id)))
                    elif (j.nomVaisseau=="Vaisseau Tank"):
                             self.canevasGalaxie.create_image(j.x-10,j.y-10,image=self.vaisTankG,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact",None,str(j.solaire.id)))

                for p in j.projectile:
                        debutx,debuty=hlp.getAngledPoint(p.angle,15,p.x,p.y)
                        self.canevasGalaxie.create_line(p.x,p.y,debutx,debuty,
                                    fill="royalblue",tags=("artefact","projectile",None,None,None,None),width=3)
        for i in mod.ias:
            for j in i.flotteSystemeSolaire:
                 if(j.espaceCourant==None):
                    self.canevasGalaxie.create_rectangle(j.x-10,j.y-10,j.x-4,j.y-4,fill=i.couleur,
                                     tags=(j.proprietaire,"flotte",str(j.id),"artefact","None",str(j.solaire.id)))

        self.parent.updateInfosJoueur(mod)
# -*- coding: utf-8 -*-
from tkinter import *
import random
import os,os.path
import time



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
        self.cadreapp.grid(row=1, column=0)
        self.creercadresplash(ip,nom)
        self.creercadrelobby()
        self.changecadre(self.cadresplash)
        self.cadreoutilsgeneral=Frame(self.root)
        self.labgeneral=Label(self.cadreoutilsgeneral)
        self.labgeneral.grid(row = 1, column =0)
        self.ip=ip
        self.vueactive=None

        self.cadrepartie=Frame(self.cadreapp)
        self.cadrejeu=Frame(self.cadrepartie)
        self.cadreinfojoueur=Frame(self.cadrepartie,height=100, width=800, bg="gray",padx =50)
        self.cadreMessagerie=Frame(self.cadrepartie,height=150, width=400, bg="pink",padx =50)
        self.cadreoutils=Frame(self.cadrepartie,width=200,height=200,bg="darkgrey")
        self.cadreinfo=Frame(self.cadreoutils,width=200,height=200,bg="darkgrey")
        self.cadreBouton=Frame(self.cadreoutils,width=200,height=200,bg="medium spring green")

        self.cadreinfo.grid_propagate(False)


        self.couleurinfo="gray"
        self.couleurbouton="gray33"
        self.cadrejeu.grid(row=1, column=0)
        self.mod=None

    def changementdevue(self,evt):
        nom=evt.widget.cget("text")
        print(nom)
        self.changevueactive(self.vues[nom])

    def changevueactive(self,vue):
        if self.vueactive:
            self.vueactive.cadrespatial.grid_forget()
            self.vueactive.cadreinfo.grid_forget()
            self.cadreBouton.grid_forget()
        self.vueactive=vue
        self.vueactive.cadrespatial.grid()
        self.vueactive.cadreinfo.grid()

    def combinedactions(self):
        self.planete=self.mod.joueurs[self.nom].planetemere
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
    def changevue(self,vue):
        if self.vueactif:
            self.vueactif.grid_forget()
        self.vueactif=vue
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

    def creerCadreInfoJoueur(self,cadre,mod):
        self.cadre = cadre
        self.mod = mod

        self.labcouleur=Label(self.cadre,text="couleur:",bg=self.couleurinfo)
        self.idcouleur=Label(self.cadre, bg=self.mod.joueurs[self.nom].couleur )
        self.btndiplomatie=Button(self.cadre,text="Diplomatie",bg=self.couleurinfo)
        # ajouter text variable
        self.labcouttotal=Label(self.cadre,text="cout total:",bg=self.couleurinfo)
        self.nbcouttotal=Label(self.cadre,text="-" ,bg=self.couleurinfo)

        self.btnarbretech=Button(self.cadre,text="Arbre Technologique",bg=self.couleurinfo)

        self.labcredit=Label(self.cadre, text="credit:",bg=self.couleurinfo)
        self.nbcredit=Label(self.cadre, text=self.mod.joueurs[self.nom].credit,bg=self.couleurinfo)

        self.labnourriture= Label(self.cadre, text="nourriture:",bg=self.couleurinfo)
        self.nbnourriture=Label(self.cadre, text=self.mod.joueurs[self.nom].nourriture,bg=self.couleurinfo)

        self.labdeuterium= Label(self.cadre, text="deuterium:",bg=self.couleurinfo)
        self.nbdeuterium=Label(self.cadre, text=self.mod.joueurs[self.nom].deuterium,bg=self.couleurinfo)

        self.labmoral= Label(self.cadre, text="moral:",bg=self.couleurinfo)
        self.nbmoral=Label(self.cadre, text="-",bg=self.couleurinfo)
        # boutons et bind
        self.bgalaxie=Button(self.cadreinfojoueur,text="Galaxie",bg=self.couleurbouton)
        self.bsolaire=Button(self.cadreinfojoueur,text="Solaire",bg=self.couleurbouton)
        self.bplanete=Button(self.cadreinfojoueur,text="Planete",bg=self.couleurbouton)
        self.bsolairemere=Button(self.cadreinfojoueur,text="SolaireMere",bg=self.couleurbouton)
        # call fct to grid
        self.gridCadreInfoJoueur(self.cadre,self.mod)

    def gridCadreInfoJoueur(self,cadre,mod):
        self.cadre = cadre
        self.mod = mod

        self.labcouleur.grid(row=0,column=0)
        self.idcouleur.grid(row=0,column=1)
        self.labcouttotal.grid(row=0,column=2,)
        self.nbcouttotal.grid(row=0,column=3)
        # ajout text var
        self.labcredit.grid(row=1,column=0)
        self.nbcredit.grid(row=1,column=1)
        self.labnourriture.grid(row=1,column=2)
        self.nbnourriture.grid(row=1,column=3)
        self.labdeuterium.grid(row=1,column=4)
        self.nbdeuterium.grid(row=1,column=5)
        self.labmoral.grid(row=1,column=6)
        self.nbmoral.grid(row=1,column=7)
        # boutons
        self.btndiplomatie.grid(row=0,column=4)
        self.btnarbretech.grid(row=0,column=5)
        self.bgalaxie.grid(row = 1, column =8)
        self.bsolaire.grid(row = 1, column =9)
        self.bplanete.grid(row = 1, column =10)
        self.bsolairemere.grid(row=1,column=11)
        self.bsolairemere.config(state=NORMAL, command = lambda  : self.combinedactions() )

    def creeraffichercadrepartie(self,mod):
        self.nom=self.parent.monnom
        self.mod=mod
        self.cadreoutilsgeneral.grid()
        self.vues={"Galaxie":VueGalaxie(self.cadrejeu,self),
					"Planete":VuePlanete(self.cadrejeu,self),
					"Solaire":VueSolaire(self.cadrejeu,self)}
        self.changevueactive(self.vues["Solaire"])
        self.vueactive.cadrespatial.grid()

        self.cadreinfojoueur=Frame(self.cadrepartie,height=100, width=800, bg="gray",padx =50)
        self.cadreMessagerie=Frame(self.cadrepartie,height=100, width=400, bg="pink",padx =50)
        self.cadreinfojoueur.grid(row=0, column=0)
        self.cadreMessagerie.grid(row=0, column=1)

        # fonction création des infos joueurs
        self.creerCadreInfoJoueur(self.cadreinfojoueur,self.mod)
        # bind du bouton pour retourner a la galaxie
        self.bgalaxie.bind("<Button>",self.changementdevue)
        # cadre générale des outils
        self.cadreoutils.grid(row=1, column=1)
        # cadre des infos contextuel
        # nom et couleur du joueur : text=self.nom,fg=mod.joueurs[self.nom].couleur
        self.btncreervaisseau=Button(self.cadreinfo,text="Vaisseau",command=self.creervaisseau)
        self.btncreervaisseau.grid(row=2, column=2)
        self.lbselectecible=Label(self.cadreinfo,text="Choisir cible",bg="darkgrey")

        # cadre Messagerie

        # création des objets de Messagerie
        self.labDiplomatie=Label(self.cadreMessagerie,text="Messagerie")
        self.listeMessage=Listbox(self.cadreMessagerie)
        self.scrollMessage=Scrollbar(self.cadreMessagerie, orient=VERTICAL)
        self.entryMessage=Entry(self.cadreMessagerie)
        self.envoiMessage=Button(self.cadreMessagerie,text="Envoyer", command=self.add)



        # création du grid
        self.labDiplomatie.grid(row=0, columnspan=2, sticky=W+E)
        self.listeMessage.grid(row=1, column=0)
        self.scrollMessage.grid(row=1, column=1, sticky=N+S)
        self.entryMessage.grid(row=2, column=0)
        self.envoiMessage.grid(row=2, column=1)




        self.changecadre(self.cadrepartie)


    def add(self):
        message = self.entryMessage.get()
        reponse = message
        self.listeMessage.insert(END, str(reponse))

        #création objets échange
        #self.btnEchange=Button(self.cadreMessagerie, text="Échange")
        #self.btnConfirmer=Button(self.cadreMessagerie, text="Confirmer")
        #self.btnAnnuler=Button(self.cadreMessagerie, text="Annuler")


        #création des objets diplomatie
        #self.btnAlliance=Button(self.cadreMessagerie, text="Alliance")
        #self.btnPacteGuerre=Button(self.cadreMessagerie, text="Pacte")
        #self.btnGuerre=Button(self.cadreMessagerie, text="Guerre")
        #self.btnPaix=Button(self.cadreMessagerie, text="Paix")


    def moveCanevas(self,evt):
        x=evt.x
        y=evt.y
        px=self.mod.largeur/x/100
        py=self.mod.hauteur/y/100
        self.canevasGalaxie.xview(MOVETO,px)
        self.canevasGalaxie.yview(MOVETO,py)
        print("SCROLL",px,py)

    def afficherpartie(self,mod):
        self.vues["Galaxie"].afficherpartieGalaxie(mod)


    #def _create_circle(self, x, y, r):
        #return self.canevasSolaire.create_oval(x-r, y-r, x+r, y+r,fill="yellow",tags=("soleil"))

    #def _create_circle(self, x, y, r):
       # return self.canevasSolaire.create_oval(x-r, y-r, x+r, y+r,fill="yellow",tags=("soleil"))
        # self.afficherpartie(mod)
    def nettoyageLabelPlanete(self):
        self.vues["Planete"].planeteNom.grid_forget()
        self.vues["Planete"].planeteProprio.grid_forget()
        self.vues["Planete"].planeteTaille.grid_forget()
        self.vues["Planete"].planeteCharbon.grid_forget()
        self.vues["Planete"].planeteZinc.grid_forget()
        self.vues["Planete"].planeteDeuterium.grid_forget()
        self.vues["Planete"].planeteFertile.grid_forget()
        self.vues["Planete"].parent.cadreBouton.grid_forget()


    def creervaisseau(self):
        print("Creer vaisseau")
        self.parent.creervaisseau()
        self.maselection=None
        self.canevasGalaxie.delete("marqueur")
        self.btncreervaisseau.grid_forget()

    def CliqueVuePlanete(self,canvas,mod,SysSolaire,idPlanete):
        self.canvas = canvas
        self.mod = mod
        self.SystemeSolaire=SysSolaire
        t=self.canvas.gettags(CURRENT)
        if t:
            if self.canvas == self.vues["Planete"].canevasPlanete:

                self.vues["Planete"].afficherInfosPlanete(self.mod,int(idPlanete))
                self.cadreBouton.grid(row = 1, column= 0)
                self.vues["Solaire"].afficherSystemeSolaire(self.mod,self.SystemeSolaire.id)
                self.bsolaire.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Solaire"]) )


    def CliqueVueSySsolaire(self,canvas,mod):
        self.canvas = canvas
        self.mod = mod
        # ref : http://effbot.org/tkinterbook/canvas.htm
        # ref 2 : https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm
        t=self.canvas.gettags(CURRENT)
        if t:
            if self.canvas == self.vues["Solaire"].canevasSolaire:
                if t[1] == "planeteMere":
                    self.vues["Solaire"].afficherInfosPlanete(self.mod,int(t[2]))
                    self.vues["Planete"].afficherPlanete(self.mod,int(t[2]))
                    self.bplanete.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Planete"]) )
                    print (t[2])
                else:
                    self.vues["Solaire"].afficherInfosPlanete(self.mod,int(t[2]))
                    self.vues["Planete"].afficherPlanete(self.mod,int(t[2]))
                    self.bplanete.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Planete"]) )
                    print (t[2])
                self.mod.joueurs[self.nom].setbuffer(t[2])

            #else if self.canvas == self.vues["Solaire"].canevasSolaire:
            #    if t[1] == "vaisseau" :


    def CliqueVueGalaxie(self,canvas,mod):
        self.canvas = canvas
        self.mod = mod
        s=self.canvas.gettags(CURRENT)
        if s:
            if self.canvas == self.vues["Galaxie"].canevasGalaxie:
                if s[0] == "etoile":
                    self.vues["Galaxie"].afficherInfosSystemSolaire(self.mod,int(s[1])) # afficher infos sys solaire en passant modele et id sys solaire
                    self.vues["Solaire"].afficherSystemeSolaire(self.mod,int(s[1]))
                    self.bsolaire.config(state=ACTIVE, command = lambda  : self.changevueactive(self.vues["Solaire"]) )
                    print (s[1], self.nom)
                    self.mod.joueurs[self.nom].setbuffer(s[1])
                    #self.mod.joueurs[nom].setbuffer(s[1])


    def updateInfosJoueur(self,mod):
        self.nbnourriture.grid_forget()
        self.nbcredit.grid_forget()
        self.nbdeuterium.grid_forget()
        self.nbmoral.grid_forget()

        self.nbnourriture=Label(self.cadre, text=self.mod.joueurs[self.nom].nourriture,bg=self.couleurinfo)
        self.nbcredit=Label(self.cadre, text=self.mod.joueurs[self.nom].credit,bg=self.couleurinfo)
        self.nbnourriture=Label(self.cadre, text=self.mod.joueurs[self.nom].nourriture,bg=self.couleurinfo)
        self.nbdeuterium=Label(self.cadre, text=self.mod.joueurs[self.nom].deuterium,bg=self.couleurinfo)

        self.nbcredit.grid(row=1,column=1)
        self.nbnourriture.grid(row=1,column=3)
        self.nbdeuterium.grid(row=1,column=5)
        self.nbmoral.grid(row=1,column=7)

class VueSolaire():
    def __init__(self,fen,parent):

        print("In vue solaire")
        self.cadrejeu=fen
        self.parent=parent # vue
        self.cadrespatial=Frame(self.cadrejeu)
        self.cadreinfo=Frame(self.parent.cadreoutils)
        self.canevasSolaire=Canvas(self.cadrespatial,width=800,height=600,bg="grey11")
        # lambda de demo
        self.canevasSolaire.bind( "<Button-1>", lambda event, canvas = self.canevasSolaire : self.parent.CliqueVueSySsolaire(canvas,self.parent.modele))
        self.canevasSolaire.grid(row = 0, column =1)

        #creation des labels
        self.planeteNom=Label(self.cadreinfo)
        self.planeteProprio=Label(self.cadreinfo)
        self.planeteTaille=Label(self.cadreinfo)
        self.planeteCharbon = Label(self.cadreinfo)
        self.planeteZinc = Label(self.cadreinfo)
        self.planeteDeuterium = Label(self.cadreinfo)
        self.planeteFertile = Label(self.cadreinfo)
        self.sysSolaireNom = Label(self.cadreinfo)
        self.variationNomSysSolaire = StringVar()
        self.sysSolaireNom.grid(row = 0, column =0)

    def afficherdecorSolaire(self,mod):
        self.mod = mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire
        # self.unSysSolaire = random.choice(self.listeSysSolaire)
        self.unSysSolaire = self.listeSysSolaire[0] # TEST SYS_SOLAIRE FAIRE MEME CHOSE DANS MODELE

        self.planete= self.mod.joueurs[self.parent.nom].planetemere
        self.unSysSolaire=self.planete.parent

        for i in range(random.randrange(24, 156)):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasSolaire.create_oval(x,y,x+1,y+1,fill="white",tags=(None,"fond",None,None))
            self.canevasSolaire.config(bg="midnight blue")

        for i in range(random.randrange(10,20)):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasSolaire.create_rectangle(x,y,x+8,y+8, fill="light gray", tags=(None,"asteroide",None,None))

        self._create_circle(self.parent.largeur/1.5,self.parent.hauteur/1.5,75)
        #self.systememonetoile(self.mod)

    # def systememonetoile(self,mod):
    #     for i in self.unSysSolaire.listePlanete:
    #         t=i.taille
    #         if(i.proprietaire=="inconnu"):
    #             self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill="grey80",tags=("Inconnu","planeteInconnu",None,None))
    #         else:
    #             player = None
    #             for j in self.mod.joueurs:
    #                 if(mod.joueurs[j].nom == i.proprietaire):
    #                     player = j
    #                     self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill=mod.joueurs[player].couleur,tags=(i.proprietaire,"planeteMere",str(i.id),"possession"))

    #     #for i in mod.joueurs.keys():
        #    for j in mod.joueurs[i].planetescontrolees:
        #        t=j.taille
        #        self.canevasSolaire.create_oval(j.x-t,j.y-t,j.x+t,j.y+t,fill=mod.joueurs[i].couleur,
        #                            tags=(j.proprietaire,"planete",str(j.id),"possession"))

        self.parent.CliqueVueSySsolaire(self.canevasSolaire,mod)
    # #dessine IAs
    #     for i in mod.ias:
    #         for j in i.planetescontrolees:
    #             t=j.taille
    #             self.canevasSolaire.create_oval(j.x-t,j.y-t,j.x+t,j.y+t,fill=i.couleur,
    #                                 tags=(j.proprietaire,"planete",str(j.id),"possession"))

    #     self.parent.bindSolaire(self.canevasSolaire)

    def _create_circle(self, x, y, r):
        return self.canevasSolaire.create_oval(x-r, y-r, x+r, y+r,fill="yellow",tags=(None,"soleil",None,None))
        #self.parent.afficherpartie(mod)

    def afficherplanemetemereSolaire(self,evt):
        j=self.mod.joueurs[self.nom]
        couleur=j.couleur
        x=j.planetemere.x
        y=j.planetemere.y
        t=10
        self.canevas.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                tags=(None,"planetemere","marqueur",None))
    def afficherSystemeSolaire(self,modele,idSolaire):
        self.modele=modele
        self.id=idSolaire
        self.canevasSolaire.delete("all")
        #self.cadresolaireoutils.grid_forget()
        self.afficherdecorSolaire(self.modele)

        for a in (self.modele.Galaxie.listeSysSolaire):
            #for j in (a.listeSysSolaire):
            if (a.id == idSolaire):
                self.systemeSolaire=a
        for i in self.systemeSolaire.listePlanete:
            t=i.taille
            if(i.proprietaire=="inconnu"):
                self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill="grey80",tags=("Inconnu","planeteInconnu",str(i.id),None))
            else:
                player = None
                for k in self.mod.joueurs:
                    if(modele.joueurs[k].nom == i.proprietaire):
                        player = k
                        self.canevasSolaire.create_oval(i.x-t,i.y-t,i.x+t,i.y+t,fill=modele.joueurs[player].couleur,tags=(i.proprietaire,"planeteMere",str(i.id),"possession"))
    def afficherInfosSystemSolaire(self, modele, idSysteme):
        # self.parent.bplanete.config(state = DISABLED) # fonctionne pas

        self.modele=modele
        for i in (self.modele.Galaxie.listeSysSolaire):
            if (i.id == idSysteme):
                self.systeme=i
        self.variationNomSysSolaire.set("Nom : " + str(self.systeme.nometoile))
        self.sysSolaireNom.config(bg="white", textvariable=self.variationNomSysSolaire )



    def afficherInfosPlanete(self, modele, idPlanete):

       # self.parent.bplanete.config(state = DISABLED) # fonctionne pas
        self.modele=modele



        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j

        # string variable
        self.variationCharbon = StringVar()
        self.variationZinc = StringVar()
        self.variationDeuterium = StringVar()
        self.variationFertile = StringVar()
        # assignation des valeurs aux string variable
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
        # clear grid pour placement des labels
        #self.parent.nettoyageLabelPlanete()
        # placement des labels
        self.planeteNom.grid(row=0, column=0)
        self.planeteProprio.grid(row=1, column=0)
        self.planeteTaille.grid(row=2, column=0)
        self.planeteCharbon.grid(row=3, column=0)
        self.planeteZinc.grid(row=4, column=0)
        self.planeteDeuterium.grid(row=5, column=0)
        self.planeteFertile.grid(row=6, column=0)


class VuePlanete():
    def __init__(self,fen,parent):
        print("In vue planete")
        self.cadrejeu=fen
        self.parent=parent
        self.cadrespatial=Frame(self.cadrejeu)
        self.cadreinfo=Frame(self.parent.cadreoutils)
        self.canevasPlanete=Canvas(self.cadrespatial,width=800,height=600,bg="grey11")
        self.canevasPlanete.grid(row = 0, column =1)
        self.newStruct = Button(self.parent.cadreBouton,text="Nouvelle Structure",bg="DeepSkyBlue2" , command = lambda: self.menuStructPlanete())
        self.newStruct.grid(row = 0, column = 0,columnspan = 2)


        self.planeteNom=Label(self.cadreinfo)
        self.planeteProprio=Label(self.cadreinfo)
        self.planeteTaille=Label(self.cadreinfo)
        self.planeteCharbon = Label(self.cadreinfo)
        self.planeteZinc = Label(self.cadreinfo)
        self.planeteDeuterium = Label(self.cadreinfo)
        self.planeteFertile = Label(self.cadreinfo)

    def afficherdecorPlanete(self,mod):
        self.mod = mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire
        self.unSysSolaire = random.choice(self.listeSysSolaire)
        print("in vue decor planete")
        for i in range(random.randrange(24, 156)):
            x=random.randrange(mod.largeur)
            y=random.randrange(mod.hauteur)
            self.canevasPlanete.create_oval(x,y,x+1,y+1,fill="white",tags=("fond"))

        # affichage de la planete selectionner

        #self.canevasPlanete.create_oval(x, y, x+r, y+r,fill="green2",tags=("planeteMere"))

    def afficherInfosPlanete(self, modele, idPlanete):

       # self.parent.bplanete.config(state = DISABLED) # fonctionne pas
        self.modele=modele

        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j

        # string variable
        self.variationCharbon = StringVar()
        self.variationZinc = StringVar()
        self.variationDeuterium = StringVar()
        self.variationFertile = StringVar()
        # assignation des valeurs aux string variable
        self.variationCharbon.set("Charbon : " + str(int(self.planete.charbon)))
        self.variationZinc.set("Zinc : " + str(int(self.planete.zinc)))
        self.variationDeuterium.set("Deuterium : " + str(int(self.planete.deuterium)))
        self.variationFertile.set("Fertile : " + str(int(self.planete.fertile)))

        # création des labels
        self.planeteNom.config( bg="white", text="Id: "+ str(self.planete.id))
        self.planeteProprio.config( bg="white", text="Propriétaire: "+ self.planete.proprietaire)
        self.planeteTaille.config( bg="white", text="Taille: "+ str(self.planete.taille))
        self.planeteCharbon.config( bg="white", textvariable=self.variationCharbon )
        self.planeteZinc.config( bg="white",textvariable=self.variationZinc)
        self.planeteDeuterium.config(bg="white",textvariable=self.variationDeuterium)
        self.planeteFertile.config(bg="white",textvariable=self.variationFertile)
        # clear grid pour placement des labels
        #self.parent.nettoyageLabelPlanete()
        # placement des labels
        self.planeteNom.grid(row=0, column=0)
        self.planeteProprio.grid(row=1, column=0)
        self.planeteTaille.grid(row=2, column=0)
        self.planeteCharbon.grid(row=3, column=0)
        self.planeteZinc.grid(row=4, column=0)
        self.planeteDeuterium.grid(row=5, column=0)
        self.planeteFertile.grid(row=6, column=0)



    def afficherPlanete(self,modele,idPlanete):
        #self.parent.cadreinfo.grid_forget()
        self.modele=modele
        self.id=idPlanete
        self.canevasPlanete.delete("all")
        self.afficherdecorPlanete(self.modele)
        # self.afficherInfosPlanete(self.modele,self.id)
        self.modele=modele
        x=200
        y=100
        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j
        #planete taille
        taille=self.planete.taille*50
        print(taille)
        self.canevasPlanete.create_oval(x, y, x+taille, y+taille,fill=self.planete.couleur ,tags=("planeteMere",id))

        #self.parent.bChoixBatiement.grid(row = 6, column = 0)
        self.canevasPlanete.bind( "<Button-1>", lambda event, canvas = self.canevasPlanete : self.parent.CliqueVuePlanete(canvas,self.parent.modele,self.planete.parent,self.id))

    def menuStructPlanete(self):
        self.buttonUsineCiv = Button(self.parent.cadreBouton, text = "Usine Civile",height = 2, width = 15)#, command =self.creerStructure() )
        self.buttonUsineMili = Button(self.parent.cadreBouton, text = "Usine Militaire",height = 2, width = 15)#, command =self.creerStructure())
        self.buttonRaffDia = Button(self.parent.cadreBouton, text = "Raffinerie (Diamant)",height = 2, width = 15)#, command =self.creerStructure())
        self.buttonRaffChar = Button(self.parent.cadreBouton, text = "Raffinerie (Charbon)",height = 2, width = 15)#, command =self.creerStructure())
        self.buttonRaffIso = Button(self.parent.cadreBouton, text = "Raffinerie (Isotope)",height = 2, width = 15)#, command =self.creerStructure())
        self.buttonFerme = Button(self.parent.cadreBouton, text = "Ferme",height = 2, width = 15)#, command =self.creerStructure())
        self.buttonCapitale = Button(self.parent.cadreBouton, text = "Capitale",height = 2, width = 15)#, command =self.creerStructure())
        # bind for action
        self.buttonUsineCiv.bind("<Button>",self.creerStructure)
        self.buttonUsineMili.bind("<Button>",self.creerStructure)
        self.buttonRaffDia.bind("<Button>",self.creerStructure)
        self.buttonRaffChar.bind("<Button>",self.creerStructure)
        self.buttonRaffIso.bind("<Button>",self.creerStructure)
        self.buttonFerme.bind("<Button>",self.creerStructure)
        self.buttonCapitale.bind("<Button>",self.creerStructure)

        self.buttonUsineCiv.grid(row=1 , column = 0)
        self.buttonUsineMili.grid(row=2 , column = 0)
        self.buttonRaffDia.grid(row=1 , column = 1)
        self.buttonRaffChar.grid(row=2 , column = 1)
        self.buttonRaffIso.grid(row=3 , column = 1)
        self.buttonFerme.grid(row=3 , column = 0)
        self.buttonCapitale.grid(row=4 , column = 0, columnspan = 2)
        self.parent.cadreBouton.grid(row=1 , column = 0)

    def creerStructure(self,evt):

        nom=evt.widget.cget("text")
        self.succesful = self.modele.Planete.creerStructure(self.id,nom)

        if (self.succesful == 1):
            # ca a été ajouté correctement
            pass
        if(self.succesful == 0):
            # pas ajouté car pas de place
            pass




    def afficheEmplacement(self,idPlanete,modele):
        self.id = idPlanete
        self.modele = modele

        for i in (self.modele.Galaxie.listeSysSolaire):
            for j in (i.listePlanete):
                if (j.id == idPlanete):
                    self.planete=j

        t=20

        if self.planete.nbEmplacementDispo > 0:
            for i in self.planete.nbEmplacementDispo:
                self.x = x
                self.y = y
                self.cadrespatial.create_rectangle(self.x, self.y, self.x + t, self.y + t, fill="white")


class VueGalaxie():

    def __init__(self,fen,parent):

        print("In vue galaxie")
        self.cadrejeu=fen
        self.parent=parent
        self.cadrespatial=Frame(self.cadrejeu)
        self.cadreinfo=Frame(self.parent.cadreoutils)
        self.canevasGalaxie=Canvas(self.cadrespatial,width=800,height=600,bg="grey11")
        self.canevasGalaxie.grid(row = 0, column =0)

        # mouse click
        self.canevasGalaxie.bind( "<Button-1>", lambda event, canvas = self.canevasGalaxie : self.parent.CliqueVueGalaxie(canvas,self.parent.modele))
        self.sysSolaireNom = Label(self.cadreinfo)
        self.mod=parent.mod
        self.sysSolaireNom.grid(row = 0, column =0)

    def afficherdecorGalaxie(self,mod):
        self.mod = mod
        self.listeSysSolaire=mod.Galaxie.listeSysSolaire


        for i in self.listeSysSolaire:
            t=i.taille
            self.canevasGalaxie.create_oval(i.x-t, i.y-t,i.x+t,i.y+t,fill="grey80", tags=("etoile", str(i.id)))


        self.afficherpartieGalaxie(mod)

    def afficherInfosSystemSolaire(self, modele, idSysteme):
        # self.parent.bplanete.config(state = DISABLED) # fonctionne pas

        self.modele=modele
        for i in (self.modele.Galaxie.listeSysSolaire):
            if (i.id == idSysteme):
                self.systeme=i

        self.variationNomSysSolaire = StringVar()
        self.variationNomSysSolaire.set("Nom : " + str(self.systeme.nometoile))
        self.sysSolaireNom.config(bg="white", textvariable=self.variationNomSysSolaire )




    def afficherplanemetemereGalaxie(self,evt):
        j=self.mod.joueurs[self.parent.nom]
        couleur=j.couleur
        x=j.planetemere.x
        y=j.planetemere.y
        t=10
        self.canevasGalaxie.create_oval(x-t,y-t,x+t,y+t,dash=(3,3),width=2,outline=couleur,
                                tags=("planetemere","marqueur"))
    def cliquecosmos(self,evt):
        self.parent.btncreervaisseau.grid_forget()
        t=self.canevasGalaxie.gettags(CURRENT)
        if t and t[0]==self.parent.nom:
            #self.maselection=self.canevas.find_withtag(CURRENT)#[0]
            self.parent.maselection=[self.parent.nom,t[1],t[2]]  #self.canevas.find_withtag(CURRENT)#[0]
           # print(self.parent.maselection)
            if t[1] == "planete":
                self.montreplaneteselection()
            elif t[1] == "flotte":
                self.montreflotteselection()
        elif "planete" in t and t[0]!=self.parent.nom:
            if self.parent.maselection:
                #pass # attribuer cette planete a la cible de la flotte selectionne
                self.parent.parent.ciblerflotte(self.parent.maselection[2],t[2])
            print("Cette planete ne vous appartient pas - elle est a ",t[0])
            self.parent.maselection=None
            self.parent.lbselectecible.grid_forget()
            self.canevasGalaxie.delete("marqueur")
        else:
            print("Region inconnue")
            self.parent.maselection=None
            self.parent.lbselectecible.grid_forget()
            self.canevasGalaxie.delete("marqueur")

    def montreplaneteselection(self):
        self.parent.btncreervaisseau.grid(row=1, column=1)
    def montreflotteselection(self):
        self.parent.lbselectecible.grid(row=0, column=0)

    def afficherartefacts(self,joueurs):
        pass #print("ARTEFACTS de ",self.nom)

    def afficherpartieGalaxie(self,mod):
        self.canevasGalaxie.delete("artefact")

        if self.parent.maselection!=None:
            joueur=mod.joueurs[self.parent.maselection[0]]
            if self.parent.maselection[1]=="planete":
                for i in joueur.planetescontrolees:
                    if i.id == int(self.parent.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevasGalaxie.create_oval(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.parent.nom].couleur,
                                                 tags=("select","marqueur"))
            elif self.parent.maselection[1]=="flotte":
                for i in joueur.flotte:
                    if i.id == int(self.parent.maselection[2]):
                        x=i.x
                        y=i.y
                        t=10
                        self.canevasGalaxie.create_rectangle(x-t,y-t,x+t,y+t,dash=(2,2),outline=mod.joueurs[self.parent.nom].couleur,
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

        self.parent.updateInfosJoueur(mod)
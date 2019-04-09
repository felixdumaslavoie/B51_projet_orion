from tkinter import *

class VueSolaire():
	def __init__(self,fen):
		print("In vue solaire")
		self.root=fen
		self.cadrespatial=Frame(self.root)
		self.cadresolaireoutils=Frame(self.cadrespatial)
		self.canevassolaire=Canvas(self.cadrespatial, width=800, height=600, bg="dark red")
		self.labsolaire=Label(self.cadresolaireoutils, text="in solaire!")
		self.labsolaire.pack()
		self.canevassolaire.pack(side=LEFT)
		self.cadresolaireoutils.pack(side=LEFT)

class VuePlanete():
	def __init__(self,fen):
		print("In vue planete")
		self.root=fen
		self.cadrespatial=Frame(self.root)
		self.cadreplaneteoutils=Frame(self.cadrespatial)
		self.canevasplanete=Canvas(self.cadrespatial, width=800, height=600, bg="beige")
		self.labplanete=Label(self.cadreplaneteoutils, text="in planete!")
		self.labplanete.pack()
		self.canevasplanete.pack(side=LEFT)
		self.cadreplaneteoutils.pack(side=LEFT)

class VueGalaxie():
	def __init__(self,fen):
		print("In vue galaxie")
		self.root=fen
		self.cadrespatial=Frame(self.root)
		self.cadregalaxieoutils=Frame(self.cadrespatial)
		self.canevasgalaxie=Canvas(self.cadrespatial, width=800, height=600, bg="dark blue")
		self.labgalaxie=Label(self.cadregalaxieoutils, text="in galaxie!")
		self.labgalaxie.pack()
		self.canevasgalaxie.pack(side=LEFT)
		self.cadregalaxieoutils.pack(side=LEFT)

class Vue():
	def __init__(self):
		print("In vue")
		self.root=Tk()
		self.cadreoutilsgeneral=Frame(self.root)
		self.labgeneral=Label(self.cadreoutilsgeneral, text="menu general!")
		self.labgeneral.pack(side=LEFT)
		self.bgalaxie=Button(self.cadreoutilsgeneral,text="Galaxie")
		self.bgalaxie.bind("<Button>",self.changementdevue)
		self.bgalaxie.pack(side=LEFT)
		self.bsolaire=Button(self.cadreoutilsgeneral,text="Solaire")
		self.bsolaire.bind("<Button>",self.changementdevue)
		self.bsolaire.pack(side=LEFT)
		self.bplanete=Button(self.cadreoutilsgeneral,text="Planete")
		self.bplanete.bind("<Button>",self.changementdevue)
		self.bplanete.pack(side=LEFT)



		self.cadreoutilsgeneral.pack()
		self.vues={"Galaxie":VueGalaxie(self.root),
					"Planete":VuePlanete(self.root),
					"Solaire":VueSolaire(self.root)}
		self.vueactive=None

	def changementdevue(self,evt):
		nom=evt.widget.cget("text")
		print(nom)
		self.changevueactive(self.vues[nom])

	def changevueactive(self,vue):
		if self.vueactive:
			self.vueactive.cadrespatial.pack_forget()
		self.vueactive=vue
		self.vueactive.cadrespatial.pack()




if __name__=="__main__":
	v=Vue()
	v.root.mainloop()

from PIL import Image

def resizeVaisseau(lettre,basewidth,path):
	image= Image.open(path)
	wpercent=(basewidth/float(image.size[0]))
	hsize= int((float(image.size[1])*float(wpercent)))
	image=image.resize((basewidth,hsize),Image.ANTIALIAS)
	os.path.splitext(path)
	image.save(path+letter+".png")
	return ImageTk.PhotoImage(self.image)
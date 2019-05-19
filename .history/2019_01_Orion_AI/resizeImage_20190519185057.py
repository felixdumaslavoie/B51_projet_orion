from PIL import Image

def resizeVaisseau(basewidth,path):
	image= Image.open(path)
	wpercent=(basewidth/float(image.size[0]))
	hsize= int((float(image.size[1])*float(wpercent)))
	image=image.resize((basewidth,hsize),Image.ANTIALIAS)
	image.save('c'+path)
	return ImageTk.PhotoImage(self.image)
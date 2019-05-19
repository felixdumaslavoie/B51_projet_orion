from PIL import Image

def resizeVaisseauCanvas(basewidth,path,image):
	image= Image.
	wpercent=(basewidth/float(image.size[0]))
	hsize= int((float(image.size[1])*float(wpercent)))
	image=image.resize((basewidth,hsize),Image.ANTIALIAS)
	image.save('c'+path)
	return ImageTk.PhotoImage(self.image)
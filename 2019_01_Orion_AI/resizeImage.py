from PIL import Image, ImageTk
import os

def resizeImage(lettre,basewidth,path):

	image= Image.open(path)
	wpercent=(basewidth/float(image.size[0]))
	hsize= int((float(image.size[1])*float(wpercent)))
	image=image.resize((basewidth,hsize),Image.ANTIALIAS)
	path,extension=os.path.splitext(path)
	image.save(path+lettre+extension)
	return ImageTk.PhotoImage(image)
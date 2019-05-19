from PIL import Image

def resizeVaisseauImage(basewidth,image,path):
	wpercent=(basewidth/float(img.size[0]))
	hsize= int((float(imgage.size[1])*float(wpercent)))
	image=image.resize((basewidth.))
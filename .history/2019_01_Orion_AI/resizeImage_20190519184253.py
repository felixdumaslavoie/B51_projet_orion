from PIL import Image

def resizeVaisseauCanvas(basewidth,image,path):
	wpercent=(basewidth/float(imgage.size[0]))
	hsize= int((float(image.size[1])*float(wpercent)))
	image=image.resize((basewidth,hsize),Image.ANTIALIAS)
	#image.save('c'+path)
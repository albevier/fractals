import os
import numpy as np

from fractal_generators.mandelbrot_set import mandelbrot

def canvas(self):
	return

# for testing purposes only
def mkimg(self):
	#define grid size, in pixels per inch
	imwidth,imheight=1000,1000 #inches values
	ppi=300
	width = imwidth/ppi
	height = imheight/ppi
	#get values
	Re_c,Im_c,itr=self.set()
	#make plot. figsize takes dimensions in integer inches
	fig,ax=plt.subplots(figsize=(width, height),dpi=ppi) 
	#apply the colormap, i transposed to reorient the picture
	ax.imshow(itr.T,cmap='RdPu')
	plt.show()
	return()

if __name__=='__main__':
	setObject = mandelbrot(iterations = 250, resolution = 500)
	setObject.mkimg()

import numpy as np
from matplotlib import pyplot as plt
from numba import jit 

'''creating mandelbrot set object'''

class mandelbrot():
	def __init__(self, iterations = 250, resolution = 500): # defining the __init__ function to call later for object
		self.iterations = iterations
		self.resolution = resolution

	@jit
	def mbGenerator(self,c):
		z = 0
		i = 0
		while (i <= self.iterations) & (abs(z) < 2):
			z = z**2 + c
			i += 1
		return(i)

	def mbSet(self):
		'''Generates a mandelbrot set, along with a set containing the number of iterations per value of c '''
		Re_c=np.linspace(-2.,2., self.resolution) #generate an array for the real part
		Im_c=np.linspace(-2.,2., self.resolution) #generate an array for the imaginary part
		#initialize an array that will house the iterations for each c value calculated.
		#array size matches size(Re_c) X size(Im_c) because I make combinations
		#of an element in Re_c with every element in Im_c, and so on.

		itr=np.empty((len(Re_c),len(Im_c)))
		index = 0
		for i in range(len(Re_c)):
			for j in range(len(Im_c)): #use two for loops to mix the values of Re_c and Im_c
				itr[i,j] = self.mbGenerator(Re_c[i] + 1j*Im_c[j]) #mix the real and complex values
				index += 1
				print(index/(self.resolution**2)*100)
		return (Re_c,Im_c,itr) #return what will be the x and y values, and a z value for the colormapping

	# for testing purposes only
	def mkimg(self):
		#define grid size, in pixels per inch
		imwidth,imheight=1000,1000 #inches values
		ppi=300
		width = imwidth/ppi
		height = imheight/ppi
		#get values
		Re_c,Im_c,itr=self.mbSet()
		#make plot. figsize takes dimensions in integer inches
		fig,ax=plt.subplots(figsize=(width, height),dpi=ppi) 
		#apply the colormap, i transposed to reorient the picture
		ax.imshow(itr.T,cmap='RdPu')
		plt.show()
		return()


if __name__=='__main__':
	setObject = mandelbrot(iterations = 250, resolution = 500)
	setObject.make_img()

	





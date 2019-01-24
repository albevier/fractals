#
#
#Problem 4
#
#
import numpy as np
from matplotlib import pyplot as plt
# Learned about this @jit decorator while reading about computation of mandelbrot sets. 
# the decorated function is compiled using numba, which improves calculation
# speed for numpy-like operations, sometimes by factors of 100 or more!
from numba import jit 

@jit
def mandel_calc(c):
	'''Determines if a complex number is in the mandelbrot set over 250 iterations.'''
	z=c #seed the sequence with z, this is z1 in the sequence
	for n in range(250): #set max number of iterations to 250
		if abs(z)>2:  #set some threshold for the z values. i'll choose cmin and cmax<2 later
			return(n) 
		z=z**2+c #generate next iteration
	return(0) #if iteration 250 reached, then treat this value of c as convergent

@jit
def mandel_set(rcmin,rcmax,icmin,icmax,rstep,istep):
	'''Generates a mandelbrot set, along with a set containing the number of iterations per
	value of c'''
	#generate values of c to test.
	Re_c=np.linspace(rcmin,rcmax, rstep) #generate an array for the real part
	Im_c=np.linspace(icmin,icmax,istep) #generate an array for the imaginary part
	#initialize an array that will house the iterations for each c value calculated.
	#array size matches size(Re_c) X size(Im_c) because I make combinations
	#of an element in Re_c with every element in Im_c, and so on.
	iterations=np.empty((rstep,istep))
	for i in range(rstep):
		for j in range(istep): #use two for loops to mix the values of Re_c and Im_c
			iterations[i,j] = mandel_calc(Re_c[i] + 1j*Im_c[j]) #mix the real and complex values
	return (Re_c,Im_c,iterations) #return what will be the x and y values, and a z value for the colormapping

def make_img(rcmin,rcmax,icmin,icmax):
	#define grid size, in pixels per inch
	imwidth,imheight=1000,1000 #inches values
	ppi=1000
	width = imwidth/ppi
	height = imheight/ppi
	#get values
	Re_c,Im_c,itr=self.mandel_set(rcmin,rcmax,icmin,icmax,imwidth,imheight)
	#make plot. figsize takes dimensions in integer inches
	fig,ax=plt.subplots(figsize=(width, height),dpi=ppi) 
	ax.set_title('Mandelbrot')
	#apply the colormap, i transposed to reorient the picture
	ax.imshow(itr.T,cmap='RdPu')
	plt.show()

if __name__=='__main__':

	#I make the mandelbrot image zoomed into an experimental region ... spirally
	make_img(-1,0,-0.5,0.5)






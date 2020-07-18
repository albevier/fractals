import numpy as np

from tqdm import tqdm
from matplotlib import pyplot as plt

'''creating mandelbrot set object'''

class mandelbrot():
	def __init__(self, iterations = 250, resolution = 500): # defining the __init__ function to call later for object
		self.iterations = iterations
		self.resolution = resolution

	def generator(self,c):
		z = 0
		i = 0
		while (i <= self.iterations) & (abs(z) < 2):
			z = z**2 + c
			i += 1
		return(i)

	def set(self):
		'''Generates a mandelbrot set, along with a set containing the number of iterations per value of c '''
		Re_c=np.linspace(-2.,2., self.resolution) #generate an array for the real part
		Im_c=np.linspace(-2.,2., self.resolution) #generate an array for the imaginary part
		#initialize an array that will house the iterations for each c value calculated.
		#array size matches size(Re_c) X size(Im_c) because I make combinations
		#of an element in Re_c with every element in Im_c, and so on.

		itr=np.empty((len(Re_c),len(Im_c)))
		index = 0
		for i in tqdm(range(len(Re_c))):
			for j in range(len(Im_c)): #use two for loops to mix the values of Re_c and Im_c
				itr[i,j] = self.generator(Re_c[i] + 1j*Im_c[j]) #mix the real and complex values
				index += 1
		return (Re_c,Im_c,itr) #return what will be the x and y values, and a z value for the colormapping

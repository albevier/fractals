import numpy as np

'''creating mandelbrot set object'''
class mandelbrot(object):
	def __init__(self, iterations = 32, zoom = 0, zoomPoint = 0): # defining the __init__ function to call later for object
		self.iterations = iterations
		self.zoom = zoom
		self.zoomPoint = zoomPoint


	def mandelbrot_generator(self,iterations,zoomPoint, c):
		z = zoomPoint
		i = 0
		while i < iterations & abs(z) < 2
			z = z*z + c
			i += 1
			return i

if __name__=='__main__':





import numpy as np

'''creating mandelbrot set object'''
class mandelbrot(object):
	def __init__(self, iterations=32, zoom=0): # defining the __init__ function to call later for object
		self.iterations = iterations
		self.zoom = zoom
		self.zoomPoint = zoomPoint


	def generator(points):
		plane_x = 200 # size of the real axis
		plane_y = 200 # size of the imaginary axis
		set = np.array(plane_x,plane_y)



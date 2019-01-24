import time
import os
from mandelbrot_set import mandelbrot
from dev import ArrayToImage

if __name__=='__main__':
	# creating instances of the mandelbrot set class and Array to image converter class
	obj = mandelbrot(resolution=500)
	mandelbrot = obj.mbSet()
	converter = ArrayToImage(cm='fiery')
	converter.array_convert(array=mandelbrot)
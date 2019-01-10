import os
import time
import numpy as np
import subprocess as subp
import scipy.misc

class ArrayToImage(object):
	def __init__(self,cm='gray'):
		"""
		:param cm: Sets global colormap from presets stored in self.colordict.
		:return: Setup base parameters and frame cache.
		"""
		self.cm = cm
		self.colordict = {'fiery':[1/3,150,1,0,1/6,0],'blue':[1/6,0,0,20,1,0],'xmas':[-1/1.5,160,1,0,0.2,0],'70s':[.5,255/2,-1,255,-1,255],'gray':[1,0,1,0,1,0],'teal':[0,0,1,0,1,0],'poison':[1,0,0,30,0,200],'misc':[-1/1.5,150,1,0,0.5,70]}
		self.counter = 0 
		self.cwd = os.getcwd()
		ls_out = subp.check_output(['ls']).decode('utf-8')
		directories = ls_out.splitlines()
		if 'Frames' not in directories:
			os.system('mkdir Frames')
			self.save_path = self.cwd + '/Frames'
		else:	
			for i in range(1000): #this is very basic mechanism, should be improved
				frame_loc = 'Frames_{}'.format(i)
				if frame_loc not in directories:
					os.system('mkdir {}'.format(frame_loc))
					self.save_path = os.getcwd() + '/' + frame_loc
					break
		print(' :: Frame cache initialized in {} :: '.format(self.save_path))

	def array_convert(self,array = np.array([[0,1] ,[0,1]]),color_map=[1,0,1,0,1,0],manual_grad=True):
		"""
		    :param array: The rectangular numpy array containing colorvalues to be transformed into a png.
		    :param color_map: Seed for manual colormap of each generated image.
		    :param manual_grad: Enable or disable global colormap.
		    :return: Returns indexed .png file stored in cache location.
		"""

		scipy.misc.toimage(array, cmin = 0.0, cmax = 1.0,mode = 'L', pal = self.paint(color_map = color_map,manual = manual_grad)).save(self.save_path + '/frame{}.png'.format(self.counter))
		self.counter+=1
 	
	def paint(self, manual=False,color_map=[1,0,1,0,1,0]):
		"""
			:param manual: Enable use of manual colormaps, to be specified for each conversion.
			:param color_map: Seed for manual colormap to be used in conversion.
			:return: Generates an (n,3) numpy array with the pal colormap values to be used in scipy.misc.toimage. Defaults are stored in self.colordict.
		"""
		if manual:
			m1, b1, m2, b2, m3, b3 = color_map
			triplet = [[0,0,0]]
			for i in range(1,255):
				triplet.append([m1*i+b1 , m2*i+b2 , m3*i+b3])
			return(triplet)
		else:
			try:
				self.cm = str(self.cm)
				assert self.cm in self.colordict
			except Exception:
				print('''Invalid colormap, available choices: \n \n {}'''.format(self.colordict))
			else:
				m1, b1, m2, b2, m3, b3 = self.colordict[self.cm]
				triplet = [[0,0,0]]
				for i in range(1,255):
					triplet.append([m1*i+b1 , m2*i+b2 , m3*i+b3])
				return(triplet)

	def cache_list(self):
		"""
			Searches for and lists Frame caches.
		"""
		ls_out = subp.check_output(['ls']).decode('utf-8')
		directories = ls_out.splitlines()
		rm_list = []
		if 'Frames' in directories:
			rm_list = ['Frames']
		for i in range(1000):
			frame_loc = 'Frames_{}'.format(i)
			if frame_loc in directories:
				rm_list.append(frame_loc)
		return(rm_list)

	def cleanup(self):
		"""
			Removes Frame Caches, useful for debugging.
		"""
		rm_list = self.cache_list()
		if len(rm_list)!=0:
			subp.check_output(['rm','-R']+rm_list)
			print(' :: Removed Frame Caches ::')
			return(1)
		else:
			print(' :: No Cache Found ::')
			return(0)

if __name__ == '__main__':
	# Some demo here. Grayscale only at the moment. (1/8/19)
	randarray = np.array([[0,0,0,0,0],[0,1,1,1,0],[0,1,0.5,1,0],[0,1,1,1,0],[0,0,0,0,0]])
	randarray2 = np.random.uniform(0,1,1000000).reshape((1000,1000))
	randarray3 = 1/(1000000)*np.arange(1000000).reshape(2000,500)
	converter = ArrayToImage(cm='fiery')
	converter.array_convert(array=randarray)
	converter.array_convert(array=randarray2)
	converter.array_convert(array=randarray3)
	print('Check {} for images'.format(converter.save_path))
	input(' :: Press <Enter> to Remove Cache :: ')
	converter.cleanup()
	


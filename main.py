# import pygame
# import numpy

class camera:
	def __init__(self, optimized, distance):
		self.optimized = optimized
		self.distance = distance
	    
	def move(self, axis, lerp, jumps):
		self.axis = axis
		self.lerp = lerp
		self.jumps = jumps
		
	def rotate(self, axis, lerp, look):
		self.axis = axis
		self.lerp = lerp
		self.look = look
		
if __name__ == "__main__":
	camera(0, 512).run()
	print("lol")
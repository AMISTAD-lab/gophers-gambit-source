from classCell import *
from typeCell import *
from classBoard import *

class Terrain(Board):
	def __init__(self, rowLength, colLength, trapList=[]):
		self.trapList = trapList
		self.existingTraps = []
		super().__init__(rowLength, colLength)
		self.board = super().emptyBoard(rowLength, colLength) #make dirt
		self.board = super().saveCells() #get info version of dirt
		self.addTraps(trapList) #add info version of traps to board

	def addTraps(self, trapList):
		"""trapList = [(trapboard, start_x, start_y)...]"""
		for trapTuple in trapList:
			if noOverlaps(trapTuple, self.existingTraps):
				trapboard, start_x, start_y = trapTuple
				self.board = alg.addTrapToTerrain(self.board, start_x, start_y, trapboard)
				self.existingTraps.append([(start_x, start_x + len(trapboard[0]) - 1), (start_y, start_y + len(trapboard) - 1)])
			else:
				raise Exception("A trap could not be added because of overlap")		

def overlap(trapTuple, otherTrapBounds):
	trapboard, start_x, start_y = trapTuple
	(x_min, x_max), (y_min, y_max) = otherTrapBounds
	rowLength = len(trapboard[0])
	colLength = len(trapboard)
    #coordinates of top-right corner of this rectangle
	rowEnd = start_x + rowLength
	colEnd = start_y + colLength
		
	xOverlap = False
	yOverlap = False
		
	#determine if overlapping in X direction
	if ((rowEnd <= x_max and rowEnd >= x_min) or (start_x <= x_max and start_x >= x_min)):
		xOverlap = True
		
	#determine if overlapping in Y direction
	if ((colEnd <= y_max and colEnd >= y_min) or (start_y <= y_max and start_y >= y_min)):
		yOverlap = True
		
	#if overlapping in both X and Y, then the rectangles are overlapping
	if (xOverlap and yOverlap):
		return True
	else:
		return False

def noOverlaps(trapTuple, existingTraps):
	for oldTrap in existingTraps:
		if overlap(trapTuple, oldTrap):
			return False
	return True

		
		    
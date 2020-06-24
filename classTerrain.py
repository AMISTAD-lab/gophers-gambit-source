from classCell import *
from typeCell import *
from classBoard import *

class Terrain(Board):
	def __init__(self, rowLength, colLength, trapList=[]):
		self.trapList = trapList
		self.existingTraps = []
		super().__init__(rowLength, colLength)
		self.board = super().emptyBoard(rowLength, colLength)
		self.addTraps(trapList)

	def addTraps(self, trapList):
		"""[[(xmin, xmax), (ymin, ymax)], ...]"""
		for trapTuple in trapList:
			if noOverlaps(trapTuple, self.existingTraps):
				trap, start_x, start_y, rotationType = trapTuple
				#rotate trap (WRITE A METHOD that takes in the type and calls left, right, up from the board class)
				super().addBoard(start_x, start_y, trap)
				self.existingTraps.append([(start_x, start_x + trap.rowLength - 1), (start_y, start_y + trap.colLength - 1)])
			else:
				print("A trap could not be added because of overlap")		

def overlap(trapTuple, otherTrapBounds):
	trap, start_x, start_y, rotationType = trapTuple
	(x_min, x_max), (y_min, y_max) = otherTrapBounds
	#rotate and check (DONT FORGET, need to make sure rotated version fits, not original)

    #coordinates of top-right corner of this rectangle
	rowEnd = start_x + trap.rowLength
	colEnd = start_y + trap.colLength
		
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

		
		    
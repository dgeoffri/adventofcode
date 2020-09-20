#!/usr/bin/env python

class LCDScreen(object):
	def __init__(self):
		self.LCD = [ [0] * 50  for x in range(6) ] 

	def dispatch_instruction(self, instruction):
		tokens = instruction.split()
		if tokens[0] == "rect":
			x, y = map(int, tokens[1].split("x"))
			self.rect((x,y))
		elif tokens[0] == "rotate":
			if tokens[1] == "row":
				rowinst = tokens[2].split("=")
				if rowinst[0] != "y":
					print "Bad instruction! no y where expected: %s" % instruction
					return
				if tokens[3] != "by":
					print "Bad instruction! no \"by\" where expected: %s" % tokens
					return
				row = int(rowinst[1])
				amount = int(tokens[4])
				self.rotate_row(row, amount)
			elif tokens[1] == "column":
				colinst = tokens[2].split("=")
				if colinst[0] != "x":
					print "Bad instruction! no x where expected: %s" % instruction
					return
				if tokens[3] != "by":
					print "Bad instruction! no \"by\" where expected: %s" %instruction
					return
				col = int(colinst[1])
				amount = int(tokens[4])
				self.rotate_column(col, amount)
			else:
				print "Bad instruction! Expect \"row\" or \"column\" for rotate instruction: %s" % instruction
		else:
			print "Bad instruction! Expected \"rect\" or \"rotate\" as main instruction: %s" % instruction

	def rect(self, area):
		# print "Doing rect for area %s" % str(area)
		x, y = area
		for i in range(y):
			for j in range(x):
				self.LCD[i][j] = 1

	def rotate_column(self, column, amount):
		# print "Doing rotate of column %d by %d places" % (column, amount)
		for i in range(amount):
			temp = self.LCD[len(self.LCD) - 1][column]
			for y in range(len(self.LCD) - 1, 0, -1):
				self.LCD[y][column] = self.LCD[y-1][column]
			self.LCD[0][column] = temp

	def rotate_row(self, row, amount):
		# print "Doing rotate of row %d by %d places" % (row, amount)
		for i in range(amount):
			self.LCD[row].insert(0, self.LCD[row].pop())

	def display(self):
		for row in self.LCD:
			rowtoprint = ''.join(map(str,row)).replace('0', ' ').replace('1', 'X')
			print rowtoprint

	def get_lit_pixel_count(self):
		return sum(sum(row) for row in self.LCD) 

if __name__ == "__main__":
	LCD = LCDScreen()
	with open("day08.txt", "r") as inputfile:
		for line in inputfile:
			LCD.dispatch_instruction(line.rstrip())
			# LCD.display()
	print "There are %d pixels lit on the display" % LCD.get_lit_pixel_count()
	LCD.display()

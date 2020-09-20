#!/usr/bin/env python

class person(object):

	def __init__(self):
		self.location = (0, 0)
		self.directions = [(1,0), (0,1), (-1,0), (0,-1)]
		self.facing = 0

	def execute_step(self, instruction):
		if instruction[0] == 'R':
			self.facing = (self.facing + 1) % 4
		elif instruction[0] == 'L':
			self.facing = (self.facing - 1) % 4

		distance = int(instruction[1:])

		x = self.location[0] + self.directions[self.facing][0] * distance
		y = self.location[1] + self.directions[self.facing][1] * distance

		self.location = (x, y)

		return self.location

	def execute_steps(self, instructions):
		for instruction in instructions.split(", "):
			location = self.execute_step(instruction)
		return location

if __name__ == "__main__":
	with open("day01.txt", "r") as inputfile:
		p = person()
		location = p.execute_steps(inputfile.read())
		print "You are %d steps away from the HQ." % (abs (location[0]) + abs (location[1]))


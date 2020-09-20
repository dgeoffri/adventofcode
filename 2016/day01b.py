#!/usr/bin/env python

class person(object):

	def __init__(self):
		self.location = (0, 0)
		self.directions = [(1,0), (0,1), (-1,0), (0,-1)]
		self.facing = 0
		self.visited = []
		self.atHQ = False

	def execute_step(self, instruction):
		if self.atHQ:
			return self.location

		if instruction[0] == 'R':
			self.facing = (self.facing + 1) % 4
		elif instruction[0] == 'L':
			self.facing = (self.facing - 1) % 4

		distance = int(instruction[1:])

		for step in range(distance):
			self.visited.append(self.location)
			x = self.location[0] + self.directions[self.facing][0]
			y = self.location[1] + self.directions[self.facing][1]
			self.location = (x, y)

			if self.location in self.visited:
				self.atHQ = True
				break

		return self.location

	def execute_steps(self, instructions):
		for instruction in instructions.split(", "):
			location = self.execute_step(instruction)
		return location

if __name__ == "__main__":
	with open("day1.txt") as instruction_file:
		p = person()
		location = p.execute_steps(instruction_file.read())
		print "You are %d steps away from the HQ." % (abs (location[0]) + abs (location[1]))


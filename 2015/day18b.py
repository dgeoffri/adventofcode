#!/usr/bin/env python
import array

def sticklights(lightarray):
	# Stick corner lights on
	for y, x in [(0,0), (len(lightarray[0])-1, 0), (0, len(lightarray)-1), (len(lightarray[len(lightarray)-1])-1, len(lightarray)-1)]:
		lightarray[y][x] = 1

def animate(lightarray):
	newlightarray = [array.array('B', (0 for x in xrange(len(lightarray[y])))) for y in xrange(len(lightarray))]
	for y in xrange(len(lightarray)):
		for x in xrange(len(lightarray[y])):
			thelightitself = lightarray[y][x]
			neighbors = 0
			for neighboring_y in xrange(-1 if y>0 else 0, 2 if y<len(lightarray)-1 else 1):
				for neighboring_x in xrange(-1 if x>0 else 0, 2 if x<len(lightarray[y])-1 else 1):
					if (neighboring_y==0) and (neighboring_x==0):
						continue
					else:
						neighbors += lightarray[y+neighboring_y][x+neighboring_x]
			# print "Position: ({}, {}): the light is {}.  {} of its neighbors are on.".format(x, y, 'on' if thelightitself else 'off', neighbors)
			if thelightitself:
				newlightarray[y][x] = 1 if (neighbors>=2) and (neighbors<=3) else 0
			else:
				newlightarray[y][x] = 1 if (neighbors==3) else 0
	sticklights(newlightarray)
	return newlightarray

def displaylights(lightarray):
	for line in lightarray:
		print ''.join(map(lambda x: '#' if x else '.', line))
	print

def main():
	with open('day18.txt', 'r') as inputfile:
		lightarray=[array.array('B', list(map(lambda x: 1 if x=='#' else 0, line.rstrip()))) for line in inputfile]
	sticklights(lightarray)
	displaylights(lightarray)
	iterations = 100
	for _ in xrange(iterations):
		lightarray = animate(lightarray)
		displaylights(lightarray)
	print "{} lights are lit at the end of {} animation iterations.".format(sum(map(sum, lightarray)), iterations)
	
if __name__=='__main__':
	main()
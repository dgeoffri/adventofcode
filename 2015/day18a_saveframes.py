#!/usr/bin/env python
import array, textwrap

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
	return newlightarray

def displaylights(lightarray):
	for line in lightarray:
		print ''.join(map(lambda x: '#' if x else '.', line))
	print

def savelightstopbm(lightarray, framenum=0):
	with open('day18a_frame%05d.pgm'%framenum, 'wb') as f:
		yres = len(lightarray)
		xres = len(lightarray[0])
		f.write('P2\n{} {}\n1\n'.format(xres, yres))
		for y in xrange(yres):
			f.write('\n'.join(textwrap.wrap(' '.join(map(str, lightarray[y])), width=70))+'\n')

def main():
	with open('day18.txt', 'r') as inputfile:
		lightarray=[array.array('B', list(map(lambda x: 1 if x=='#' else 0, line.rstrip()))) for line in inputfile]
	# displaylights(lightarray)
	savelightstopbm(lightarray)
	iterations = 2048
	for frame in xrange(iterations):
		lightarray = animate(lightarray)
		displaylights(lightarray)
		savelightstopbm(lightarray, frame+1)
	print "{} lights are lit at the end of {} animation iterations.".format(sum(map(sum, lightarray)), iterations)
	
if __name__=='__main__':
	main()

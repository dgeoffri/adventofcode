#!/usr/bin/env python
# coding: utf-8
import re

regex=re.compile(r"Step (\D) must be finished before step (\D) can begin.")
steps=open('day7.txt','r').read().splitlines()
tt=[regex.match(f).groups() for f in steps]

prereqs={}
for i in map(lambda x: chr(x), range(ord("A"), ord("Z")+1)):
	prereqs[i] = ""

for step, prereq in tt:
    	# if prereq not in prereqs:
        #	prereqs[prereq] = step
        # else:
            	prereqs[prereq] += step

print prereqs
            
done=[]
workers=[('.', 0)]*5
clock=0

# readytogo = ''.join([t for t in map(lambda x: chr(x), range(ord("A"), ord("Z")+1)) if t not in prereqs])

# print "Executing step", readytogo, "as it has no prerequisites"

# done.append(readytogo)
# print done

def findfreeworker(workers):
	for x in xrange(len(workers)):
		if workers[x][0]=='.':
			return x

def allworkersdone(workers):
	for x in xrange(len(workers)):
		if workers[x][0] != ".":
			if workers[x][1] >= 0:
				break
	else:
		return True

while prereqs or not allworkersdone(workers):
	for step in sorted(prereqs.keys()):
		ready = True
		for prereq in prereqs[step]:
			if prereq not in done:
				ready = False
				break
		if ready:
			x=findfreeworker(workers)
			if x is not None:
				print "Assigning step " + step + " to worker", x, "as prerequisite(s) " + prereqs[step] + " is/are all complete and it is alphabetically next in line."
				workers[x] = (step, 60+(ord(step)-ord('A')))
				del prereqs[step]
				break
	else:
		print "   clock =", clock, workers
		clock += 1
		for x in xrange(len(workers)):
			if workers[x][0] != ".":
				if workers[x][1] > 0:
					workers[x] = (workers[x][0], workers[x][1]-1)
				else:
					done.append(workers[x][0])
					workers[x] = ('.', 0)

print "Steps taken: " + ''.join(done)
print "Seconds taken:", clock

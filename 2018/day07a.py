#!/usr/bin/env python
# coding: utf-8
import re

regex=re.compile(r"Step (\D) must be finished before step (\D) can begin.")
steps=open('day07.txt','r').read().splitlines()
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

# readytogo = ''.join([t for t in map(lambda x: chr(x), range(ord("A"), ord("Z")+1)) if t not in prereqs])

# print "Executing step", readytogo, "as it has no prerequisites"

# done.append(readytogo)
# print done

while prereqs:
	for step in sorted(prereqs.keys()):
		ready = True
		for prereq in prereqs[step]:
			if prereq not in done:
				ready = False
				break
		if ready:
			print "Executing step", step, "as prerequisite(s)", prereqs[step], "is/are all complete and it is alphabetically next in line."
			del prereqs[step]
			done.append(step)
			break

print "Steps taken: " + ''.join(done)

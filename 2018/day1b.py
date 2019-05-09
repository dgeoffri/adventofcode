#!/usr/bin/env python

ifile=open("day1a.txt")
sum=0
seen=[]
done=False
while not done:
	ifile.seek(0)
	for line in ifile:
		sum += int(line)
		#// print sum
		if sum in seen:
			print ("Seen %d twice!")%sum
			done=True
			break
		seen.append(sum)




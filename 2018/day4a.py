#!/usr/bin/env python

import numpy, collections, re

logregex = re.compile(r'\[(\d+)-(\d+)-(\d+) (\d+):(\d+)\] (.*)')
with open("day4.txt", "r") as f:
	filedata = f.read().splitlines()
	data = sorted(map(lambda x: logregex.match(x).groups(), filedata))
	del filedata

# Data look like:
# (YYYY, MM, DD, HH, MM, Event)
days = {}
guardregex = re.compile(r'Guard #(\d+) begins shift')
guardletters = {}
currentletter = 'A'
guardonduty = 0
# newday = False
lastfellasleepmin = 0
for event in data:
	# print event
	if event[5].endswith("begins shift"):
		# newday = True
		guardonduty = guardregex.match(event[5]).groups()[0]
		# print "Guard on duty  = " + str(guardonduty)
		if guardonduty not in guardletters:
			# print "Adding guard #%s as legend %s" % (guardonduty, currentletter)
			guardletters[guardonduty] = currentletter
			currentletter = chr(ord(currentletter)+1)
			# print guardletters
	elif event[5] == "falls asleep":
		if (event[0], event[1], event[2]) not in days: # use a tuple of y, m, d as a key
			days[(event[0], event[1], event[2])] = numpy.array(['.']*60)  # make a new empty daylog
		lastfellasleepmin = event[4]
	elif event[5] == "wakes up":
		days[(event[0], event[1], event[2])][int(lastfellasleepmin):int(event[4])] = guardletters[guardonduty]
	else:
		print "Unrecognized event in log"

guardsleepcount = {guard: 0 for guard in guardletters.values()}
for day in sorted(days):
	schedule = days[day]
	print day, "-", ''.join(schedule)
	guardstoday = collections.Counter(schedule)
	# print guardstoday
	del guardstoday['.']
	for guard in guardstoday:
		guardsleepcount[guard] += guardstoday[guard]
print "Guard # (Letter)    Minutes slept"
guardnumbers = { n: l for l, n in guardletters.items() }
for guard in sorted(guardsleepcount.items(), key=lambda kv: kv[1]):
	print "%-6d %-8s    %d" % (int(guardnumbers[guard[0]]), guard[0], guard[1])

for minute in range(60):
	osleptthisminute = 0
	for day in days:
		schedule = days[day]
		if schedule[minute] == 'O':
			 osleptthisminute += 1
	print "O slept " + str(osleptthisminute) + " days at " + str(minute)

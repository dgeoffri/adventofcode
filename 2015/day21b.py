#!/usr/bin/env python

import itertools

MY_HP = 100

ITEMS = { 'Dagger': 	{'Cost': 8,   'Damage': 4, 'Armor': 0},
		  'Shortsword': {'Cost': 10,  'Damage': 5, 'Armor': 0},
		  'Warhammer': 	{'Cost': 25,  'Damage': 6, 'Armor': 0},
		  'Longsword': 	{'Cost': 40,  'Damage': 7, 'Armor': 0},
		  'Greataxe': 	{'Cost': 74,  'Damage': 8, 'Armor': 0},
		  'Leather': 	{'Cost': 13,  'Damage': 0, 'Armor': 1},
		  'Chainmail': 	{'Cost': 31,  'Damage': 0, 'Armor': 2},
		  'Splintmail': {'Cost': 53,  'Damage': 0, 'Armor': 3},
		  'Bandedmail': {'Cost': 75,  'Damage': 0, 'Armor': 4},
		  'Platemail': 	{'Cost': 102, 'Damage': 0, 'Armor': 5},
		  'No Armor': 	{'Cost': 0,   'Damage': 0, 'Armor': 0},
		  'Damage +1': 	{'Cost': 25,  'Damage': 1, 'Armor': 0},
		  'Damage +2': 	{'Cost': 50,  'Damage': 2, 'Armor': 0},
		  'Damage +3': 	{'Cost': 100, 'Damage': 3, 'Armor': 0},
		  'Defense +1': {'Cost': 20,  'Damage': 0, 'Armor': 1},
		  'Defense +2': {'Cost': 40,  'Damage': 0, 'Armor': 2},
		  'Defense +3': {'Cost': 80,  'Damage': 0, 'Armor': 3},
		  'Karate 1':   {'Cost': 0,   'Damage': 0, 'Armor': 0},
		  'Karate 2':   {'Cost': 0,   'Damage': 0, 'Armor': 0} }

WEAPONS = {weapon: ITEMS[weapon] for weapon in ('Dagger', 'Shortsword', 'Warhammer', 'Longsword', 'Greataxe')}
ARMOR = {armor: ITEMS[armor] for armor in ('Leather', 'Chainmail', 'Splintmail', 'Bandedmail', 'Platemail', 'No Armor')}
RINGS = {armor: ITEMS[armor] for armor in ('Damage +1', 'Damage +2', 'Damage +3', 'Defense +1', 'Defense +2', 'Defense +3', 'Karate 1', 'Karate 2')}

print "Weapons:"
print WEAPONS
print "Armor:"
print ARMOR
print "Rings:"
print RINGS

def iterate_build():
	for ringcombo in itertools.combinations(RINGS, 2):
		for armor in ARMOR:
			for weapon in WEAPONS:
				ring1, ring2 = ringcombo
				yield weapon, armor, ring1, ring2

def stats_from_build(build):
	return {item_property: sum(ITEMS[item][item_property] for item in build) for item_property in ITEMS[build[0]].keys()}

def fight_to_the_death(build_stats, boss_stats):
	currentplayer, opposition = ( 'Me', 'Boss' )
	hitpoints = { 'Boss': boss_stats['Hit Points'], 'Me': MY_HP }
	stats = { 'Boss': {'Damage': boss_stats['Damage'], 'Armor': boss_stats['Armor']}, 'Me': build_stats }
	
	while (hitpoints[currentplayer] > 0) and (hitpoints[opposition] > 0):
		hitpoints[opposition] -= (stats[currentplayer]['Damage'] - stats[opposition]['Armor'])
		currentplayer, opposition = opposition, currentplayer

	# print "A legend has died!"
	# print "%s - hitpoints: %d" % (currentplayer, hitpoints[currentplayer])
	# print "%s - hitpoints: %d" % (opposition, hitpoints[opposition])
	
	return opposition

def main():
	boss_stats = dict()
	with open('day21.txt') as inputfile:
		for line in inputfile:
			prop, val = line.rstrip().split(': ')
			boss_stats[prop] = int(val)

	most_expensive_win = 0
	for build in iterate_build():
		build_stats = stats_from_build(build)
		winner = fight_to_the_death(build_stats, boss_stats)
		if (winner == 'Boss') and (build_stats['Cost'] > most_expensive_win):
			most_expensive_win = build_stats['Cost']
			print "New most expensive win found: " + repr(build)
			print " Cost: " + str(most_expensive_win)
	print "The absolute most expensive win cost " + str(most_expensive_win)

if __name__ == '__main__':
	main()

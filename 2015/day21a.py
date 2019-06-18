#!/usr/bin/env python

import itertools

BOSS_HP = 103
BOSS_DAMAGE = 9
BOSS_ARMOR = 2

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

def fight_to_the_death(build_stats):
	pass


if __name__ == '__main__':
	pass
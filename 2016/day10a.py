#!/usr/bin/env python

class Bot(object):
	def __init__(self):
		self.chips = []
	def give(self, chip):
		if len(self.chips) >= 2:
			raise Exception("Bot already has 2 chips")
		else:
			self.chips.append(chip)
	def get_chips(self):
		if len(self.chips) != 2:
			raise Exception("Tried to get chip pair when bot does not hold 2 chips")
		else:
			chips = sorted(self.chips)
			self.chips = []
			return chips
	def is_ready(self):
		return len(self.chips) == 2
	def __repr__(self):
		return str(sorted(self.chips))

def complete_instruction(instruction, bots, outputs):
	tokens = instruction.split()
	if tokens[0] == "value":
		if len(tokens) != 6 or\
			(tokens[2], tokens[3], tokens[4]) != ("goes", "to", "bot") or\
			not tokens[1].isdigit() or\
			not tokens[5].isdigit():
			raise Exception("Malformed value instruction")
		value = int(tokens[1])
		bot = int(tokens[5])		
		if not bot in bots:
			bots[bot] = Bot()
		bots[bot].give(value)
		return True
	elif tokens[0] == "bot":
		if len(tokens) != 12 or\
			(tokens[2], tokens[3], tokens[4], tokens[7], tokens[8], tokens[9]) != ("gives", "low", "to", "and", "high", "to") or\
			((tokens[5] != "bot") and (tokens[5] != "output")) or\
			((tokens[10] != "bot") and (tokens[10] != "output")) or\
			not tokens[1].isdigit() or\
			not tokens[6].isdigit() or\
			not tokens[11].isdigit():
			raise Exception("Malformed bot instruction")
		bot = int(tokens[1])
		low_target_type = tokens[5]
		low_target_dest = int(tokens[6])
		high_target_type = tokens[10]
		high_target_dest = int(tokens[11])
		if not bot in bots or not bots[bot].is_ready():
			return False
		else:
			low_chip, high_chip = bots[bot].get_chips()
			if (low_chip, high_chip) == (17, 61):
				print "Bot %d just compared value-61 microchips with value-17 microchips" % bot
			for target_type, dest, chip in ((low_target_type, low_target_dest, low_chip), (high_target_type, high_target_dest, high_chip)):
				if target_type == "bot":
					if not dest in bots:
						bots[dest] = Bot()
					bots[dest].give(chip)
				elif target_type == "output":
					try:
						outputs[dest].append(chip)
					except KeyError:
						outputs[dest] = [chip]
			return True
	else:
		raise Exception("Malformed instruction")

if __name__ == "__main__":
	with open("day10.txt", "r") as inputfile:
		instructions = inputfile.read().splitlines()
	bots = dict()
	outputs = dict()
	while len(instructions):
		instruction = instructions.pop(0)
		if not complete_instruction(instruction, bots, outputs):
			instructions.append(instruction)


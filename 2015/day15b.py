#!/usr/bin/env python
# coding: utf-8
import re, itertools
from sys import argv

DEBUG = True if (len(argv)>1 and argv[1] == "-d") else False
MAX_TEASPOONS = 100

def recipetotalscoreandcals(ingredients, recipedict):
	if len(ingredients) != len(recipedict):
		raise Exception("Recipe must specify a value for each ingredient")
	characteristicdict = dict()
	for ingredient in ingredients:
		# print "    {} tbsp of {}".format(recipedict[ingredient], ingredient)
		for characteristic in ingredients[ingredient]:
			val = ingredients[ingredient][characteristic] * recipedict[ingredient]
			# print "       {} points contributed to {} by {}".format(val, characteristic, ingredient)
			try:
				characteristicdict[characteristic] += val
			except KeyError:
				characteristicdict[characteristic] = val
		# calories += ingredients[ingredient]['calories'] * recipedict[ingredient]
	for characteristic in characteristicdict:
		if characteristicdict[characteristic] < 0:
			characteristicdict[characteristic] = 0
	# print characteristicdict
	return (reduce(lambda x,y: x*y, [characteristicdict[z] for z in filter(lambda x: x!= 'calories', characteristicdict.keys())]), characteristicdict['calories'])

def load_ingredients(filename):
	regex=re.compile(r'(.+): (.+) (-?\d+), (.+) (-?\d+), (.+) (-?\d+), (.+) (-?\d+), (.+) (-?\d+)$'); 
	try:
		with open(filename, 'r') as inf:
			inputdata=inf.read().splitlines()
	except Exception:
		print "I had some issue reading the input data"
		raise Exception

	ingredients = dict()

	for line in inputdata:
	    data = regex.match(line).groups()
	    ingredients[data[0]] = { data[1]: int(data[2]), data[3]: int(data[4]), data[5]: int(data[6]), data[7]: int(data[8]), data[9]: int(data[10]) }

	return ingredients

ingredients = load_ingredients('day15' + ('test' if DEBUG else '') + '.txt')
ingredientlist = ingredients.keys()

# for ingredient in ingredients:
#	print "%-20s%s" % (ingredient+":", ingredients[ingredient])

combinations = filter(lambda x: sum(x) == MAX_TEASPOONS, itertools.permutations(xrange(MAX_TEASPOONS+1), len(ingredients.keys())))

scores = dict()

for num, recipe in enumerate(combinations):
	recipedict = dict(zip(ingredientlist, recipe))
	score = recipetotalscoreandcals(ingredients, recipedict)
	scores[str(num) +":"+ repr(dict(zip(ingredientlist, recipe)))] = score
	# print "Total score for recipe #{}: {}, {} calories".format(num, *score)

highestscore = sorted(scores.items(), key=lambda x: x[1][0])[-1]
print "Highest score was {} for recipe {}, {} calories".format(highestscore[1][0], highestscore[0], highestscore[1][1])

highestscore500cals = sorted(filter(lambda x: x[1][1]==500,scores.items()), key=lambda x: x[1][0])[-1]
print "Highest score with 500 caolories was {} for recipe {}".format(highestscore500cals[1][0], highestscore500cals[0])



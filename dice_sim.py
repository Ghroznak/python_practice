#dice rolling simulator
import random

#init
n = 3; #number of dice
d = 6; #type of dice (d6, d8 etc)
result = 0;
dice = 0;
i = 0;
attr = {'Str': 1, 'Sta': 1, 'Con': 1, 'Int': 1, 'Wis': 1, 'Cha': 1};

#attributes
def stats_roll(attribute):
	result = 0
	for x in range(3):
		dice = random.randint(1, 6)
		result = result + dice
	return result

def addStats(attributes):
	for keys in attr:
		attr.values() = stats_roll(attrib)
	print (attr.items())


for value in attr:
	print (value), attr[value]





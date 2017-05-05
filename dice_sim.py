#dice rolling simulator
import random

#init
n = 3; #number of dice
d = 6; #numbers on dice
result = 0;
dice = 0;

attributes = ('Str', 'Sta', 'Con', 'Int', 'Wis', 'Cha');

#stats_roll called to roll random value to be assigned to dictionary keys
def stats_roll(attribute):
	result = 0
	for x in range(n):
		dice = random.randint(1, d)
		result = result + dice
	return result

#assigning values to list
attribute_values = (stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int))

#zipping attributes and attribute_values together into a dictionary
character_attributes = dict(zip(attributes, attribute_values)) 


print (character_attributes.items())





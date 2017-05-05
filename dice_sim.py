#dice rolling simulator
import random
import time
from time import sleep

#init
n = 3; #number of dice
d = 6; #numbers on dice
result = 0;
dice = 0;

attributes = ('Str', 'Sta', 'Con', 'Int', 'Wis', 'Cha', 'HP');

#stats_roll called to roll random value to be assigned to dictionary keys
def stats_roll(attribute):
	result = 0
	for x in range(n):
		dice = random.randint(1, d)
		result = result + dice
	return result

def health(int):
	int *= 5
	return int

#assigning values to list
char_attrib_values = (stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int))
monster_attrib_values = (stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int))

#zipping attributes and attribute_values together into a dictionary

character_attributes = dict(zip(attributes, char_attrib_values)) 
monster_attributes = dict(zip(attributes, monster_attrib_values))

character_attributes['HP'] = health(character_attributes['Con'])
monster_attributes['HP'] = health(monster_attributes['Con'])

print (character_attributes.items())
print (monster_attributes.items())

while character_attributes['HP']>0 or monster_attributes['HP']>0:
	char_dmg = character_attributes['Str'] * 2
	monster_dmg = monster_attributes['Str'] * 2
	monster_attributes['HP'] -= char_dmg
	print ("Monster is down to " + str(monster_attributes['HP']) + " hitpoints!")
	time.sleep(2)
	if monster_attributes['HP']<0:
		break
	character_attributes['HP'] -= monster_dmg
	print ("Hero is down to " + str(character_attributes['HP']) + " hitpoints!")
	time.sleep(2)
	if character_attributes['HP']<0:
		break

if monster_attributes['HP']<character_attributes['HP']:
	print ("Hero has won")
else:
	print ("Monster has won")





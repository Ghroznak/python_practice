#dice rolling simulator
import random
import time
from time import sleep

#init
n = 3; #number of dice
d = 6; #numbers on dice
result = 0;
dice = 0;

attributes = ('Str', 'Agi', 'Con', 'Int', 'Wis', 'Cha', 'HP');

def stats_roll(attribute):		#stats_roll called to roll random value to be assigned to dictionary keys
	result = 0
	for x in range(n):
		dice = random.randint(1, d)
		result = result + dice
	return result

def health(int):	#determines health.
	int *= 5
	return int

#assigning values to list
hero_attrib_values = (stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int))
monster_attrib_values = (stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int), stats_roll(int))

#zipping attributes and attribute_values together into a dictionary

hero_attributes = dict(zip(attributes, hero_attrib_values)) 
monster_attributes = dict(zip(attributes, monster_attrib_values))

hero_attributes['HP'] = health(hero_attributes['Con'])
monster_attributes['HP'] = health(monster_attributes['Con'])

def attack_roll(atk, dfs):
	attacker = atk * random.randint(1,20)
	defender = dfs * random.randint(1,20)
	if attacker > defender:
		return True
	else:
		return False

def damage_roll(int):
	result = int + random.randint(1, 6)
	return result
	
def initiative(int):
	result = random.randint(1,20)
	return result
	
while hero_attributes['HP']>0 or monster_attributes['HP']>0:
	if attack_roll(hero_attributes['Str'], monster_attributes['Agi']) == True:
		monster_attributes['HP'] -= damage_roll(hero_attributes['Str'])
		print ("Donald Trump is down to " + str(monster_attributes['HP']) + " hitpoints!")
	else:
		print ("Hero missed!")
	time.sleep(2)
	if monster_attributes['HP'] < 1:
		break
	if attack_roll(monster_attributes['Str'], hero_attributes['Agi']) == True:
		hero_attributes['HP'] -= damage_roll(monster_attributes['Str'])
		print ("Hero is down to " + str(hero_attributes['HP']) + " hitpoints!")
	else:
		print ("Monster missed!")
	time.sleep(2)
	if hero_attributes['HP'] < 1:
		break

if monster_attributes['HP']<hero_attributes['HP']:
	print ("Hero has won")
else:
	print ("Monster has won")

import random
import time

difficulty = 0.5;
killcount = 0;

class hero:	#attributes related to hero
	
	def __init__(self, name, race, attributes):
		self.name = name
		self.race = race
		self.attributes = attributes
	
class monster:		#attributes related to monster
	
	def __init__(self, attributes):
		self.attributes = attributes
	
def create_attributes(difficulty):		#creates attributes
	
	def stats_roll(int):		#stats_roll called to roll random value to be assigned to dictionary keys
		result = 0
		for x in range(1, 4):
			dice = random.randint(1, 6)
			result = result + dice
		return result
	
	def health(int):		#adds health based off 'Con' value
		int *= 5
		return int
	
	attributes = ('Str', 'Agi', 'Con')
	attrib_values = ((round((stats_roll(int) * difficulty), 0)),(round((stats_roll(int) * difficulty), 0)), (round((stats_roll(int) * difficulty), 0)))
	attributes = dict(zip(attributes, attrib_values))
	attributes['HP'] = health(attributes['Con'])
	return attributes

def encounter():	#starts the fighting loop until Hero HP <  1
	
	enemy = create_attributes(difficulty)	#creates a new monster for sake of looping the combat
	enemy = monster(enemy)			#adds monster to the monster class
	
	print (player.attributes)		#shows stats of the player
	print (enemy.attributes)		#shows stats of the monster
	
	def attack_roll(atk, dfs):					#determines if an attack is a hit or miss
		attacker = atk * random.randint(1,20)
		defender = dfs * random.randint(1,20)
		if attacker > defender:
			return True
		else:
			return False

	def damage_roll(int):					#determines amount of damage done if attack_roll function = true
		result = int + random.randint(1, 6)
		return result

	def combat():			#plays out the combat instance
		turn = 0;
		global killcount, difficulty;
		
		while 1:		#keeps looping the fighting as long as either hero or monster has > 0 HP
			turn += 1
			print ("---------- Round " + str(turn))
			if attack_roll(player.attributes['Str'], enemy.attributes['Agi']) == True:	#checks if there is a hit
				dmg = damage_roll(player.attributes['Str'])
				enemy.attributes['HP'] -= dmg
				print ("ooo(:::::::> Monster Elf was hit for " + str(dmg) + " damage and is down to " + str(enemy.attributes['HP']) + " hitpoints!")
			else:
				print ("MISS!Hero missed!")
			time.sleep(2)
			if enemy.attributes['HP'] < 1:
				break
			if attack_roll(enemy.attributes['Str'], player.attributes['Agi']) == True:
				dmg = damage_roll(enemy.attributes['Str'])
				player.attributes['HP'] -= dmg
				print ("ooo(:::::::> Hero was hit for " + str(dmg) + " damage and is down to " + str(player.attributes['HP']) + " hitpoints!")
			else:
				print ("MISS! Monster Elf missed!")
			time.sleep(2)
			if player.attributes['HP'] < 1:
				break
				
		if enemy.attributes['HP'] < player.attributes['HP']:
			print ("Hero has won")
			healing = 5 * random.randint(1, 10)
			player.attributes['HP'] += healing
			if player.attributes['HP'] > player.attributes['Con'] * 5:		#checks if healing would go over the Max HP allowed (5 * Con)
				player.attributes['HP'] = player.attributes['Con'] * 5		#if healing goes over Max HP the HP is reduced to Max
			print ("Hero consumed a healing potion and healed up for " + str(healing) + " points. Lets kill another monster!")
			time.sleep(2)
			killcount += 1				#keeps track of how many monsters slain.
			difficulty += 0.1			#adds a difficulty modifier which increases the stats of newly created monsters
			difficulty = round(difficulty, 1)
		else:
			print ("Monster Elf has won")
			print ("Hero killed " + str(killcount) + " Monster Elfs this time!")
			print ("Difficulty reached: " + str(difficulty))
			
	combat()

me = create_attributes(1)
enemy = create_attributes(difficulty)		
player = hero("Ghroznak", "Orc", me)
enemy = monster(enemy)			

while player.attributes['HP'] > 0:
	encounter()

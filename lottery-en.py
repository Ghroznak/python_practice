import random
from random import randrange
import time as t

#init
rows = 0;
cost = 0;
win = False;
i = 0;
winner = [[], [], [], [], [], [], []]

def lottonumbers(*args):			#generates random lotto numbers
	number = random.sample(range(1,35), 7)
	number.sort()
	return number

def player_numbers(*args):		#generates 5 random lotto numbers
	n = 0;
	for list in winner:
		winner[n] = lottonumbers(dict)
		n += 1
	return winner

while i < 50:					#randomly draws new numbers until winning 50 times.
	start = t.time()
	while not win:
		lottono = lottonumbers()
		winner = player_numbers()
		win = lottono in winner
		rows += 1
		cost = rows * 25 
	
	#writes results to file with comma seperation
	#f = open('H:\Delete Me\lotto.txt', 'a')
	#f.write("# of rows," + str(rows) + "," + "Cost," + str(cost) + "," + "Winning number was" + "," + str(winner) + '\n')
	
	print("Rows generated: " + str(rows) + "\nThis time it cost: " + str(cost) + "\nWinning number was " + str(lottono)) #prints out total cost in NOK to achieve a lottery win
	
	#resets values for the next run of the loop
	win = False;
	rows = 0;
	cost = 0;
	i += 1
	duration = float(t.time() - start)		#prints time it took from start of loop until winning number was hit.
	print("--- %.2f seconds ---" % duration) 
	
f.close()	#closes file after script ends

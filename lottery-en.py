import random
from random import randrange
import time as t

#init
yournumbers = 0;
yournumbers = [7, 11, 13, 17, 23, 29, 31]
winningnumber = 0;
rows = 0;
cost = 0;
win = False
i = 0;

#runs the script 50 times.
while i < 50:
	start = t.time()
	while not win:
		#n = how many numbers to draw
		n = 7; 
		#generate random number
		#yournumbers = random.sample(range(1,35),n) 
		#generate random winning number
		winningnumber = random.sample(range(1,35),n) 
		#sorting number list for comparison
		yournumbers.sort()
		winningnumber.sort()
		#compare winning number to your number
		win = True if str(winningnumber) == str(yournumbers) else False
		rows += 1
		cost = rows*5 
	
	f = open('H:\Delete Me\lotto.txt', 'a')
	f.write("# of rows:" + str(rows) + ":" + "Cost:" + str(cost) + ":" + "Winning number was" + ":" + str(winningnumber) + '\n')
	print("This time it cost: " + str(cost))
	win = False;
	rows = 0;
	cost = 0;
	i += 1
	duration = float(t.time() - start)
	print("--- %.2f seconds ---" % duration) 
f.close()
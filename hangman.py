# Hangman
import random

def make_a_word(strng): #create a def or remove it again? revert strng to secret_word if removed.
	word_File_path = '/Users/RogerMBA/PycharmProjects/Hangman/english3.txt'
	f = open('english3.txt', 'r')
	lines = f.readlines()
	for index, line in enumerate(lines):
		lines[index] = line.strip('\n')

	strng = lines[random.randint(1, len(lines))]
	strng = strng.upper()
	print(strng)
	return strng

make_a_word(secret_word)
reveal_word = ["_"] * len(secret_word)
used_letter = []
wrong_letter = []
win_condition = list(secret_word)
win_condition = ' '.join(win_condition)

def compare(strng):
	if not strng.isalpha() or len(strng) > 1:
		print("Please guess only one letter at a time! Try again!")
	elif strng in used_letter:
		print("The letter >> " + str(strng) + " << has already been used. Try again!")
	elif strng in secret_word:
		print("You found a letter! " + str(strng) + " was in the word!")
		used_letter.append(strng)
		for index, value in enumerate(secret_word):
			if value == strng:
				reveal_word[index] = strng
		the_word = ' '.join(reveal_word)
		if the_word == win_condition:
			print("You figured it out! Congratulations!")
			exit()
		else:
			print("So far you revealed this much of the word " + str(the_word))
	else:
		used_letter.append(strng)
		wrong_letter.append(strng)
		attempts = 10 - len(wrong_letter)
		print("That letter was not in the word. Try again!\n You have " + str(attempts) + " attempts left!")
		if attempts == 0:
			print("\nYou lost you klutz!")
			exit()


while 1:
	guess = input("Guess a letter: ")
	guess = guess.upper()
	compare(guess)

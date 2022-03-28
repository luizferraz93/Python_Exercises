#Modify the program to use a while loop, to allow the player to keep guessing.
#The program should let the player know whether to guess higher or lower, and should
#print a message when the guess is correct.
#Allow the player to quit by entering 0 (zero) for their guess.

#answer = 5

#print (input("Please guess a number between 1 to 10: "))
#guess = int(input())
#
#if guess != answer:
#	if guess < answer:
#		print("Please guess higher")
#	else:
#		print("Please guess lower")
#	guess = int(input())
#	if guess == answer:
#		print("Well done, you guessed it")
#	else:
#		print("Sorry you haven't guessed correctly")
#else:
#	print("You got it first time!")



import random

highest = 10
answer = random.randint(1, highest)
guess = 0

print (input("Please guess a number between 1 and {}: ".format(highest)))

while guess != answer:

	guess = int(input())
	if guess == 0:
		break
	if guess == answer:
		print("Well done, you guessed it")
		break
	else:
		if guess < answer:
			print("Please guess higher")
		else:
			print("Please guess lower")

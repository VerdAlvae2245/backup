import random

mysteryNum = random.randint(1, 100)
score = 0

while True:
	guess = int(input("Pick a number 1 though 100 "))
	score = score + 1

	if guess == mysteryNum:
		print("Good Guess")
		break
	elif guess> mysteryNum:
		print("Too high, try again")
	else:
		print("too low, try agian")

print("It took you " + str(score) + " guesses")
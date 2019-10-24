


# break into pieces 
# welcome screen , with name entry
# score screen with computer , player (name), ties
# options for game r, p, s, q
# game will loop intil q is entered
# each loop it will get a random choice from the computer
# a choice from the platers compare the two , and update the score
# when the game is over (q is entered) final score displayed

# WELCOME PAGE
# prompt for the player name
# a welcome message

#__________________________________________________________________________________

# imports:
import random
# varibles
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices = ["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name ")
# main loop
while True:
	# Print score
	print("Score:")
	print("Computer: " + str(computerScore))
	print(name + ":" + str(playerScore))
	print("Ties: " + str(ties))
	choice = input("Enter 'r' for rock , 'p' for Paper, 's' for scissors or 'q' to quit: ")
	computerChoice = random.choice(cChoices)
	print(computerChoice)
	if choice == "q":
		break

	
	if choice == "r":
		print(name + " Picked Rock")
		if computerChoice == "r": # Tie
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("computer picked Paper")
			print("Paper beats Rock")
			computerScore += 1
		else: # s is only choice left
			print("Computer picked Scissors")
			print("Rock beats Scissors")
			playerScore += 1
	
	if choice == "p":
		print(name + "Picked Paper")
		if computerChoice == "p":
			print("Computer picked Paper")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "r":
			print("computer picked Rock")
			print("Paper beats Rock")
			playerScore += 1
		else:
			print("Computer picked Scissors")
			print("Scissors beats Papers")
			computerScore += 1
	
	if choice == "s":
		print(name + "Picked Scissors")
		if computerChoice == "p":
			print("Computer picked Paper")
			print("Scissors beat paper")
			playerScore += 1
		elif computerChoice == "r":
			print("Computer picked Rock")
			print("Rock beats scissors")
			computerScore += 1
		else:
			print("Computer picked Scissors")
			print("This is a tie")
			ties = ties + 1
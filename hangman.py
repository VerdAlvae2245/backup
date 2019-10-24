import random

#print("Welcome to hangman")
#name = input("What is your name? ")
 
myList = "arizona", "obama", "walmart", "target"
words = random.choice(myList)
myList= list(words)

Right = []
Wrong = []
guessList = []

misses = 0

tries = input("How mabnt tries would you like to have? ")
# How to change a string into a list
# how to make a list with _ for characters

for letter in words:
	guessList.append("_")
print(guessList)

letter = input("Enter a letter: ")

if letter in myList:
	index = guessList.index(guess)
	Right.pop(int(index))
	Right.insert(int(index),guess)
	print(Right)

else:
	print("Missed")











import random

#print("Welcome to hangman")
#name = input("What is your name? ")
 
myList = "arizona", "obama", "walmart", "target"
words = random.choice(myList)
myList= list(words)

Right = []
Wrong = []
guessList = []

for letter in myList:
	Right.append("_")

misses = 0

tries = input("How mant tries would you like to have? ")

letter = input("Enter a letter: ")

if letter in words:
	index = myList.index(letter)
	Right.pop(int(index))
	Right.insert(int(index),letter)
	print(Right)
	print("You have " )
if letter not in words:
	print("Wrong")
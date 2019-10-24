# Eduardo Verdugo Alvarez
#hour 1

print("Welcome to To Do List")

todoList = [ ]
while True:
	print("Enter a to add a item")
	print("Enter r to remove a item")
	print("Enter p to print the List")
	print("Enter q to quit")
	choice = input("Choose: ")

	if choice == "q":
		break
	elif choice == "a":
		 choice = input("What do you want to add to your list? ")
		 todoList.append(choice)
	elif choice == "r":
		 choice1 = input("What do you want to remove from your list? ")
		 todoList.remove(choice1)
	elif choice == "p":
		 choice = print(todoList)
	else:
		print("You choose something not listed")
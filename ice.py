favFoods = ["Pizza", "Ice Cream","Soup"]
print(favFoods[0])
print(favFoods[2])
print(favFoods)
# Add to the end of the list
favFoods.append("Yogurt")
print(favFoods)
print("My 4th favorite food is "[3])
# insert - Add to sn index in a list
favFoods.insert(1,"Chicken")
print(favFoods)
# remove an item form the list
favFoods.remove("Chicken")
print(favFoods)
# Remove by index
favFoods.pop(0)
print(favFoods)

favFoods.insert(0,"Pizza")
# loop through a list
for food in favFoods:
	print(favFoods)

	numList = [3, 6, 2, 10, 22, 44, 53, 7]

# loop through the list and all the numbers together then print the sum

sum = 0
for num in numList:
	sum = sum + num


print(sum)
#
print(len(favFoods))

# Make a list of favorites movies
# prompt for a favorite list 
movieList = ("Cars", "Transformers", "Fast and Furious", "Marvel Movies")
myMovie = input("What is your favorite Movie ? ")
movieList.append("myMovie")
print(movieList)

#list methods and Functions
# append - adds an item to the end  of a list 
# insert - adds an item to a specified index
# remove - removes a specified item from the list


# print(movieList[len(movieList)- 1])
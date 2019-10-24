# Calculation, printing, varibles

# Printing to the screen 
# The built in function print(), print to the screen
# it will print both strings and numbers
print("Printing to the screen...")
print("hello") #a string
print('hello agian')
print(6) #a number
print("6") #a string agian
print(6+6) # 12
print("6"+"6") # string concationate

# preforming calculations
# addition +
# subtration -
# multiplication *
# division /
# exponents **
# modulo %

print(4 - 2) # subtration -> 2
print(4 * 2)
print(4 / 3)
print(4 ** 3)
print("Modulo operator test...")
print(5 % 3)
print( 10 % 2)
print(16 % 3 )
# Modulo gives remainders
# python operators follow the same order of oprtation as Math
print(4 - 2 * 2)
print((4-2)* 2)

# variables
#varibles are used to hold data
#vriable are declared and set to a value
badLuck = 13 # declared a varible called badLuck and initialized it to 13
print("badLuck = " + str(badLuck)) # cast it to a string
# Lets do another one
goodLuck = "4" # string varibles
print("goodLuck =" + goodLuck) # dont have to cast
badLuck + 5 # this is pointless
print(badLuck)
badLuck = badLuck + 5 # now badluck is 18
print(badLuck)

# you can also save input into variables
# using input(), A prompt goes inside the ()
name = input("What is your name?")
print("Hello" + name)
print(name*10)
name = name +"\n" # escape character
print(name *10)
# lets try some math
base = input("Enter the base number:")
exp = input("Enter the exponecnt")
print(int(base)**nt(exp))
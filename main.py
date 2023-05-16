#Manipulating strings
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")
print("For Fun : Hello World!\nHello World\n" + "Angela")

a = "Test"
b = " Test Function for all"
print(a + b)
print('-' * 100) #using an operator


print("The Input Function:")

# Testing the input function by itself
input("Please enter your name : ")

#using the input function within a print function
print("Hello " + input("What is your name? ") + " !")

#using the len function to calculate the length of a string
print("Your name length is: " + str(len(input("What is your name? "))))


print("-" * 100)

print("Variables")

name = input("What is your name? ")

print(len(name))

#switch the inputs for a and b around
# make use of a third variable
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)

print("-" * 100)

print("Project")

#Objectives:
# 1) Create greeting for the program
# 2) Get name of City - print on next line
# 3) Get name of pet - print on next line
# 4) Combine both - print on next line

print("Welcome to the band name generator!")
city = input("what is the name of your city that you were born in? \n")
pet = input("What is the name of your first pet? \n")

print(f"Your band name could be: {city} {pet}!")
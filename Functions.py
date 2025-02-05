# Function - Set of code created once and used through out the program
# Helps break our program smaller and managable.
# Function - Define the function
#          - Call the function

def hi():
    print("Hi user")
hi()

# def add():
#     a = int(input("Enter any no"))
#     b = int(input("Enter any no"))
#     print("Sum of two values are:", a+b )
# add()

# Parameters - write inside parenthesis() with name of function
# Args - Values passed to parameter while calling function
# With different values

def add(x,y): # Parameters
    print(x+y)  # Args
add(3,4)
add(2,3)

#area of rectangle
def rect(l,b):
    print("area of rect ",l*b)
rect(2,4)

# Return - Exit the code and save value at end.
def sub(a,b):
    return ("sub is : ", a-b)
print(sub(45,7))

# Recursion - call itself - benefits of looping
# def I_love_you():
#     print("Love")
#     return I_love_you()
# print(I_love_you())

# factorial by recursion
def fact(n):
    if n == 1:
        return 1
    else:
        return n*(fact(n-1))
print(fact(3))

# Lambda In Python - Anonymous func required for short period of time// Multi tasking
x = lambda a,b,c,d: (a+b)*c%2
print(x(3,4,7,4))

# Local - Restricted only one block of code & can't be changed throughout the program
i = 29
print("var value",i)
def hellw():
    i = 34
    return i
print(hellw())  # prints 34
print(i)   # prints 29 again Unchanged

#  Global variable - Not restricted to one block of code & can be changed throughout the program
i = 29
print("var value",i)
def hellw():
   global i
   i = 34
   return i
print(hellw())  # prints 34
print(i)   # prints 34 changed completely



# Loops
# For Loop - For Range +1
# While loop -
# while true -
# Nested loop -
from itertools import repeat
from math import trunc

for i in range(1,101,2):
       print(i)
n = int(input("Enter any no: "))

# print Table
for i in range(1,11):
    print(n,"*",i,"=", n*i)

var = 1  # `i` is an integer    (Python Understand it)
var = "Hello"  # Now `i` is a string
var = [1, 2, 3]  # Now `i` is a list

# While loop ------ Execute till condition is true
# Increment is done inside Loop

n = 1
a = int(input("write a number jiski table chahiye: "))
while n<=10:
    print(a,"X" ,n, "=", n*a )
    n+=1

# while True - Infinite Loop == Need to break
while True:

  num1 = int(input("Enter number here: "))
  num2 = int(input("Enter another number here: "))

  print("Sum of these nos are:", num1 + num2)
  repeat = input("Do you want to stop the program: ")
  if repeat == "yes":
      break # Stop the program

# Nested Loops - A loop inside loop called nested loop
# Nested is not a loop, any loop consist of loop inside called as nested loop

for i in range (1,12):  # outer loop for rows
    for j in range(1, i+1):   # Inner for columns
      print(j,end="")
    print()

# Conditional Statement with loops

for i in range (1,1000):
    if i%2==0 and i%7==0:
        print(i)

for songs in range(1,11):
  while songs<=10:
     if songs == 3:
       print("add this to fav")
     else: print(songs)
     songs += 1
     break
# # Break & continue statement

for i in range (1,15):
    if i == 5:
        continue
    print(i)


# Q1 Sum of even upto 50
sum = 0
for i in range (1,51):
    if i%2 == 0:
      sum = sum  + i
print("sum of all even", sum)

#Q2 - first 20 nos and their squares

for i in range (1,21):
    print("square of",i ,"is",i*i)

# Q3 - add First 10 odd nos using while loop

sum = 0
for i in range(1,21):
    if i%2 != 0:
        sum = sum + i
print("sum of first 10 odd nos are",sum)

# Q4 _program to check no is divisible 8 & 12 upto 100
for i in range (1,101):
    if i%8 == 0 and i%12 == 0:
      print(i)

# Q5 Create billing system at super market

while True:
    name = input("Enter customer name: ")
    total = 0
    while True:
        print("Enter amount & quantity")
        amount = float(input("Enter the price of item: "))
        quantity = int(input("Qty of items: "))
        total = total + amount*quantity
        repeat = input("Do you want to add more items:? (yes/no): ")
        if repeat == "no" or repeat == "NO":
           break
    print("-"*50)
    print("your name:",name)
    print("Your Bill Amount Is : ", total)
    print("-" * 50)
    print(" ***** Thank you! Visit Again ************")

#     repeat1 = input("Do you want to go to next customer? (yes/no):" )
#     if repeat1 == "no" or  repeat1 == "NO" :
#         break
#
# a = "I am born to write history"
# print(a.count("o"))
# z = a.find("write")
# print(z)

# Q) Display star pattern
for i in range(1,7): # Rows
    for j in range(1,i+1): #columns
        print("$",end= " ")
    print()

# Q) Display pattern == just reverse i & j
for i in range(1,6):
    for j in range (1, i+1):
        print(i, end= " ")
    print()
# Q) program to display 11111 - 2222 - 333
for i in range(1,7):
    for j in range(7,i,-1):
        print(i, end= "  ")
    print()

# Q) program for multiply table

for i in range(1,11):
    for j in range(1,i+1):
        print(i*j, end= " ")
    print()

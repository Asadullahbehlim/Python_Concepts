#  If-Else Statements -------
from operator import length_hint
from random import choice

mark = 93

if mark >= 90:
  print("Good")
  if mark >= 95:
      print("You can go to a trip")
elif mark  >=60 and mark<80:
  print("improve")
elif mark >= 80 and mark <90:
  print("Succeeding")
else:
   print("fail")

# Q1) Write a program to check if no. is positive

no = 78
if no >= 1:
  print("number is positive")
elif no == 0:
  print("zero")
else:
  print("no is negative")

# Q2) Write a program to check even or odd.

no = 79
if no %2== 0:
  print("even")
else:
  print("odd")

# Q3) Program to write area

print("PROGRAM TO GET AREA")
print("""Press 1 to get area of square
press 2 to get area of rectangle
press 3 to get area of circle
press 4 to get area of triangle""")

choice = int(input("enter your choice 1 to 4: "))
if choice == 1:
   side = float(input("Enter the length of a side: "))
   area = side*side
   print("area of square is: ", area)
elif choice == 2:
   length = int(input("Enter the length"))
   breadth = int(input("Enter the breadth"))
   area = length*breadth
   print("area of rectangle: ", area)
elif choice == 3:
  radius = float(input("Enter radius of square"))
  area = 3.14*radius*radius
  print("area of circle", area)
elif choice == 4:
  base = float(input("Enter base of triangle"))
  height = float(input("Enter height of triangle"))
  area = 0.5*base*height
  area = print("area of triangle", area)
else:
  print("Invalid Input, Enter nos between 1 to 4")

# Q4 Program to check vowel or not.
letter = input("Enter your letter here: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("its a vowel")
else: print("its constant")

# Q5 Program to check single digit upto 5 digit nos -
num = int(input("Enter a number upto 5 digits here : "))
if num >0 and num <= 9 :
    print("Its a single digit number", num)
elif num>=10 and num <=99:
    print("Its a double digit number", num)
elif num>=100 and num <=999:
    print("Its a triple digit number", num)
elif num>=1000 and num <=9999:
    print("Its a four digit number", num)
elif num>=10000 and num <=99999:
    print("Its a five digit number", num)
else: print("Invalid Input")


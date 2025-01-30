# A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
#  write a program to separate the following string.
# into coma(,) separated value.

A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
B = A.split(".")
print(B)


# Program to sort things alphabatically in python

a = input("Enter anything here: ")
b = sorted(a)
print(b)

# program to remove a given character in string.

var = "Tria"
new = var.replace("T","")
print(new)

# Program to remove dot(.) from following string. Z = "F.R.I.E.N.D.S"

Z = "F.R.I.E.N.D.S"

d = Z.replace(".","")
print(d)

# Q) Program to check no. of occurence

str = "cricket"
count = str.count("c")
print(count)

#Q) Take a input string and reverse it

a = input("Enter any word: ")
b = a[::-1]
print(b)

# check string has all digits
a = input("Enter anything here: ")
if a.isdigit():
       print("Its a numeric")
else:
       print("Not a digit")

# check whether its plaindrom or not
a = input("enter anything bro:")
rev = a[::-1]
if a == rev:
    print("Its a palindrome")
else:
    print("nahi hai be")

# Q) check vowels

z = input("Enter anything here: ")
vowels = {"a","e","i","o","u" }
for i in z:

    if i in vowels:
       print("It has vowel")
       break
else: print("It doesn't has vowel")

# Q) Check title for no
z = input("Enter anything: ")
print(z.title())

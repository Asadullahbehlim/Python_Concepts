a = "Hello cricket"
print(a.find("i"))

#format method
name = "devilliers"
b = "my name is {}"
print(b.format(name))

# String Slicing --------      String[start : end : step]
# Slicing in Simple words --- String [0(default): End(default/full): Step(How much to skip)]
# ends with
Movie = "zindagi na milegi dobara "
print(Movie[6::9])  # String slicing
print(Movie[::1])

# Q) Program to get fibonacci series upto 10 Numbers.
# Method1 ====
a,b = 0,1
for _ in range(10):
    print(a,  end= " ")
    a,b = b, a + b
#Method 2 =====
a = 0
b = 1
for i in range(2,11):
    c = a+b
    a = b
    b = c
    print(c)

# Q3) Program to print prime nos
# print("Prime numbers between 1 and 100 are:")
# for num in range(1,101):
#     if num>1:
#         for i in range(2,num):
#             if num%i == 0:
#                 break
#         else:
#                 print(num, end= " ")

# Taking Input from user
# num = int(input("Enter any no: "))
# if num<=1:
#         print("Its not a prime no.")
# else:
#         for i in range(2,num):
#             if num%i == 0:
#               print("Its not a prime no.")
#               break
#         else:
#            print("Its a prime no. ")

# palindrome number - While Loop
# num = int(input("Enter any number"))
# temp = num
# rev = 0
# while num>0:
#     dig = num%10
#     rev = rev*10 + dig
#     num = num // 10
# if rev == temp:
#         print("Its a palindrome")
# else:
#         print("Its not a palindrome")
#
# # palindrome for strings
# num = input("Enter number:")
#
# if num == num[::-1]:
#     print("Its a palindrome")
# else:
#     print("Its not a palindrome")


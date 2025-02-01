A = ["Kohli", "devilliers","Warner","Starc"]

# Q) To swap first & forth element

A[0],A[3] = A[3],A[0]
print(A)

# Q) To add new value at second position

A.insert(1,"Bumrah")

print(A)

# Q) Delete a value from third position

A.pop(2)
print(A)

# Q) Write a program to multiply all nos in list
B = [16,34,22,39]
mul = 1
for i in (B):
    mul = mul * i
print(mul)

# Q) program to get largest/smallest no from list

C = [16,34,22,39]
C.sort()   #Arrange the list ascending order
print(C)
print("largest value in given list:",C[3])
print("smallest value in given list:",C[0])

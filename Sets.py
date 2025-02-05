# Unordered and mutable
# There's no indexing in it
from os import setsid

# Q) FIND min and max value in it
a = {13,64,32,39}
print("the max value is :",max(a))
print(min(a))

# Q) Find the common elements in 3 lists of given set.

a = [1,5,3,6,2 ]
b = [2,4,5,6 ]
c = [1,9,6,4,3,5 ]
print(set(a) & set(b) & set(c))

# Q) Difference between two sets

a = { 1,5,3,6,2 }
b = { 2,4,5,6 }
print(b.difference(a))

# Q) Remove anything
print(a.remove(1))
print(a)
# check subset or not
print(a.issubset(b))
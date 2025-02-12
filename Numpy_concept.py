import numpy as np

# Numpy -> Used for mathematical & statistical calculation

l1 = np.array([20, 30, 40,50])
l2 = np.array([40, 30, 70,37])
b  = print(l1*l2)
c = np.array_split(l1,2)    # array split
print(c)
arr = np.array([[ 32, 21, 54 ],[22, 43,56]])
#  [22, 43, 56]]

print(arr[1,1:2])
print(np.size(arr))
print((arr.dtype))

a = [32, 34, 36, 38.43]
arr2 = np.array(a)
print(arr2.shape)
print(len(arr2))
print(arr2.astype(int))
print(arr2.dtype)

def func(a,b):
    print(a-b)
func(44,23)


a = np.pow(2,7)
print(a)

import numpy as np
# ar = np.array([[3,2,56,23,98],[22,56,77,51,41]])
# print(np.sort(ar))
#
# #Search
# ar1 = np.array([3,2,56,23,98])
# s = np.where(ar1 %2 ==0)
# s1 = np.searchsorted(ar1,56)
# print(s,s1)
#
# # Filter
# ar2 = np.array([20,30,40,60])
# fa = ar2 %3 ==0
# new = ar2[fa]
# print(new)

# aggregating Function
a = np.array([[23,44,56,21],[33,14,26,51]])
print(np.sum(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.cumsum(a))

x = [100,132,154,232,344]
y = [122, 433, 231, 655]

price = np.array(x)
quantity = np.array(y)

print(price,"\n" ,quantity)
print(np.sum(x))
print(np.sum(y))


# Normal Sort Method
# q = [23,4,67,3]
# c = q.sort()
# print(q)

# Statistical Function
import statistics as stats
baked_food = [200,300,150,324,200]
food = np.array(baked_food)
print(np.mean(baked_food))     # sum of all value
print(np.median(baked_food))     # central value
print(stats.mode(baked_food))
print(np.std(baked_food))

tobacco_consume = [20,30,40,50]
death = [120,130,160,185]
print(np.corrcoef([tobacco_consume,death]))

price = [300,100,150,250,200]
sales = [10,20,6,15,4]
print(np.corrcoef([price,sales]))

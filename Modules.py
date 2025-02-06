# dateTime Module
import datetime

y = datetime.datetime.now()
print(y)

z = datetime.datetime(2005,5,7)
print(z.strftime("%m"))

# Random Module - pick any random number
import random
l = ["kohli","Jassi","Devilliers","Sky"]
x = random.choice(l)
print(x)

# Math Module
import math
d = min(23,54,86)
print(d)

# Power
a =pow(2,7)
print(a)

# square root
c = math.sqrt(289)
print(c)

# Positive convert
d = abs(-676)
print(d)

# Ceiling value

e = math.ceil(54.76)
print(e)

import demo as d
f = d.add(3,4)
print(f)

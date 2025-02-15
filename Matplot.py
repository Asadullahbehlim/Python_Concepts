# Matplot to create visulatization in python
import colorsys

import matplotlib.pyplot as plt

x = [2010,2014,2018,2022]
y = [70,120,100,170]

plt.bar(x,y)
plt.xlabel("Yearly Data", fontsize = 10)
colors = ["red","green","blue","yellow","orange"]
plt.bar(x,y, color = colors, edgecolor = "black" )
plt.ylabel("Collection In Crores")
plt.title("Money collection")

plt.show()
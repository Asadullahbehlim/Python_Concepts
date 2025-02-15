from itertools import groupby
from pickletools import markobject

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel
from pandas import read_excel
#
# data = pd.read_excel("/Users/asadullahbehlim/Downloads/expense3.xlsx")
# df = pd.DataFrame(data)
# print(df)
# grouped_by = df.groupby("Payment Mode")["Amount"].sum()
# print(grouped_by)
# # plt.bar(df["Payment Mode"].astype(str),df["Amount"])
# plt.bar(grouped_by.index, grouped_by.values)
# plt.show()

import matplotlib.pyplot as plt
from pyparsing import alphas

x = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday","Sunday"]
y =  [165, 179,150,185,239,358,421]
y1 =  [169, 187,127,195,224,338,477]

plt.title("Customers coming to restaurant")
plt.ylabel("No of customers")
plt.plot(x,y, marker = "o", ls = "--", color = "red", label = "week1")
plt.plot(x,y1, marker = ">", ls = "-", color = "green", label = "week2")
plt.legend()

plt.show()



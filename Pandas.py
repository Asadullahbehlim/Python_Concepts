# Pandas = Panel Data (Used To Manipulate & Transform Data)
# It has function to analyzing, cleaning, exploring and manipulating data.

import pandas as pd
#
# data = {"Name": ["Abd","Starc","Root"],
#         "Age": [33,36,31],
#         "Net worth": [256000,187000,298000] }
# data_format = pd.DataFrame(data)
# print(data_format)

# data1 = pd.read_excel("/Users/asadullahbehlim/Downloads/Investment_sheet.xlsx")
# print(data1)

data2 = pd.read_csv("/Users/asadullahbehlim/Downloads/company1.csv")
print(data2.isnull().sum())
print("==========================")
print(data2.dropna())
print("==========================")

import numpy as np

print(data2.replace(np.nan,"hii"))
print("==========================")

data2["salary"] = data2["salary"].replace(np.nan,  29000 )
print(data2)
print("==========================")
print(data2["salary"].mean())
print("==========================")
print(data2.bfill())     # Forward Fill

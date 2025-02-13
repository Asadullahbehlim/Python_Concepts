import pandas as pd
from openpyxl.utils.dataframe import (dataframe_to_rows)
#
# df = pd.read_excel("/Users/asadullahbehlim/Downloads/ESD.xlsx")
# df.loc[(df["Bonus %"] == 0), "GetsBonus"] = "no bonus"
# df.loc[(df["Bonus %"] > 0, "GetBonus")] = "bonus"
# print(df.head(10))
# print(df.tail(15))

data = pd.read_csv("/Users/asadullahbehlim/Downloads/company1.csv")
print(data)

data["Bonus"] = (data["salary"]*20)/100
data["PF"]= (data["salary"]*12/100)# Bonus is 15% of salary
print(data)

data = {"Months": ["January","Febraury","March","April"] }
a = pd.DataFrame(data)
print(a)

def extract(value):
    return value[0:3]

a[" Short_months "] = a["Months"].map(extract)
print(a)

print("=======Group By In-Pandas ==========")

df = pd.read_excel("/Users/asadullahbehlim/Downloads/ESD.xlsx")
df.loc[(df["Bonus %"] == 0), "GetsBonus"] = "no bonus"
df.loc[(df["Bonus %"] > 0, "GetBonus")] = "bonus"
print(df.head(10))
print(df.tail(15))

gp = df.groupby(["Job Title","Gender"]).agg({"EEID":"count"})
print(gp)
gp1 = df.groupby(["Country","Gender"]).agg({"Age": "mean"})      # Average Age
print(gp1)

print(" ============= Merge - Join and concat =========== ")

print(" ======= Concat (Niche laa ke rakh deta ) Combine=========== ")

data1 = {"Cricketer_Name": ["Abd","symonds","kohli","kallis" ],
         "Age": [38,45,35,47],
         "Avg":[52,41,51,53]}


data2 = {"Cricketer_Name": ["Abd","symonds","kohli","kallis" ],
         "Age" : [2004, 1998, 2008, 1995],
         "Avg":[53, 20, 82, 65]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# df1.set_index("Cricketer_Name", inplace=True)
# df2.set_index("Cricketer_Name", inplace=True)
result = pd.concat([df1,df2])

print(result)

print(" ============= Merge (Added New Column )=========== ")


data1 = {"Cricketer_Name": ["Abd","symonds","kohli","kallis" ],
         "Age": [38,45,35,47],
         "Avg":[52,41,51,53]}


data2 = {"Cricketer_Name": ["Abd","symonds","kohli","kallis" ],
         "Debut" : [2004, 1998, 2008, 1995],
         "S/R":[53, 20, 82, 65]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

#result = df2.merge(df1)  # Easy Approach
result = pd.merge(df1,df2, on = "Cricketer_Name")
print(result)


print("============= Join (Side by Side Matching) ===========")
# Join is used to combine two DataFrames based on a common column (key).

data1 = {
    "Cricketer_Name": ["Abd", "symonds", "kohli", "kallis"],
    "Age": [38, 45, 35, 47],
    "Avg": [52, 41, 51, 53]
}

data2 = {
    "Cricketer_Name": ["Abd", "symonds", "kohli", "kallis"],
    "Debut": [2004, 1998, 2008, 1995],
    "S/R": [53, 20, 82, 65]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Set Index (VERY IMPORTANT for Join)
df1.set_index("Cricketer_Name", inplace=True)
df2.set_index("Cricketer_Name", inplace=True)

# Joining Both Tables Side-by-Side
result = df1.join(df2)

print(result)

print("============= Compare DataFrame ===========")

dict = { "Fruits": ["Mango","Banana","orange"],
         "Price": [80,50,60],
         "Qty": [5,12,6] }

df = pd.DataFrame(dict)

df1 = df.copy()
print(df1)
print("Prices after a month ")

df1.loc[0,"Price"] = 100
df1.loc[2,"Price"] = 80
print(df1)
print(df.compare(df1, keep_shape= True))



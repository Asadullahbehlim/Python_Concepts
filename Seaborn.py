import matplotlib.pyplot as plt
import  seaborn as sns
import pandas as pd
from pandas import read_excel

#
# data = { "Days": [1,3,4,6,7],
#          "NOP": [2,5,6,8,3]}
#
# # df = pd.DataFrame(data)
# #
# # print(df)
# sns.lineplot(data = data,x= "Days",y= "NOP")
#
# plt.show()
# ============ Read Excel Seaborn =========== #
# data = read_excel(("/Users/asadullahbehlim/Downloads/ESD.xlsx"))
# df = pd.DataFrame(data)
#
# sns.lineplot(data, x = "Business Unit", y = "Age", style= "Ethnicity", hue="Gender")
# plt.show()
#
# SeaBorn Barplot
# data = sns.load_dataset("titanic")
# print(data)
# sns.barplot(data, x = "survived", y = "pclass", hue="sex", palette="pink")
# plt.show()

# Hist plot
data = sns.load_dataset("tips")
sns.histplot(data, x = "day", hue="sex", kde= True)
plt.show()
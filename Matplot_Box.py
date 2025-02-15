import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import savefig

# l3 =[25,46,79,32,45,19,68,73,48]
# l = [1,3,4,6,9,12,15,23]
# l1 = [2,4,5,6,8,9]
#
# plot_values = [l,l1]
# plt.boxplot(plot_values)
# plt.show()
#

# data = pd.read_excel("/Users/asadullahbehlim/Downloads/ESD.xlsx")
# df = pd.DataFrame(data)
# #plt.violinplot(df["Annual Salary"], showmedians=True), boxplot, stem,
#
# plt.stem(df["Annual Salary"])
# plt.show()

# x = [32,26,22,4,7,45,59,62,68,74,85,83,88]
# plt.hist(x,bins=len(x), edgecolor="black", color= "red")
# plt.show()
#
# data = pd.read_excel("/Users/asadullahbehlim/Downloads/ESD.xlsx")
# df = pd.DataFrame(data)
# plt.hist(df["Age"])
# plt.show()

# Stackplot
days = [1,2,3,4,5,6,7,8]

NOP1 = [5,10,18,29,37,47,55,65]
NOP2 = [10,20,30,40,50,60,70,80]
NOP3 = [8,32,46,55,64,77,88,97]
plt.stackplot(days, NOP1,NOP2,NOP3)
#plt.step(days, NOP1,NOP2,NOP3)
#savefig("fig.png")
plt.show()

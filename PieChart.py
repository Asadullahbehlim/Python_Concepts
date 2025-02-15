import matplotlib.pyplot as plt
import pandas as pd
# By Sample Data
# brands = ["oneplus","Samsung","Apple","Huaweyi"]
# x = [21,32,29,18]
# c = ["pink","lightblue","silver","lightgreen"]
# ex = [0,0.1,0,0]
# plt.pie( x, labels = brands, colors = c, explode= ex, shadow=True, autopct="%.2f" )
# plt.show()

data = pd.read_excel("/Users/asadullahbehlim/Downloads/expense3.xlsx")
df = pd.DataFrame(data)
#group = df.groupby("Payment Mode")["Amount"].sum()
print(df)
plt.pie(df["Amount"], autopct= "%.2f")
plt.show()
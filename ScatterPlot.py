import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#
# x = np.random.randint(1,10,300)
# y = np.random.randint(10,500,300)
#
# plt.scatter(x,y,marker="*")
# plt.show()
#
data = pd.read_excel("/Users/asadullahbehlim/Downloads/ESD.xlsx")
df = pd.DataFrame(data)
print(df)
plt.scatter(df["Age"],df["EEID"], s = df["Annual Salary"])
plt.colorbar()
plt.show()


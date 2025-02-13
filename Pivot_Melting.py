from pandas import pivot

# pivoting has three parameters index, columns, values.
# melting - If we have one column, and we want to melt and have 2 columns
import pandas as pd

dict = { "keys": ["k1","k2","k1","k2"],
        "names": ["John","Ben","david","peter"],
         "houses": ["red","blue","green","red"],
         "grades": ["3rd","5th","7th","9th"]
}

df = pd.DataFrame(dict)
print(df)
#print(df.pivot(index="keys", columns="names", values=["houses","grades"]))
result = pd.melt(df, id_vars= "names", value_vars= ["houses","grades"], var_name="Houses & Grades", value_name="values")
print(result)
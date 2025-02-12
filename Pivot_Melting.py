import pandas as pd

dict = { "keys": ["k1","k2","k1","k2"],
        "names": ["John","Ben","david","peter"],
         "houses": ["red","blue","green","red"]
}

df = pd.DataFrame(dict)
print(df)
print(df.pivot(index="keys",columns="names", values="houses"))
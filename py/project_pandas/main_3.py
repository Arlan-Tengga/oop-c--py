import pandas as pd
import numpy as np

penjualan_a = pd.DataFrame({
    "produk_a" : [100,120,90],
    "produk_b" : [80,110,95],
},index=["senin","selasa","rabu"])

penjualan_b = pd.DataFrame({
    "produk_a" : [200,123,90],
    "produk_b" : [90,123,67]
},index=["senin","selasa","rabu"])

# print(penjualan_b + penjualan_a)

# print(penjualan_a + 3.4)

data_produk = pd.Series({
    "produk_a" : 50,
    "produk_b" : 40
})

data_frame = pd.DataFrame({
    "revenue" : [1000,1200,900],
    "cost" : [600,700,500],
    "tex" : [80,96,72]
},index=["Q1","Q2","Q3"])

# print(data_produk + penjualan_a)

# data_frame["profit"] = data_frame["revenue"] - data_frame["cost"] - data_frame["tex"]
# data_frame["margin"] = data_frame["profit"] + data_frame["revenue"]
# print(data_frame)

# data_a = pd.DataFrame([[1,2],[None,4]],columns=["A","B"])
# data_b = pd.DataFrame([[10,20],[30,40]],columns=["A","B"])

# print(data_a)
# print("\n")
# print(data_b)

data_kita = pd.DataFrame({
    "A" : [1,4,9],
    "B" : [15,25,36]
})

print(np.sqrt(data_kita))
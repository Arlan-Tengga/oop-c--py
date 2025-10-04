import pandas as pd
import numpy as np

data_a = pd.Series(
    [100,120,90],
    index = ["senin","selasa","rabu"],
    name = "data_a"
)

data_b = pd.Series(
    [200,400,500],
    index = ["selasa","rabu","kamis"],
    name="data_b"
)

data_c = pd.Series(
    [300,400,450,900],
    index = ["selasa","rabu","kamis","senin"],
    name="data_c"
)

data_x = pd.Series(
    [3,4,5,None,4]
)

data_f = pd.Series(
    [6,1,2,3,6]
)

def f(x):
    return np.sqrt(x)

def f_1(x):
    return np.log(x)

x = pd.Series([1,4,9,16])
print(f(x))
print("\n")
print(f_1(x))
print("\n")
print(f(x) + f_1(x))

# print(data_x.fillna(3) + data_f)

# total_penjumlahan = data_a**2 + 2*data_a*data_b  + data_b**2
# total_aljabra = (data_a + data_b)**2
# kuadratik = data_b**2

# x = data_a + data_b + data_c

# print(total_penjumlahan)
# print("\n")
# print(total_aljabra)

# print(x.describe())
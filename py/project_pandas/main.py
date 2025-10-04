import pandas as pd
import numpy as np

# series = pd.Series(data,index,name)


# data_penjualan: dict = {
#     "januari": 150,
#     "februari":200,
#     "april":300
# }
# data_series = pd.Series(data_penjualan,name="data penjualan (dalam ribu)")
# print(data_series)

def f(x):
    return x**2

x = np.linspace(0,1,10)
y = f(x)

# data_series = pd.Series(y,index=x,name="grafik eksponen")
# print(data_series.values)
# print("\n")
# print(data_series.index)

# indexing

# data_frame = pd.DataFrame(data,index=index,columns=kolom)

# data = {
#     "Nama" : ["nongpa","aji suraji","jikaw","charles"],
#     "usia" : ["26","27","34","40"],
#     "kota" : ["jakarta","bandung","makassar","jateng"]
# }


# dataframe = pd.DataFrame(data)
# print(dataframe)


def f_1(x):
    return x**2 * np.cos(x)

def f_2(x):
    return np.cos(x)**2 + np.sin(x)**2

def f_3(x):
    return np.sin(x)**2

x = np.linspace(0,1,100)

data = {
    "data 1" : f_1(x),
    "data 2" : f_2(x),
    "data 3" : f_3(x)
}
print(f"5 data awal: \n{pd.DataFrame(data).head(5)}")
print("\n")
print(f"5 data terakhir: \n{pd.DataFrame(data).tail(5)}")
print("\n")
print(f"info data: \n{pd.DataFrame(data).describe()}")
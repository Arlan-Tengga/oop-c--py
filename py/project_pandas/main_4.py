import pandas as pd

# data_csv_saya = """nama,usia,kota,gaji
# ihsan,30,sleman,30000000
# madun,31,klaten,30000000
# akbar,40,klaten,45000000
# irsyad,29,kediri,3000000"""

# with open("data_kita.csv","w") as file_csv:
#     file_csv.write(data_csv_saya)

# data_frame = pd.read_csv("data_kita.cvs")
# print(data_frame)



data_csv_saya = """
ihsan,30,sleman,30000000
madun,31,klaten,30000000
akbar,40,klaten,45000000
irsyad,29,kediri,3000000"""

with open("project_pandas/data_baru.csv","w") as file_csv:
    file_csv.write(data_csv_saya)

data_frame = pd.read_csv("project_pandas/data_baru.csv",header=None,
            names = ["nama","usia","kota","gaji"])

print(data_frame)
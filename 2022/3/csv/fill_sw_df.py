import numpy as np
import pandas as pd

# device_tab = pd.read_csv("devicees_sep_2021.csv")
# print(device_tab.to_string())
# device_platforms = device_tab["series"].unique()
## print(device_platforms)
#
# ver_column = ["None"] * len(device_platforms)
#
# device_softs = pd.DataFrame({"Platform": device_platforms, "version": ver_column})
# print(device_softs.to_string())
# device_softs.to_csv("device_platforms.csv")

month = "mar"
year = "2022"
type = "switches"
devices_file = f"{type}_{month}_{year}.csv"
soft_file = f"{type}_platforms.csv"
output_file = f"{type}_{month}_{year}_full.xlsx"

device_table = pd.read_csv(devices_file)
device_platforms = pd.read_csv(soft_file)
device_table["Docelowo"] = ""
print(device_platforms)
# print(device_table[20:23])
# for index, row in device_platforms.iterrows():
#    print(row["hostname"], row["softwareVersion"])
# sub = device_platforms.loc[0, "Platform"]

for index in device_table.index:
    series = device_table.loc[index, "series"]
    print(series)
    if not pd.isnull(device_table.at[index, "series"]):
        res = device_platforms[device_platforms["Platform"] == series]
        print(f"res: {res}")
        print(f"index: {index}")
        print(
            f"{index} {device_table.iat[index,1]} {series} {res['version'].values[0]}"
        )
        res = device_platforms[device_platforms.isin([series]).any(1)]

        device_table.at[index, "Docelowo"] = res["version"].values[0]
        # recommended_ios = device_platforms.loc[device_platforms["Platform" == series]]

# print(device_table[20:23])
# device_table.to_excel(output_file, index=False, header=True)
device_table.to_excel(
    output_file,
    index=False,
    columns=[
        "hostname",
        "managementIpAddress",
        "series",
        "softwareVersion",
        "Docelowo",
    ],
    header=["Nazwa", "IP", "Model", "Obecnie", "Docelowo"],
)

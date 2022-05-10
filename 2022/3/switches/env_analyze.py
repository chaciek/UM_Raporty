import csv
import glob
import json
import re

import pandas as pd

pairs = {}

with open("ip_names.csv", mode="r") as ip_names:
    csv_reader = csv.reader(ip_names)

    for row in csv_reader:
        pairs[row[0]] = row[1]

file_list = glob.glob("*env.json")
env_report = open("env_report.csv", mode="a")
env_csv = csv.writer(env_report)

for fn in file_list:

    pattern = "(\d+\.\d+\.\d+\.\d+)\..*"
    res = re.match(pattern, fn)

    if res:
        print(fn)
        host = re.match(pattern, fn).group(1)
        pattern = ".*TEMPERATURE is (\w+).*"

        for cont in open(fn, "r"):
            lines = cont.split(",")
            for line in lines:
                print(f"Line:{line}")
                res = re.match(pattern, line)
                if res:
                    name = pairs[host]
                    l = [host, name, res.group(1)]
                    print(l)
                    env_csv.writerow(l)

env_report.close()
env_df = pd.read_csv("env_report.csv")
env_df.to_excel("env_report.xlsx", index=False, header=True)

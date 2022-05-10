import csv
import glob
import json
import re
import os
import pandas as pd
from pprint import pprint
import datetime as dt
import calendar


pairs = {}
month = calendar.month_abbr[
    (dt.date.today().replace(day=1) - dt.timedelta(days=1)).month
]


with open("ip_names.csv", mode="r") as ip_names:
    csv_reader = csv.reader(ip_names)

    for row in csv_reader:
        pairs[row[0]] = row[1]


file_list = glob.glob("*log.json")
log_report = open("log_report.csv", mode="w")

for fn in file_list:

    pattern = "(\d+\.\d+\.\d+\.\d+)\..*"
    res = re.match(pattern, fn)

    if res:
        host = res.group(1)
        log = rf".*{month}.*\-[12]\-.*"

        with open(fn) as json_file:
            data = json.load(json_file)

            for line in data[0]:
                res = re.match(log, line)

                if res:
                    l = f"{host},{pairs[host]},{res.group(0)}"
                    print(l)
                    log_report.write(l + "\n")

#            lines = cont.split(",")
#            for line in lines:
#                # print(f"Line:{line}")
#                res = re.match(log, line)
#                print(line)
#                if res:
#                    l = f"{host},{pairs[host]},{res.group(0)}"
#                    print(l)
#                    log_report.write(l + "\n")
#
log_report.close()

if os.path.exists("log_report.csv") and os.path.getsize("log_report.csv") > 0:
    log_df = pd.read_csv("log_report.csv")
    log_df.to_excel("log_report.xlsx", index=False, header=True)

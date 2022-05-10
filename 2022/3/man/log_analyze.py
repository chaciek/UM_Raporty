import csv
import glob
import json
import re
from dateutil.relativedelta import relativedelta
import datetime as dt
import calendar


import pandas as pd

pairs = {}
month = calendar.month_abbr[
    (dt.date.today().replace(day=1) - dt.timedelta(days=1)).month
]
print(month)

with open("ip_names.csv", mode="r") as ip_names:
    csv_reader = csv.reader(ip_names)

    for row in csv_reader:
        pairs[row[0]] = row[1]

file_list = glob.glob("*logging_parsed.json")
log_report = open("log_report.csv", mode="w")

for fn in file_list:

    pattern = "(rcen-\w+-c0[12])\_.*"
    res = re.match(pattern, fn)

    if res:
        host = res.group(1)
        log = rf".*{month}.*\-[12]\-.*"

        for cont in open(fn, "r"):
            lines = cont.split(",")
            for line in lines:
                # print(f"Line:{line}")
                res = re.match(log, line)
                if res:
                    l = f"{host},{res.group(0)}"
                    print(l)
                    log_report.write(l + "\n")

log_report.close()

log_df = pd.read_csv("log_report.csv")
log_df.to_excel(f"log_report_{month.lower()}.xlsx", index=False, header=False)

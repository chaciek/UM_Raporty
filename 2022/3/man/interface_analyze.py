import csv
import glob
import json
import re

pairs = {}
month = "Nov"

with open("ip_names.csv", mode="r") as ip_names:
    csv_reader = csv.reader(ip_names)

    for row in csv_reader:
        pairs[row[1]] = row[0]


file_list = glob.glob("*show_interfaces_parsed.*")
intf_report = open("intf_report.csv", mode="w")

for fn in file_list:

    pattern = "(rcen[\-a-zA-Z0-9]+)_.*"
    res = re.match(pattern, fn)
    if res:
        host = res.group(1)
        f = open(fn)

        data = json.load(f)

        intf_report = open("intf_report.csv", mode="a")
        intf_writer = csv.writer(intf_report)
        intf_writer.writerow(["host", "intf", "in_errors", "in_crc_errors"])

        print(fn)
        for intf in data:
            if intf == "_exclude":
                continue
            counters = data[intf]["counters"]
            in_errors = 0
            in_crc_errors = 0
            if "in_errors" in counters:
                in_errors = counters["in_errors"]

            if "in_crc_errors" in counters:
                in_crc_errors = counters["in_crc_errors"]

            if in_errors > 10000 or in_crc_errors > 100:
                l = [host, intf, in_errors, in_crc_errors]
                print(l)
                intf_writer.writerow(l)

        intf_report.close()

import csv
import glob
import json
import re

file_list = glob.glob("*ver.json")

for fn in file_list:

    pattern = "(\d+\.\d+\.\d+\.\d+)\.show.*"
    res = re.match(pattern, fn)

    if res:
        host = res.group(1)

        with open(fn, "r") as json_file, open("inventory.csv", "a") as inv_file:
            show_ver = json.load(json_file)
            fieldnames = [
                "host",
                "hostname",
                "chassis",
                "chassis_sn",
                "version",
                "system_image",
            ]
            csv_file = csv.DictWriter(inv_file, fieldnames)

            d = {}
            d["host"] = host
            d["hostname"] = show_ver["hostname"]
            d["chassis"] = show_ver["chassis"]
            d["chassis_sn"] = show_ver["chassis_sn"]
            d["version"] = show_ver["version"]
            d["system_image"] = show_ver["system_image"]

            csv_file.writerow(d)

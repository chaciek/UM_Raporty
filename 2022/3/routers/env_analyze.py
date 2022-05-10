import glob
import json
import re

file_list = glob.glob("*env.json")
env_report = open("env_report.txt", "a")

for fn in file_list:

    pattern = "(\d+\.\d+\.\d+\.\d+)\..*"
    res = re.match(pattern, fn)
    if res:
        host = re.match(pattern, fn).group(1)
        pattern = ".*TEMPERATURE is (\w+).*"

    file = open(fn, "r")
    env_report.write(" \n")
    env_report.write(" \n")
    env_report.write("*********************************\n")
    env_report.write(" \n")
    env_report.write(f"          {host}\n")
    env_report.write(" \n")
    env_report.write("*********************************\n")
    env_report.write(" \n")
    env_report.write(" \n")
    for cont in open(fn, "r"):
        lines = cont.split(",")
        for line in lines:
            # print(f"Line:{line}")
            p1 = ".*temperature\:.*"
            # env_report.write(line)
            r1 = re.match(p1, line)
            if r1:
                print(r1.group(0))
                env_report.write(line + "\n")

            p2 = ".*alarms\:.*"
            r2 = re.match(p2, line)
            if r2:
                print(r2.group(0))
                env_report.write(line)

            p3 = ".*Temperature .*"
            r3 = re.match(p3, line)
            if r3:
                print(r3.group(0))
                env_report.write(line + "\n")

            p4 = ".*Sensor [12345].*"
            r4 = re.match(p4, line)
            if r4:
                print(r4.group(0))
                env_report.write(line)

            p5 = ".*Power Supply.*Output Status:.*"
            r5 = re.match(p5, line)
            if r5:
                print(r5.group(0))
                env_report.write(line + "\n")

            p6 = ".*3G Modem Sensor.*"
            r6 = re.match(p6, line)
            if r6:
                print(r6.group(0))
                env_report.write(line)

            p7 = ".*[Ff]an.*"
            r7 = re.match(p7, line)
            if r7:
                print(r7.group(0))
                env_report.write(line)

env_report.close()

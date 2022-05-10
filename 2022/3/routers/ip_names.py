import pandas as pd
import numpy as np
import datetime as dt
import calendar

month = (dt.date.today().replace(day=1) - dt.timedelta(days=1)).month
month_name = calendar.month_abbr[month].lower()

year = dt.date.today().year
path = f"/mnt/c/Dane/UM_Warszawa/Raporty/{year}/{month}/csv/"

source_filename = path + f"routers_{month_name}_{year}.csv"

destination_filename = "ip_names.csv"
ip = pd.read_csv(source_filename)
headers = ["managementIpAddress", "hostname"]

ip.to_csv(destination_filename, index=False, columns=headers, header=False)
# with (open("ip_names.csv", mode="w")) as csv_file:
#    in_writer = csv.writer(csv_file, delimiter=",")
#
#    for pair in ip_names:
#        in_writer.writerow(pair)
#

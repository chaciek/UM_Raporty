import pandas as pd
import numpy as np

source_filename = "routers_dec_2021.csv"
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

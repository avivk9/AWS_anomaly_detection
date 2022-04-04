import time

from boto3_instance_utilization import update_time
from boto3_instance_utilization import update_cpu

import csv

with open('trycsv.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['times', 'utilizations'])

with open('trycsv.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    times = update_time()
    utilizations = update_cpu()
    for i in range(len(times)):
        writer.writerow([times[i], utilizations[i]])

import time

from boto3_instance_utilization import getTimes
from boto3_instance_utilization import getUtilizations

import csv

with open('trycsv.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['times', 'utilizations'])

while(True):
    with open('trycsv.csv', 'a', newline='') as f:
        thewriter = csv.writer(f)
        times = getTimes()
        utilizations = getUtilizations()
        for i in range(len(times)):
            thewriter.writerow([times[i], utilizations[i]])
    time.sleep(3600)
import csv
with open('trycsv.csv','w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['times', 'utilizations'])
    thewriter.writerow(['1','0.5'])
    thewriter.writerow(['2','0.6'])
    thewriter.writerow(['3','0.85'])

with open('trycsv.csv','a', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['times', 'utilizations'])
    thewriter.writerow(['1','0.5'])
    thewriter.writerow(['2','0.6'])
    thewriter.writerow(['3','0.85'])
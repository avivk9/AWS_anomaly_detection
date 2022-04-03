from boto3_instance_utilization import list_time
from boto3_instance_utilization import list_utilization

# print(f"{list_time}")
# print(f"{list_utilization}")

string = ""
list_time_first5 = []
for str in list_time:
    devided = str.split(" ")
    first5 = devided[1][0:5]
    list_time_first5.append(first5)

print(list_time_first5)
print(list_utilization)
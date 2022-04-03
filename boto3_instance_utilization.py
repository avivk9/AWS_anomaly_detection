import boto3
from datetime import datetime, timedelta
from credentials import AWS_ACCESS_KEY, AWS_SECRET_KEY

from utils.functions import stringsToFloats

# define the instance ID we'd like to inspect
INSTANCE_ID = "i-0de58090ae091a863"

# initialize tt boto3he boto3 session
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
)

# get the CloudWatch client from the session object
client = session.client("cloudwatch", region_name="us-east-1")

# get metric statistics about an EC2 instance
# docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.get_metric_statistics
list_time = []
list_utilization = []
list_time_first5 = []


def update():
    response = client.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[{"Name": "InstanceId", "Value": INSTANCE_ID}],
        StartTime=datetime.utcnow() - timedelta(seconds=3600),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=[
            "Average",
        ],
        Unit="Percent",
    )
    # inspect the datapoints
    # for datapoint in response["Datapoints"]:
    # if "Average" in datapoint:
    # print(f"Time: {datapoint['Timestamp']}, Average: {datapoint['Average']}")

    # sort the datapoints by timestamp
    datapoints_sorted = sorted(response["Datapoints"], key=lambda x: x["Timestamp"])

    # putting points of timestamp/utilization in arrays
    for datapoint in datapoints_sorted:
        list_time.append(f"{datapoint['Timestamp']}")
        list_utilization.append(f"{datapoint['Average']}")
        # print(f"{datapoint['Timestamp']}: {datapoint['Average']}")

    # setting every timestamp in a simple format
    string = ""
    for str in list_time:
        devided = str.split(" ")
        first5 = devided[1][0:5]
        list_time_first5.append(first5)


print(list_time_first5)
print(list_utilization)


def getTimes():
    update()
    return list_time_first5


def getUtilizations():
    update()
    return stringsToFloats(list_utilization)

# timestamp arry- list_time_first5
# utilization array- list_utilization

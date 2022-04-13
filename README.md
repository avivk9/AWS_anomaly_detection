AWS_anomaly_detection
===============

### Collaborators
+ __[Aviv Keinan](https://github.com/avivk9)__ 
+ __[Omer Sherer](https://github.com/OmerSherer)__ 
+ __[Sheer Shveka](https://github.com/SheerShveka)__

### Background
Made as a part of Hackathon in College Of Management & Spot by NetApp  
We were given a problem: Detect CPU anomalies from aws server and analyze them  
(also dealt with [SQL Injections problem](https://github.com/RonGreenberg/SQL-Firewall))

### The AWS Server
We created an AWS machine and upload their 2 different programs  
[One](https://github.com/avivk9/AWS_anomaly_detection/blob/main/Machine%20Codes/low_cpu_usage.py) that will demonstrate usual and normal usage  
[And another](https://github.com/avivk9/AWS_anomaly_detection/blob/main/Machine%20Codes/high_cpu_usage.py) that will demonstrate unusual extreme usage

### The Communication
Using Python and BOTO3 module we communicated with the AWS server and got information about  
the CPU utilization with possibilities to achieve more metrics in the future - [code.](https://github.com/avivk9/AWS_anomaly_detection/blob/main/boto3_instance_utilization.py)

### Analyze The Data Given
With the data came from the BOTO3 responses we created a server status.  
__Claim:__ The status calculation was based on guesses and unreliable methods  

```python
def detect(utilizations):
    last = len(utilizations) - 1
    # 0 usage
    if utilizations[last] <= 1 and utilizations[last - 1] <= 1 and utilizations[last - 2] <= 1:
        return "empty_server"
    # low usage
    if utilizations[last] <= 30 and utilizations[last - 1] <= 30 and utilizations[last - 2] <= 30:
        return "change_server_host"
    # calculate m
    m = utilizations[last] - utilizations[last - 1] / utilizations[last - 1] - utilizations[last - 2]

    # high m based on the prev one
    if m >= 2:
        return "hacked"
    # low m based on the prev one
    if m <= -2:
        return "server_cooled_hard"
    # normal
    return "normal_status"
```
### GUI
Using 'Tkinter' and 'Matplotlib' modules we presented the CPU Utilization over Time
together with the server status and a refresh button

![pic](C:\Users\Aviv\IdeaProjects\AWS_anomaly_detection\cpu graph.PNG)

![pic2](C:\Users\Aviv\IdeaProjects\AWS_anomaly_detection\cpu2.PNG)
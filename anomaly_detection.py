import details
from details import Point

import csv

class anomalyDetection:
    th = 0.9
    normalModel = []
    reports = []
    correlated_list = []
    def __init__(self):
        self.normalModel = None

class normal:
    def __init__(self, top_th, bot_th, longest_incline, longest_decline):
        self.top_th = top_th
        self.bot_th = bot_th
        self.longest_incline = longest_incline
        self.longest_decline = longest_decline


    def learnNormal(self,csvfile):
        devided = ""
        times = []
        utilizations = []
        slopes = []

        with open(csvfile) as file:
            reader = csv.reader(file)
            for row in reader:
                devided = row.split(",")
                times.append(devided[0])
                utilizations.append(devided[1])

        for i in range(len(times)-1):
            slopes[i] = (utilizations[i+1]-utilizations[i])/(times[i+1]-times[i])

        for i in range(len(slopes))




    def detect(self, times, utilizations):
        anomalys = []
        reports = []
        points = []
        for i in range(len(points)):
            points[i] = Point(times[i], utilizations[i])

        return anomalys


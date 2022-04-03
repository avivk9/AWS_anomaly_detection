import details
from controller import controller
from details import Point

import csv
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class anomalyDetection:
    th = 0.9
    normalModel = []
    reports = []
    correlated_list = []
    def __init__(self):
        self.normalModel = None



class normal:
    def __init__(self, top, bot, max_slope, min_slope):
        self.top = top
        self.bot = bot
        self.max_slope = max_slope
        self.min_slope = min_slope

    @abstractmethod
    def attach(self, observer: controller) -> None:
        pass

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

        for i in range(le)

        for i in range(len(times)-1):
            slopes[i] = (utilizations[i+1]-utilizations[i])/(times[i+1]-times[i])

        max_slope = slopes[0]
        min_slope = slopes[0]

        for i in range(len(slopes)):
            if slopes[i] > max_slope:
                max_slope = slopes[i]
            if slopes[i] < min_slope:
                min_slope = slopes[i]



    def detect(self, times, utilizations):
        anomaly = ""
        reports = []
        points = []
        for i in range(len(points)):
            points[i] = Point(times[i], utilizations[i])

        return anomaly


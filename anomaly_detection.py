import details
from controller import controller
from details import Point

import csv
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class normal:
    def __init__(self, top, bot, max_slope, min_slope):
        self.top = top * 1.1
        self.bot = bot * 1.1
        self.max_slope = max_slope * 1.1
        self.min_slope = min_slope * 0.9


class anomalyDetection:
    normalModel = []

    def __init__(self):
        self.normalModel = None

    @abstractmethod
    def attach(self, observer: controller) -> None:
        pass

    def learnNormal(self, csvfile):
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

        top = utilizations[0]
        bot = utilizations[0]
        for i in range(len(utilizations)):
            if utilizations[i] > top:
                top = utilizations[i]
            elif utilizations[i] < bot:
                bot = utilizations[i]

        for i in range(len(times) - 1):
            slopes[i] = (utilizations[i + 1] - utilizations[i]) / (times[i + 1] - times[i])

        max_slope = slopes[0]
        min_slope = slopes[0]

        for i in range(len(slopes)):
            if slopes[i] > max_slope:
                max_slope = slopes[i]
            if slopes[i] < min_slope:
                min_slope = slopes[i]

        self.normalModel = normal(top, bot, max_slope, min_slope)

    def detect(self, times, utilizations):
        anomaly = ""
        # reports = []
        # points = []
        last = len(utilizations) - 1
        # 0 usage
        if utilizations[last] <= 1 and utilizations[last - 1] <= 1 and utilizations[last - 2] <= 1:
            return "empty_server"
        # low usage
        if utilizations[last] <= 30 and utilizations[last - 1] <= 30 and utilizations[last - 2] <= 30:
            return "change_server_host"
        # calculate m
        m = utilizations[last] - utilizations[last - 1] / utilizations[last - 1] - utilizations[last - 2]

        #
        if m >= 2:
            return "hacked"
        if m <= -2:
            return "server_cooled_hard"
        return "normal_status"

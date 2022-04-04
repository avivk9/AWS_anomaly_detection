from controller import controller

import csv
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class normal:
    def __init__(self, top, bot, max_slope, min_slope, sequence0):
        self.top = top * 1.1
        self.bot = bot * 1.1
        self.max_slope = max_slope * 1.1
        self.min_slope = min_slope * 0.9
        self.sequence0 = int(sequence0 * 1.1)


class anomalyDetection:
    normalModel = []

    def __init__(self):
        self.normalModel = normal(0, 0, 0, 0, 0)

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

        # longest sequence of 0 usage
        count_sequence0 = 0
        max_sequence0 = 0
        for i in range(len(utilizations)):
            if utilizations[i] < 1:  # basically, it's 0 usage
                count_sequence0 += 1
            elif count_sequence0 > max_sequence0:
                max_sequence0 = count_sequence0
        if count_sequence0 > max_sequence0:
            max_sequence0 = count_sequence0

        for i in range(len(times) - 1):
            slopes[i] = (utilizations[i + 1] - utilizations[i]) / (times[i + 1] - times[i])

        max_slope = slopes[0]
        min_slope = slopes[0]

        for i in range(len(slopes)):
            if slopes[i] > max_slope:
                max_slope = slopes[i]
            if slopes[i] < min_slope:
                min_slope = slopes[i]

        self.normalModel = normal(top, bot, max_slope, min_slope, max_sequence0)

    def detect(self, times, utilizations):
        anomaly = ""
        last = utilizations[len(utilizations) - 1]
        # 0 usage
        if self.is_long_sequence0(utilizations):
            return "empty_server"
        # low usage
        if self.is_long_sequence_low(utilizations):
            return "change_server_host"
        if last > self.normalModel.max_slope or last < self.normalModel.min_slope:
            return "exceeded_limit"

        # calculate m
        m = (utilizations[last] - utilizations[last - 1])/(times[last]-times[last-1])

        #
        if m >= self.normalModel.max_slope:
            return "hacked"
        if m <= self.normalModel.min_slope:
            return "server_cooled_hard"
        return "normal_status"


    def is_long_sequence0(self, utilizations):
        last = len(utilizations)
        flag = True
        for i in range(self.normalModel.sequence0):
            flag = flag and utilizations[last - i] <= 1
        return flag

    def is_long_sequence_low(self, utilizations):
        last = len(utilizations)
        flag = True
        for i in range(self.normalModel.sequence0):
            flag = flag and utilizations[last - i] <= 30
        return flag
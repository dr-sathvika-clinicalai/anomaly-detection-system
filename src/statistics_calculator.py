import math

class StatisticsCalculator:
    def __init__(self,values):
        self.values = values

    def mean(self):
        return sum(self.values)/len(self.values)

    def variance(self):
        mean_value = self.mean()
        squared_diff_sum = 0

        for value in self.values:
            squared_diff_sum += (value - mean_value) ** 2

        return squared_diff_sum/ len(self.values)

    def standard_deviation(self):
        return math.sqrt(self.variance())
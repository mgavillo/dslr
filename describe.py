import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import sys
import seaborn as sns

class Describe():

    def __init__(self, data):
        self.data = data
        self.dataNum = data.iloc[:,6:]
        self.dataSorted = self.dataNum.transform(np.sort)
        self.N = len(self.dataNum.columns)
        self.count = [0 for x in range(self.N)]
        self.mean = self.count[:]

    def calc_count_mean(self):
        '''
        for each feature, calulate count without blank input
        then calculate average
        '''
        for index, column in enumerate(self.dataNum.columns):
            self.count[index] = self.dataNum[column].notnull().sum()
            for d in self.dataNum[column]:
                if not math.isnan(d):
                    self.mean[index] += d
            self.mean[index] /= self.count[index]        

    def calc_std(self):
        '''
        for each feature, calculate standart deviation, a measure of
        the spread of a distribution

        sdt = sqrt(mean(abs(x - x.mean())**2))
        '''
        std = [0 for x in range(self.N)]
        for index, column in enumerate(self.dataNum):
            deviations = []
            for x in self.dataNum[column]:
                if not math.isnan(x):
                    deviations.append((x - self.mean[index]) ** 2)
            variance = sum(deviations) / self.count[index]
            std[index] = math.sqrt(variance)
        return std

    def calc_percentile(self, perc, j, index):
        x = perc * self.count[index]
        i = int(x)
        ret = self.dataSorted[j][i] + ((x - int(x)) * (self.dataSorted[j][i + 1] - self.dataSorted[j][i]))
        return ret

    def calc_percentiles(self):
        self.perc = self.dataNum
        self.perc = self.perc.transform(np.sort)

        min = [0 for x in range(self.N)]
        max = min[:]
        q1 = min[:]
        q2 = min[:]
        q3 = min[:]
        for index, column in enumerate(self.dataSorted):
            q1[index] = self.calc_percentile(0.25, column, index)
            q2[index] = self.calc_percentile(0.5, column, index)
            q3[index] = self.calc_percentile(0.75, column, index)
            min[index] = self.dataSorted[column][0]
            max[index] = self.dataSorted[column][self.count[index] - 1]
        return q1, q2, q3, min, max

    def show(self):
        self.calc_count_mean()
        std = self.calc_std()
        q1, q2, q3, min, max = self.calc_percentiles()
        d = [self.count, self.mean, std, min, q1, q2, q3, max]
        df = pd.DataFrame(d, columns = self.dataNum.columns, index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"])
        print(df)

if __name__ == "__main__":
    data = pd.read_csv(sys.argv[1])
    describe = Describe(data)
    describe.show()
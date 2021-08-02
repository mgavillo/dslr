import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

import seaborn as sns



dataNum = data.iloc[:,6:]
N = len(dataNum.columns)
min = [0 for x in range(N)]
max = min[:]
count = min[:]
mean = min[:]
q1 = min[:]
q2 = min[:]
q3 = min[:]
std = min[:]


        data = pd.read_csv(sys.argv[1])

    def read_and_clean():

    def calc_count_mean():
        '''
        for each feature, calulate count without blank input
        then calculate average
        '''
        count = min[:]
        mean = min[:]
        for index, column in enumerate(dataNum.columns):
            count[index] = dataNum[column].notnull().sum()
            for d in dataNum[column]:
                if not math.isnan(d):
                    mean[index] += d
            mean[index] /= count[index]        

    def calc_std():
        '''
        for each feature, calculate standart deviation, a measure of
        the spread of a distribution

        sdt = sqrt(mean(abs(x - x.mean())**2))
        '''
        std = [0 for x in range(N)]
        for index, column in enumerate(dataNum):
            deviations = []
            for x in dataNum[column]:
                if not math.isnan(x):
                    deviations.append((x - mean[index]) ** 2)
            variance = sum(deviations) / count[index]
            std[index] = math.sqrt(variance[index])
        return(std)

data_process.calc_count_mean()
data_process.calc_std()
percentile = dataNum

percentile = percentile.transform(np.sort)
for index, column in enumerate(percentile):
    i = 0.75 * count[index]
    i2 = 0.5 * count[index]
    # print(math.floor(0.25 * count[index]))
    # print(math.ceil(0.25 * count[index]))
    x = 0.25 * (count[index] + 1)
    i = int(x)
    q1[index] = percentile[column][i]
    if not x.is_integer():
        print(x - int(x))
        q1[index] += (x - int(x)) * (percentile[column][i + 1] -  percentile[column][i])
    q2[index] = percentile[column][math.floor(0.5 * count[index]) - 1]
    q3[index] = percentile[column][math.floor(0.75 * count[index]) - 1]
    min[index] = percentile[column][0]
    max[index] = percentile[column][count[index] - 1]

data_process(sys.argv[1])
print()
print(percentile)
print(dataNum.describe())

d = [count, mean, std, min, q1, q2, q3, max]
df = pd.DataFrame(d, columns = dataNum.columns, index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"])
print(df)

    
import csv
import numpy as np
import pandas as pd
import math

data = pd.read_csv("./datasets/dataset_train.csv")

dataNum = data.iloc[:,6:]
print(dataNum.describe())
N = len(dataNum.columns)
min = [0 for x in range(N)]
max = min[:]
count = min[:]
mean = min[:]
p25 = min[:]
p50 = min[:]
p75 = min[:]
variance = min[:]
std = min[:]
for index, column in enumerate(dataNum):
    min[index] = dataNum[column][0]
    max[index] = min[index]
    count[index] = dataNum[column].notnull().sum()
    for d in dataNum[column]:
        if not math.isnan(d):
            # print(d)
            if min[index] > d or math.isnan(min[index]):
                min[index] = d
            elif max[index] < d or math.isnan(max[index]):
                max[index] = d
            mean[index] += d / count[index]

for index, column in enumerate(dataNum):
    deviations = []
    for x in dataNum[column]:
        if not math.isnan(x):
            deviations.append((x - mean[index]) ** 2)
    variance[index] = sum(deviations) / count[index]
    std[index] = math.sqrt(variance[index])



percentile = dataNum
print()
print(percentile.columns.tolist())
percentile = percentile.transform(np.sort)
for index, column in enumerate(dataNum):
    i = 0.75 * count[index]
    i2 = 0.5 * count[index]

    print(i)
    print(i2)
    print(dataNum[column][int(i)])
print()
print(percentile)
d = [count, mean, std, min, p25, p50, p75, max]
df = pd.DataFrame(d, columns = dataNum.columns, index=["count", "mean", "std", "min", "25%", "50%", "75%", "max"])
print(df)

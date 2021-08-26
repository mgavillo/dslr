import sys
import csv
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import argparse


class Describe():
    def __init__(self, data):
        self.data = data
        self.dataNum = self.data_to_dataNum(data)
        self.dataSorted = self.dataNum.transform(np.sort)
        self.N = len(self.dataNum.columns)
        self.count, self.mean = self.calc_count_mean(self.dataNum)
        self.std = self.calc_std(self.dataNum)

    def data_to_dataNum(self, data):
        '''
        Param : dataset with categorical and numerical values
            check if type of column isn't float64
            if so create new array with other features
        Return : dataset with only numerical values
        '''
        for index, feature in enumerate(data):
            if data[feature].dtype != np.float64:
                new_features = [x for x in data.columns if x != feature]
                data = data.loc[:, new_features]
        return data

    def calc_count_mean(self, data):
        '''
        for each feature, calulate count without blank input
        then calculate average
        '''
        count = [0 for x in range(self.N)]
        mean = [0 for x in range(self.N)]
        for index, column in enumerate(data.columns):
            count[index] = data[column].notnull().sum()
            for d in data[column]:
                if not math.isnan(d):
                    mean[index] += d
            mean[index] /= count[index]
        return count, mean

    def calc_std(self, data):
        '''
        for each feature, calculate standart deviation, a measure of
        the spread of a distribution

        sdt = sqrt(mean(abs(x - x.mean())**2))
        '''
        std = [0 for x in range(self.N)]
        for index, column in enumerate(data):
            deviations = []
            for x in data[column]:
                if not math.isnan(x):
                    deviations.append((x - self.mean[index]) ** 2)
            variance = sum(deviations) / self.count[index]
            std[index] = math.sqrt(variance)
        return std     

    def calc_min_max(self):
        '''
        return min max calculated with sorted data
        '''
        min = [0 for x in range(self.N)]
        max = [0 for x in range(self.N)]
        for index, column in enumerate(self.dataSorted):
            min[index] = self.dataSorted[column][0]
            max[index] = self.dataSorted[column][self.count[index] - 1]
        return min, max
   
    def calc_percentile(self, perc, j, index) -> float:
        '''
        calculate percentile dealing with float index
        '''
        float_i = perc * self.count[index]
        i = int(float_i)                            
        floor = self.dataSorted[j][i]
        ceil = self.dataSorted[j][i + 1]
        dec_i = float_i - int(float_i)
        value = (floor + (dec_i * (ceil - floor)))
        return value

    def calc_percentiles(self):
        q1 = [0 for x in range(self.N)]
        q2 = [0 for x in range(self.N)]
        q3 = [0 for x in range(self.N)]
        for index, column in enumerate(self.dataSorted):
            q1[index] = self.calc_percentile(0.25, column, index)
            q2[index] = self.calc_percentile(0.5, column, index)
            q3[index] = self.calc_percentile(0.75, column, index)
        return q1, q2, q3

    def show(self):
        '''
        calculate measuring values
        show data as a pandas dataframe
        '''
        q1, q2, q3 = self.calc_percentiles()
        min, max = self.calc_min_max()
        d = [self.count, self.mean, self.std, min, q1, q2, q3, max]
        df = pd.DataFrame(d, columns = self.dataNum.columns,
                index=["count",
                        "mean",
                        "std",
                        "min",
                        "25%",
                        "50%",
                        "75%",
                        "max"])
        print(df)

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_args()
    data = pd.read_csv(args.data)
    describe = Describe(data)
    describe.show()
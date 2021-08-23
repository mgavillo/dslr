from describe import Preprocess

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def show_pair_plot(data):
    dataNum = data.dataNum
    dataNum["Hogwarts House"] = data.data["Hogwarts House"]
    dataNum = dataNum.dropna()
    sns.pairplot(dataNum, hue="Hogwarts House", markers = ".", height=1)
    my_path = os.path.dirname(__file__)
    my_file = "plot/pair_plot.png"
    plt.savefig(os.path.join(my_path, my_file))
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    args = parser.parse_args()
    data = pd.read_csv(args.data)
    d = Preprocess(data)
    show_pair_plot(d)
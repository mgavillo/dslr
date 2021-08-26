from describe import Describe

import os
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def subject_split_houses(dataNum, data, subject):
    '''
    split values of given subject in four house arrays
    '''
    houses = "Hogwarts House"
    Gryffindor = dataNum.loc[data[houses] == "Gryffindor"][subject]
    Slytherin = dataNum.loc[data[houses] == "Slytherin"][subject]
    Ravenclaw = dataNum.loc[data[houses] == "Ravenclaw"][subject]
    Hufflepuff = dataNum.loc[data[houses] == "Hufflepuff"][subject]
    return Gryffindor, Slytherin, Ravenclaw, Hufflepuff

def legend_plot():
    plt.legend()
    plt.title("correlated features")
    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the Dark Arts")

def show_pair_plot(data, f1, f2):
    Gry1, Sly1, Rav1, Huf1 = subject_split_houses(data.dataNum, data.data,f1)
    Gry2, Sly2, Rav2, Huf2 = subject_split_houses(data.dataNum,data.data, f2)
    plt.figure()
    plt.scatter(Gry1, Gry2, label = "Gryffindor", color='r')
    plt.scatter(Sly1, Sly2, label = "Slytherin", color='y')
    plt.scatter(Rav1, Rav2, label = "Ravenclaw", color='g')
    plt.scatter(Huf1, Huf2, label = "Hufflepuff", color='b')
    legend_plot()
    plt.show()

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    parser.add_argument('--feature1',
        type=str, help="First feature to scatter",
        default="Defense Against the Dark Arts")
    parser.add_argument('--feature2',
        type=str, help="Second feature to scatter",
        default="Astronomy")
    return parser.parse_args()

def save_plot(file_name):
    _path = os.path.dirname(__file__)
    plt.savefig(os.path.join(_path, file_name))

if __name__ == "__main__":
    args = _parse_args()
    data = pd.read_csv(args.data)
    d = Describe(data)
    show_pair_plot(d, args.feature1, args.feature2)
    save_plot("plot/scatter_plot.png")
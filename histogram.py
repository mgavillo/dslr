from describe import Describe

import os
import matplotlib.pyplot as plt
import argparse
import pandas as pd

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


def show_histrogram(data):
    Gryffindor, Slytherin, Ravenclaw, Hufflepuff
            = subject_split_houses(data.dataNum, data.data, 'Aritmancy')
    plt.figure()
    plt.hist(Gryffindor, bins=25, alpha=0.5, label = 'Gry', color = 'r')
    plt.hist(Ravenclaw, bins=25, alpha=0.5, label = 'Rav', color = 'b')
    plt.hist(Slytherin, bins=25, alpha=0.5, label = 'Sly', color = 'g')
    plt.hist(Hufflepuff, bins=25, alpha=0.5, label = 'Huf', color = 'y')
    plt.legend(loc = 'upper right')
    plt.title(subject)
    plt.show()

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    return parser.parse_args()

def save_plot(file_name):
    _path = os.path.dirname(__file__)
    plt.savefig(os.path.join(_path, file_name))

if __name__ == "__main__":
    args = _parse_args()
    data = pd.read_csv(args.data)
    d = Describe(data)
    show_histrogram(d)
    save_plot("plot/histogram.png")


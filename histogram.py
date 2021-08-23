from describe import Preprocess

import os
import matplotlib.pyplot as plt
import argparse
import pandas as pd

def show_histrogram(data):
    d = data.dataNum
    data = data.data
    house = "Hogwarts House"
    subject = "Arithmancy"
    Gryffindor = d.loc[data[house] == "Gryffindor"][subject]
    Slytherin = d.loc[data[house] == "Slytherin"][subject]
    Ravenclaw = d.loc[data[house] == "Ravenclaw"][subject]
    Hufflepuff = d.loc[data[house] == "Hufflepuff"][subject]
    plt.figure()
    plt.hist(Gryffindor, bins=25, alpha=0.5, label = 'Gry', color = 'r')
    plt.hist(Ravenclaw, bins=25, alpha=0.5, label = 'Rav', color = 'b')
    plt.hist(Slytherin, bins=25, alpha=0.5, label = 'Sly', color = 'g')
    plt.hist(Hufflepuff, bins=25, alpha=0.5, label = 'Huf', color = 'y')
    plt.legend(loc = 'upper right')
    plt.title(subject)
    my_path = os.path.dirname(__file__)
    my_file = "plot/histogram.png"
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
    show_histrogram(d)


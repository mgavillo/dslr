from describe import Describe

import os
import pandas as pd
import matplotlib.pyplot as plt
import argparse

def show_pair_plot(data):
    dataNum = data.dataNum
    data = data.data
    house = "Hogwarts House"
    subject1 = "Defense Against the Dark Arts"
    subject2 = "Astronomy"
    
    Gryffindor = dataNum.loc[data[house] == "Gryffindor"][subject1]
    Gryffindor2 = dataNum.loc[data[house] == "Gryffindor"][subject2]

    Slytherin = dataNum.loc[data[house] == "Slytherin"][subject1]
    Slytherin2 = dataNum.loc[data[house] == "Slytherin"][subject2]

    Ravenclaw = dataNum.loc[data[house] == "Ravenclaw"][subject1]
    Ravenclaw2 = dataNum.loc[data[house] == "Ravenclaw"][subject2]

    Hufflepuff = dataNum.loc[data[house] == "Hufflepuff"][subject1]
    Hufflepuff2 = dataNum.loc[data[house] == "Hufflepuff"][subject2]
    
    plt.figure()
    plt.scatter(Gryffindor, Gryffindor2, label = "Gryffindor", color='r')
    plt.scatter(Slytherin, Slytherin2, label = "Slytherin", color='y')
    plt.scatter(Ravenclaw, Ravenclaw2, label = "Ravenclaw", color='g')
    plt.scatter(Hufflepuff, Hufflepuff2, label = "Hufflepuff", color='b')
    plt.legend()
    plt.title("correlated features")
    plt.xlabel("Astronomy")
    plt.ylabel("Defense Against the Dark Arts")
    my_path = os.path.dirname(__file__)
    my_file = "plot/scatter_plot.png"
    plt.savefig(os.path.join(my_path, my_file))
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    args = parser.parse_args()
    data = pd.read_csv(args.data)
    d = Describe(data)
    show_pair_plot(d)
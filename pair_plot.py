from describe import Describe

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def prepare_data(data):
    dataPlot = data.dataNum
    dataPlot["Hogwarts House"] = data.data["Hogwarts House"]
    dataPlot = dataPlot.dropna()
    return(dataPlot)

def confing_plot(plot):
    plot.fig.set_figheight(10)
    plot.fig.set_figwidth(17)
    for ax in plot.axes.flatten():
        ax.set_ylabel(ax.get_ylabel(), rotation = 60) #rotates labels of y axis to see them
        ax.yaxis.get_label().set_horizontalalignment('right')

def show_pair_plot(data):
    dataPlot = prepare_data(data)
    sns.set(style="whitegrid", font_scale=0.5)  #font size of labels
    plot = sns.pairplot(dataPair,
        hue="Hogwarts House",                  #diferencing colors
        markers = ".",
        height=1,                              #height of figure
        aspect=1,                              #widht of figure
        plot_kws = {'linewidth':0})            #delete point borders for scatter plots
    config_plot(plot)
    plt.show()

def save_plot(file_name):
    _path = os.path.dirname(__file__)
    plt.savefig(os.path.join(_path, file_name))

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    return parser.parse_args()

if __name__ == "__main__":
    args = _parse_args()
    data = pd.read_csv(args.data)
    d = Describe(data)
    show_pair_plot(d)
    save_plot("plot/pair_plot.png")



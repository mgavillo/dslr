from describe import Describe

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import argparse

def show_pair_plot(data):
    dataPair = data.dataNum
    dataPair["Hogwarts House"] = data.data["Hogwarts House"]
    dataPair = dataPair.dropna()
    sns.set(style="whitegrid", font_scale=0.5)
    plot = sns.pairplot(dataPair,
        hue="Hogwarts House",
        diag_kind="hist",
        markers = ".",
        height=1,
        aspect=1,
        plot_kws = {'edgecolor':"r", # for edge color
             'linewidth':0, # line width of spot
             'linestyle':'--', # line style of spot
            })
    plot.fig.set_figheight(10)
    plot.fig.set_figwidth(17)
    for ax in plot.axes.flatten():
    #     ax.set_xlabel(ax.get_xlabel(), rotation = 60)
        ax.set_ylabel(ax.get_ylabel(), rotation = 60)
        ax.yaxis.get_label().set_horizontalalignment('right')
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
    d = Describe(data)
    show_pair_plot(d)



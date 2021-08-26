import os
from logreg_train import LogisticRegression
import numpy as np
import pandas as pd
import argparse
import csv
import sys

def save_csv(ret):
    ret = np.array(ret)    
    f = open('./houses.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['Index','Hogwarts House'])
    writer.writerows(enumerate(ret))
    f.close()
    print("Predicted houses saved in weights.py")

def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    parser.add_argument('-w', '--weights',
        type=str, help="npy file containing the weights",
        default="weights.npy")
    return parser.parse_args()

def load_weights(w):
    try:
        w = np.load(w, allow_pickle = True)
    except OSError:
        sys.exit("Please train model before predict")
    return w

if __name__ == "__main__":
    args = _parse_args()        
    data = pd.read_csv(args.data)
    lr = LogisticRegression(data)
    weights = load_weights(args.weights)
    lr.update_weights(weights)
    ret = lr.predict(np.array(lr.features))
    save_csv(ret)
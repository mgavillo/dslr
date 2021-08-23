from logreg_train import LogisticRegression
import numpy as np
import pandas as pd
import argparse
import csv

def save_ret(ret):
    ret = np.array(ret)    
    f = open('./houses.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(['Index','Hogwarts House'])
    writer.writerows(enumerate(ret))
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    parser.add_argument('-w', '--weights',
        type=str, help="npy file containing the weights",
        default="weights.npy")
    args = parser.parse_args()
    data = pd.read_csv(args.data)

    lr = LogisticRegression(data)
    weights = np.load(args.weights, allow_pickle = True)
    lr.update_weights(weights)
    ret = lr.predict(np.array(lr.features))
    save_ret(ret)
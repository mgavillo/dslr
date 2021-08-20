from describe import Describe
import numpy as np
import pandas as pd
import argparse



class LogisticRegression():
    def __init__(self, data):
        self.d = Describe(data)
        self.d.data = self.d.data.dropna()
        self.d.calc_count_mean()
        self.d.calc_std()
        self.mean = self.d.mean
        self.std = self.d.std
        self.features = self.d.dataNum.dropna()
        self.features = self.features.loc[:, ['Herbology', 'Defense Against the Dark Arts',
                   'Ancient Runes', 'Charms']]
        print(self.features)
        self.labels = np.array(self.d.data.loc[:,"Hogwarts House"])
        self.n_iter = 30000
        self.eta=5e-5
        self.weights= []
        self.normalize()

    def normalize(self):
        print("COUCOU")
        for index, column in enumerate(self.features):
            for x in self.features[column]:
                x = (x - self.mean[index]) / self.std[index]

    def _sigmoid(self, X):
        return 1 / (1 + np.exp(-X))

    def fit(self):
        X = np.array(self.features, dtype=np.float128)
        # X = np.insert(X, 0, 1, axis=1)
        for house in np.unique(self.labels):
            expected_y = np.where(self.labels == house, 1, 0)
            w = np.ones(X.shape[1])
            for _ in range(self.n_iter):
                x = X.dot(w)
                probability = self._sigmoid(x)
                gradient = np.dot(X.T, (expected_y - probability))
                w += self.eta * gradient
            self.weights.append((w, house))
        print(self.weights)
        print(len(self.weights[0]))
        print(len(self.weights[1]))

        np.save("weights", self.weights)
            # errors = y - self._sigmoid(z)

    def _predict_one(self, x):

        # for w,c in self.weights:
        #     print(x.dot(w), c)
        # print("--------------------")
        i = max((x.dot(w), c) for w,c in self.weights)[1]
        return i
    
    def predict(self, X):
        return [self._predict_one(i) for i in X]
    
    def score(self):

        p = self.predict(np.array(self.features))
        print(self.labels[39], p[39])
        return sum(p == self.labels) / len(self.labels) 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data',
        type=str, help="CSV file containing the dataset",
        default="./datasets/dataset_train.csv")
    args = parser.parse_args()
    data = pd.read_csv(args.data)
    lr = LogisticRegression(data)
    lr.fit()
    print("Score = ", lr.score())

from describe import Describe
import numpy as np
import pandas as pd
import argparse
from sklearn.metrics import accuracy_score

class LogisticRegression():
    def __init__(self, data, n_iter = 30000, eta = 1e-5):
        self.data = data.loc[:,
            ['Hogwarts House', 'Herbology',
            'Defense Against the Dark Arts',
            'Ancient Runes',
            'Charms', 'Divination']]
        self.d = Describe(self.data)
        self.mean = self.d.mean
        self.std = self.d.std
        self.features = self.d.dataNum
        self.labels = self.data.iloc[:, 0]
        self.n_iter = n_iter
        self.eta = eta
        self.weights = []
        self.fight_against_nan()
        self.normalize()

    def normalize(self):
        for index, column in enumerate(self.features):
            _min, _max = self.d.calc_min_max()
            for i, x in enumerate(self.features[column]):
                self.features[column][i] = (x - _min[index]) / (_max[index] - _min[index])
        print(self.features)

    def fight_against_nan(self):
        for index, column in enumerate(self.features):
            i = 0
            for i, x in enumerate(self.features[column]):
                if np.isnan(x):
                    self.features[column][i] = self.mean[index]
                    
    def _sigmoid(self, X):
        return 1 / (1 + np.exp(-X))

    def fit(self):
        X = np.array(self.features, dtype=np.float128)
        for house in np.unique(self.labels):
            expected_y = np.where(self.labels == house, 1, 0)
            w = np.ones(X.shape[1])
            for _ in range(self.n_iter):
                x = X.dot(w)
                probability = self._sigmoid(x)
                gradient = np.dot(X.T, (expected_y - probability))
                w += self.eta * gradient
            self.weights.append((w, house))
        np.save("weights", np.array(self.weights, dtype=object))

    def _predict_one(self, x):
        return max((x.dot(w), c) for w,c in self.weights)[1]
    
    def predict(self, X):
        return [self._predict_one(i) for i in X]
    
    def score(self):
        p = self.predict(np.array(self.features))
        return sum(p == self.labels) / len(self.labels) 
    
    def _sklearn_score(self):
        y_pred = self.predict(np.array(self.features))
        return(accuracy_score(self.labels, y_pred))

    def update_weights(self, weights):
        self.weights = weights


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
    print('sklearn_score = ', lr._sklearn_score())

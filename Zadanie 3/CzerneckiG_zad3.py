import numpy as np
import csv

class kNNClassifier:
    def __init__(self, k=3, distance='euclidean'):
        self.k = k
        self.distance = distance
        self.X_train = None
        self.y_train = None

    def train(self, X_train, y_train):
        if self.X_train is None:
            self.X_train = X_train
            self.y_train = y_train
        else:
            self.X_train = np.vstack((self.X_train, X_train))
            self.y_train = np.concatenate((self.y_train, y_train))

    def predict(self, X_test):
        if self.distance == 'euclidean':
            dist_func = self.euclidean_distance
        elif self.distance == 'manhattan':
            dist_func = self.manhattan_distance
        elif self.distance == 'maximum':
            dist_func = self.maximum_distance
        elif self.distance == 'cosine':
            dist_func = self.cosine_distance
        else:
            raise ValueError('Invalid distance function')

        y_pred = []
        for x in X_test:
            distances = [dist_func(x, x_train) for x_train in self.X_train]
            k_indices = np.argpartition(distances, self.k)[:self.k]
            k_labels = self.y_train[k_indices]
            unique_labels, counts = np.unique(k_labels, return_counts=True)
            pred_label = unique_labels[np.argmax(counts)]
            y_pred.append(pred_label)

        return np.array(y_pred)

    def euclidean_distance(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    def manhattan_distance(self, x1, x2):
        return np.sum(np.abs(x1 - x2))

    def maximum_distance(self, x1, x2):
        return np.max(np.abs(x1 - x2))

    def cosine_distance(self, x1, x2):
        dot_product = np.dot(x1, x2)
        norm_product = np.linalg.norm(x1) * np.linalg.norm(x2)
        return 1 - (dot_product / norm_product)


def load_dataset(filename):
    dataset = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        for row in csv_reader:
            dataset.append([float(value) for value in row])
    return np.array(dataset)

def split_dataset(dataset):
    X = dataset[:, :-1]
    y = dataset[:, -1].astype(int)
    return X, y

def accuracy(y_true, y_pred):
    correct = np.sum(np.logical_and(np.isfinite(y_true), np.isfinite(y_pred), y_true == y_pred))
    total = np.sum(np.isfinite(y_true))
    if total > 0:
        return correct / total
    else:
        return 0.0

def cross_validation(X, y, classifier, k_values):
    num_folds = 5
    fold_size = len(X) // num_folds
    accuracies = []

    for k in k_values:
        k_accuracies = []
        for i in range(num_folds):
            start = i * fold_size
            end = (i + 1) * fold_size
            X_test_fold = X[start:end]
            y_test_fold = y[start:end]
            X_train_fold = np.concatenate((X[:start], X[end:]))
            y_train_fold = np.concatenate((y[:start], y[end:]))

            classifier.train(X_train_fold, y_train_fold)
            y_pred_fold = classifier.predict(X_test_fold)
            fold_accuracy = accuracy(y_test_fold, y_pred_fold)
            k_accuracies.append(fold_accuracy)

        mean_accuracy = np.mean(k_accuracies)
        accuracies.append(mean_accuracy)

    return accuracies


dataset_files = ["dataset0.csv", "dataset1.csv", "dataset2.csv"]
datasets = []
for file in dataset_files:
    dataset = load_dataset(file)
    datasets.append(dataset)

k_values = [1, 3, 5]
distance_functions = ['euclidean', 'manhattan', 'maximum', 'cosine']

for dataset in datasets:
    X, y = split_dataset(dataset)
    classifier = kNNClassifier()

    for distance in distance_functions:
        classifier.distance = distance
        accuracies = cross_validation(X, y, classifier, k_values)

        print(f"Dataset: {dataset_files[datasets.index(dataset)]}")
        print(f"Distance function: {distance}")
        print(f"K values: {k_values}")
        print(f"Accuracies: {accuracies}")
        print()

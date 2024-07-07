import os
import pickle
import sys
import numpy as np
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier


def train(X, y, seed, n_est, min_split):
    """
    Train a random forest classifier.

    Args:
        X: features
        y: target column
        seed (int): Random seed.
        n_est (int): Number of trees in the forest.
        min_split (int): Minimum number of samples required to split an internal node.

    Returns:
        sklearn.ensemble.RandomForestClassifier: Trained classifier.
    """

    clf = RandomForestClassifier(
        n_estimators=n_est, min_samples_split=min_split, n_jobs=2, random_state=seed
    )

    clf.fit(X, y)

    return clf


def main():
    params = yaml.safe_load(open("params.yaml"))["train"]

    if len(sys.argv) != 3:
        sys.stderr.write("Arguments error. Usage:\n")
        sys.stderr.write("\tpython train.py features model\n")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]
    seed = params["seed"]
    n_est = params["n_est"]
    min_split = params["min_split"]

    # Load the data
    train_df = pd.read_csv(os.path.join(input, 'train_encoded.csv'))
    X = train_df.iloc[:, 1:]
    y = train_df.iloc[:, 0]

    clf = train(X, y, seed=seed, n_est=n_est, min_split=min_split)

    # Save the model
    with open(output, "wb") as fd:
        pickle.dump(clf, fd)


if __name__ == "__main__":
    main()

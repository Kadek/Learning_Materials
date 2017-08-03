import numpy as np
import matplotlib.pyplot as plt


def testbed(n_set, n_arms, n_iter):
    test = [0] * n_arms
    for i in range(n_set):
        arms = [np.random.normal() for _ in range(n_arms)]
        test = list(map(lambda x, y: x+y, arms, test))
    test = list(map(lambda x: x/i, test))
    return test


def binnify(n_bins, data):
    bins = [0]*(n_bins+1)

    max_val = max(data)
    min_val = min(data)
    span = abs(max_val-min_val)/n_bins

    min_val = abs(min_val)
    for x in data:
        bins[round((x + min_val)/span)] += 1

    return bins


def show_data(data):
    print(data)
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    data = testbed(2000, 100000, 100)
    bins = binnify(10, data)
    show_data(bins)

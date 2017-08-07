import numpy as np
import matplotlib.pyplot as plt
import random

def testbed(n_set, n_arms, n_iter, epsilon):
    """Implementation of exercise 2.2

    from Reinforcement Learning: An Introduction
    by Richard S. Sutton and Andrew G. Barto

    """
    performance = [0] * n_iter

    for i in range(n_set):
        value = [0] * n_arms
        value_n = [0] * n_arms

        arms = [np.random.normal() for _ in range(n_arms)]

        for j in range(n_iter):

            test = np.random.rand()

            # if less than epsilon then explore
            if(test < epsilon):
                index = random.randint(0, n_arms-1)
            else:
                max_value = max(value)
                index = value.index(max_value)

            new_value = compute_value(index, value, value_n, arms)

            update_performance(performance, j, i, new_value)

    return performance

def update_performance(performance, curr_iter, curr_set, value):
    performance[curr_iter] = (performance[curr_iter]*curr_set + value)/(curr_set+1)

def compute_value(index, value, value_n, arms):
    """Function handles updating values

    """

    new_value = arms[index] + np.random.normal()

    value[index] = (value[index]*value_n[index] + new_value)
    value_n[index] += 1
    value[index] /= value_n[index]

    return new_value

def binnify(n_bins, data):
    """Puts data into equal sized bins

    n_bins : amount of bins
    data : data to puts in bins

    Not very generic
    """

    bins = [0]*(n_bins+1)

    max_val = max(data)
    min_val = min(data)
    span = abs(max_val-min_val)/n_bins

    min_val = abs(min_val)
    for x in data:
        bins[round((x + min_val)/span)] += 1

    return bins


def show_data(data, labels):
    print(data)
    for row in data:
        plt.plot(row)

    plt.legend(labels)
    plt.show()

if __name__ == "__main__":

    epsilons = [0, 0.01, 0.1, 0.5, 1]

    data = []
    for epsilon in epsilons:
        data.append(testbed(2000, 10, 1000, epsilon))
        print("Calculation for epsilon={} ready".format(epsilon))

    show_data(data, epsilons)

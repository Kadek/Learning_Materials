import numpy as np
import matplotlib.pyplot as plt
import random

def testbed(n_set, n_arms, n_iter, select_index, select_parameter):
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

            index = select_index(value, n_arms, select_parameter);

            new_value = compute_value(index, value, value_n, arms)

            update_performance(performance, j, i, new_value)

    return performance

def epsilon_select(value, n_arms, epsilon):
    """Select function

    Chooses randomly from all possibilities.
    Chance of that happening is equal to epsilon.

    """

    test = np.random.rand()

    # if less than epsilon then explore
    if (test < epsilon):
        index = random.randint(0, n_arms - 1)
    else:
        max_value = max(value)
        index = value.index(max_value)

    return index

def softmax_select(value, n_arms, temp):
    """Select function

    Chooses randomly from Gibbs Distribution of possible values

    """

    # generate Gibbs distribution
    e_values = list(map(lambda x: np.math.exp(x/temp), value))
    sum_e = sum(e_values)

    if(sum_e == 0):
        return 0

    e_values = list(map(lambda x: x/sum_e, e_values))

    # find random index
    test = np.random.rand()
    i = 0
    for e_value in e_values:
        test -= e_value
        if(test <= 0):
            return i
        i += 1

    return i

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

def show_data(data, labels):
    for row in data:
        plt.plot(row)

    plt.legend(labels)
    plt.show()

if __name__ == "__main__":

    """epsilons = [0, 0.01, 0.1, 0.5, 1]

    data = []
    for epsilon in epsilons:
        data.append(testbed(2000, 10, 1000, epsilon_select, epsilon))
        print("Calculation for epsilon={} ready".format(epsilon))

    show_data(data, epsilons)
    """

    temperatues = [0.01, 0.05, 0.1]

    data = []
    for temperatue in temperatues:
        data.append(testbed(2000, 10, 1000, softmax_select, temperatue))
        print("Calculation for temperature={} ready".format(temperatue))

    show_data(data, temperatues)
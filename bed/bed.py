import numpy as np
import matplotlib.pyplot as plt
import random

def testbed(n_set, n_arms, n_iter, select_index, select_parameter, action_value_function, step=0):
    """Implementation of exercise 2.2

    from Reinforcement Learning: An Introduction
    by Richard S. Sutton and Andrew G. Barto

    """
    performance = [0] * n_iter

    for i in range(n_set):
        value = [0] * n_arms
        value_n = [1] * n_arms

        arms = [np.random.random()  - 0.5] * n_arms
        value_history = list(map(lambda x: [x], arms))

        for j in range(n_iter):

            index = select_index(value, n_arms, select_parameter);

            (new_value, arms) = compute_value(index, value, value_n, arms, action_value_function, step, value_history)

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
    try:
        e_values = list(map(lambda x: np.math.exp(x/temp), value))
    except Exception:
        print("You temperature is too low! Math overflow error.")
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

def compute_value(chosen_arm_index, value, value_n, arms, action_value_function, step, value_history):
    """Function handles updating values

    Currently:
    - computation of action-values
    - random walk for true values

    """

    # computation of action-values
    new_value = arms[chosen_arm_index] + np.random.normal()

    action_value_function(chosen_arm_index, value, value_n, new_value, step, value_history)

    # random walk for true values
    arms = list(map(lambda x: x + np.random.random() - 0.5, arms))

    return (new_value, arms)

def incremental_average_action_value(chosen_arm_index, value, value_n, new_value, step, value_history):
    """Computing action values

    Simple incremental determination of average value

    """
    value[chosen_arm_index] = value[chosen_arm_index] + (1/value_n[chosen_arm_index])*(new_value-value[chosen_arm_index])
    value_n[chosen_arm_index] += 1

def constant_step_action_value(chosen_arm_index, value, value_n, new_value, step, value_history):
    """Computing action values

    Uses constant step value to compute weighted average value

    value_history is a monstrosity,
    array where first element is the first average value
    and then we start storing rewards.

    """
    value_history[chosen_arm_index].append(new_value)
    tmp = np.power(1-step, len(value_history[chosen_arm_index]) - 1)
    tmp *= value_history[chosen_arm_index][0]

    for i in range(1,len(value_history[chosen_arm_index])):
        tmp = pow(1-step, len(value_history[chosen_arm_index]) - i - 1)*step*value_history[chosen_arm_index][i]

    value[chosen_arm_index] = tmp


def add_plot_data(data, labels):
    for row in data:
        plt.plot(row)

    plt.legend(labels)

if __name__ == "__main__":

    """epsilons = [0, 0.01, 0.1, 0.5, 1]

    data = []
    for epsilon in epsilons:
        data.append(testbed(2000, 10, 1000, epsilon_select, epsilon))
        print("Calculation for epsilon={} ready".format(epsilon))

    show_data(data, epsilons)
    """

    temperatues = [0.5, 1, 5]

    for action in [incremental_average_action_value, constant_step_action_value]:
        plt.figure(len(plt.get_fignums())+1)
        data = []
        for temperatue in temperatues:
            data.append(testbed(2000, 10, 2000, softmax_select, temperatue, action, 0.1))
            print("Calculation for temperature={} ready".format(temperatue))
            add_plot_data(data, temperatues)
    plt.show()
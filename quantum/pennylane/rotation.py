import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import MaxNLocator

import pennylane as qml
from pennylane import numpy as np

dev1 = qml.device('default.qubit', wires=1)

@qml.qnode(dev1)
def circuit(params):
	qml.RX(params[0], wires=0)
	qml.RY(params[1], wires=0)
	return qml.expval.PauliZ(0)

def cost(var):
	return circuit(var)

def optimize_graddesc(init_params):
	opt = qml.GradientDescentOptimizer(stepsize=0.4)

	steps = 100
	params = init_params
	var = []
	var.append(params)

	for i in range(steps):
	    # update the circuit parameters
	    params = opt.step(cost, params)
	    var.append(params)

	    if (i+1) % 5 == 0:
	        print('Cost after step {:5d}: {: .7f}'.format(i+1, cost(params)))

	print('Optimized rotation angles: {}, {}'.format(params, cost(params)))
	return var


def optimize_ada(init_params):
	ada = qml.AdagradOptimizer(0.4)

	var = init_params
	var_ada = [var]

	for it in range(100):
	    var = ada.step(cost, var)
	    
	    if (it + 1) % 5 == 0:
	        var_ada.append(var)
	        print('Objective after step {:5d}: {: .7f} | Angles: {}'.format(it + 1, cost(var), var) )

	print('Optimized rotation angles: {}, {}'.format(var, cost(var)))
	return var_ada

def draw(var_gd, var_ada):
	fig = plt.figure(figsize = (6, 4))
	ax = fig.gca(projection='3d')

	X = np.linspace(-3, 3, 30)
	Y = np.linspace(-3, 3, 30)
	xx, yy = np.meshgrid(X, Y)
	Z = np.array([[cost([x, y]) for x in X] for y in Y]).reshape(len(Y), len(X))
	surf = ax.plot_surface(xx, yy, Z, cmap=cm.coolwarm, antialiased=False)

	path_z = [cost(var)+1e-8 for var in var_gd]
	path_x = [v[0] for v in var_gd]
	path_y = [v[1] for v in var_gd]
	ax.plot(path_x, path_y, path_z, c='green', marker='.', label="graddesc", zorder=10)

	path_z = [cost(var)+1e-8 for var in var_ada]
	path_x = [v[0] for v in var_ada]
	path_y = [v[1] for v in var_ada]
	ax.plot(path_x, path_y, path_z, c='purple', marker='.', label="adagrad", zorder=11)

	ax.set_xlabel("v1")
	ax.set_ylabel("v2")
	ax.zaxis.set_major_locator(MaxNLocator(nbins = 5, prune = 'lower'))

	plt.legend()
	plt.show()

init_params = [3, 3.01]
draw(optimize_graddesc(init_params), optimize_ada(init_params))
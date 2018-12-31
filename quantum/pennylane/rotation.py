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

args = np.array([3.14/2, 0])
def optimize(init_params):
	opt = qml.GradientDescentOptimizer(stepsize=0.4)

	steps = 100
	params = init_params

	for i in range(steps):
	    # update the circuit parameters
	    params = opt.step(cost, params)

	    if (i+1) % 5 == 0:
	        print('Cost after step {:5d}: {: .7f}'.format(i+1, cost(params)))

	print('Optimized rotation angles: {}, {}'.format(params, cost(params)))

print("Start: {}, {}".format(args, cost(args)))
optimize(args)
import pennylane as qml
from pennylane import numpy as np

dev_qubit = qml.device('default.qubit', wires=1)
dev_fock = qml.device('strawberryfields.fock', wires=2, cutoff_dim=10)


@qml.qnode(dev_qubit)
def qubit_rotation(phi1, phi2):
    """Qubit rotation QNode"""
    qml.RX(phi1, wires=0)
    qml.RY(phi2, wires=0)
    return qml.expval.PauliZ(0)

@qml.qnode(dev_fock)
def photon_redirection(params):
    qml.FockState(1, wires=0)
    qml.Beamsplitter(params[0], params[1], wires=[0, 1])
    return qml.expval.MeanPhoton(1)

def squared_difference(x, y):
    """Classical node to compute the squared
    difference between two inputs"""
    return np.abs(x-y)**2

def cost(params, phi1=0.5, phi2=0.1):
    """Returns the squared difference between
    the photon-redirection and qubit-rotation QNodes, for
    fixed values of the qubit rotation angles phi1 and phi2"""
    qubit_result = qubit_rotation(phi1, phi2)
    photon_result = photon_redirection(params)
    return squared_difference(qubit_result, photon_result)

def optimize():
	# initialise the optimizer
	opt = qml.GradientDescentOptimizer(stepsize=0.4)

	# set the number of steps
	steps = 100
	# set the initial parameter values
	params = np.array([0.01, 0.01])

	for i in range(steps):
	    # update the circuit parameters
	    params = opt.step(cost, params)

	    if (i+1) % 5 == 0:
	        print('Cost after step {:5d}: {: .7f}'.format(i+1, cost(params)))

	print('Optimized rotation angles: {}'.format(params))

optimize()
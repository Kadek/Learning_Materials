import pennylane as qml
from pennylane import numpy as np
from pennylane.optimize import NesterovMomentumOptimizer
import matplotlib.pyplot as plt

dev = qml.device('default.qubit', wires=2)

def get_angles(x):

    beta0 = 2 * np.arcsin(np.sqrt(x[1]) ** 2 / np.sqrt(x[0] ** 2 + x[1] ** 2 + 1e-12) )
    beta1 = 2 * np.arcsin(np.sqrt(x[3]) ** 2 / np.sqrt(x[2] ** 2 + x[3] ** 2 + 1e-12) )
    beta2 = 2 * np.arcsin(np.sqrt(x[2] ** 2 + x[3] ** 2) / np.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2 + x[3] ** 2))

    return np.array([beta2, -beta1 / 2, beta1 / 2, -beta0 / 2, beta0 / 2])

def statepreparation(a):

    qml.RY(a[0], wires=0)

    qml.CNOT(wires=[0, 1])
    qml.RY(a[1], wires=1)
    qml.CNOT(wires=[0, 1])
    qml.RY(a[2], wires=1)

    qml.PauliX(wires=0)
    qml.CNOT(wires=[0, 1])
    qml.RY(a[3], wires=1)
    qml.CNOT(wires=[0, 1])
    qml.RY(a[4], wires=1)
    qml.PauliX(wires=0)

def layer(W):

    qml.Rot(W[0, 0], W[0, 1], W[0, 2], wires=0)
    qml.Rot(W[1, 0], W[1, 1], W[1, 2], wires=1)

    qml.CNOT(wires=[0, 1])

@qml.qnode(dev)
def circuit(weights, angles=None):

    statepreparation(angles)
    
    for W in weights:
        layer(W)

    return qml.expval.PauliZ(0)

def variational_classifier(var, angles=None):

    weights = var[0]
    bias = var[1]

    return circuit(weights, angles=angles) + bias

def square_loss(labels, predictions):

    loss = 0
    for l, p in zip(labels, predictions):
        loss = loss + (l - p) ** 2
    loss = loss / len(labels)

    return loss

def accuracy(labels, predictions):

    loss = 0
    for l, p in zip(labels, predictions):
        if abs(l - p) < 1e-5:
            loss = loss + 1
    loss = loss / len(labels)

    return loss

def cost(weights, features, labels):

    predictions = [variational_classifier(weights, angles=f) for f in features]

    return square_loss(labels, predictions)

def load():
	data = np.loadtxt("data/iris_classes1and2_scaled.txt")
	X = data[:, 0:2]
	print("First X sample (original)  :", X[0])

	# pad the vectors to size 2^2 with constant values
	padding = 0.3 * np.ones((len(X), 1))
	X_pad = np.c_[np.c_[X, padding], np.zeros((len(X), 1)) ] 
	print("First X sample (padded)    :", X_pad[0])

	# normalize each input
	normalization = np.sqrt(np.sum(X_pad ** 2, -1))
	X_norm = (X_pad.T / normalization).T  
	print("First X sample (normalized):", X_norm[0])

	# angles for state preparation are new features
	features = np.array([get_angles(x) for x in X_norm])  
	print("First features sample      :", features[0])

	Y = data[:, -1]

	return (X, X_norm, features, Y)

def visualise(X, X_norm, features, Y):
	plt.figure()
	plt.scatter(X[:,0][Y== 1], X[:,1][Y== 1], c='r', marker='o', edgecolors='k')
	plt.scatter(X[:,0][Y==-1], X[:,1][Y==-1], c='b', marker='o', edgecolors='k')
	plt.title("Original data")
	plt.show()

	plt.figure()
	dim1 = 0
	dim2 = 1
	plt.scatter(X_norm[:,dim1][Y== 1], X_norm[:,dim2][Y== 1], c='r', marker='o', edgecolors='k')
	plt.scatter(X_norm[:,dim1][Y==-1], X_norm[:,dim2][Y==-1], c='b', marker='o', edgecolors='k')
	plt.title("Padded and normalised data (dims {} and {})".format(dim1, dim2))
	plt.show()

	plt.figure()
	dim1 = 0
	dim2 = 3
	plt.scatter(features[:,dim1][Y== 1], features[:,dim2][Y== 1], c='r', marker='o', edgecolors='k')
	plt.scatter(features[:,dim1][Y==-1], features[:,dim2][Y==-1], c='b', marker='o', edgecolors='k')
	plt.title("Feature vectors (dims {} and {})".format(dim1, dim2))
	plt.show()

def split_data(features, Y):
	np.random.seed(0)
	num_data = len(Y)
	num_train = int(0.75 * num_data)
	index = np.random.permutation(range(num_data))
	feats_train = features[index[:num_train]]
	Y_train = Y[index[:num_train]]
	feats_val = features[index[num_train:]]
	Y_val = Y[index[num_train:]]

	# We need these later for plotting
	X_train = X[index[: num_train]]
	X_val   = X[index[num_train :]]

	return (num_train, feats_train, feats_val, Y_train, Y_val, X_train, X_val)

def optimize(feats_train, feats_val, Y_train, Y_val, features, Y):
	num_qubits = 2
	num_layers = 6
	var_init = (0.01 * np.random.randn(num_layers, num_qubits, 3), 0.0)

	opt = NesterovMomentumOptimizer(0.01)
	batch_size = 5

	# train the variational classifier
	var = var_init
	for it in range(60):

	    # Update the weights by one optimizer step
	    batch_index = np.random.randint(0, num_train, (batch_size, ))
	    feats_train_batch = feats_train[batch_index]
	    Y_train_batch = Y_train[batch_index]
	    var = opt.step(lambda v: cost(v, feats_train_batch, Y_train_batch), var)

	    # Compute predictions on train and validation set
	    predictions_train = [np.sign(variational_classifier(var, angles=f)) for f in feats_train]
	    predictions_val = [np.sign(variational_classifier(var, angles=f)) for f in feats_val]

	    # Compute accuracy on train and validation set
	    acc_train = accuracy(Y_train, predictions_train)
	    acc_val = accuracy(Y_val, predictions_val)

	    print("Iter: {:5d} | Cost: {:0.7f} | Acc train: {:0.7f} | Acc validation: {:0.7f} "
	          "".format(it+1, cost(var, features, Y), acc_train, acc_val))
	return var

def visualize_trained(var, X_train, X_val, Y_train, Y_val):
	plt.figure()
	cm = plt.cm.RdBu

	# make data for decision regions
	xx, yy = np.meshgrid(np.linspace(0.0, 1.5, 20), np.linspace(0.0, 1.5, 20))
	X_grid = [np.array([x, y]) for x, y in zip(xx.flatten(), yy.flatten())] 

	# preprocess grid points like data inputs above
	padding = 0.3 * np.ones((len(X_grid), 1))
	X_grid = np.c_[np.c_[X_grid, padding], np.zeros((len(X_grid), 1)) ]  # pad each input
	normalization = np.sqrt(np.sum(X_grid ** 2, -1))
	X_grid = (X_grid.T / normalization).T  # normalize each input
	features_grid = np.array([get_angles(x) for x in X_grid])  # angles for state preparation are new features
	predictions_grid = [variational_classifier(var, angles=f) for f in features_grid]
	Z = np.reshape(predictions_grid, xx.shape)

	# plot decision regions
	cnt = plt.contourf(xx, yy, Z, levels=np.arange(-1, 1.1, 0.1), cmap=cm, alpha=.8, extend='both')
	plt.contour(xx, yy, Z, levels=[0.0], colors=('black',), linestyles=('--',), linewidths=(0.8,))
	plt.colorbar(cnt, ticks=[-1, 0, 1])

	# plot data
	plt.scatter(X_train[:,0][Y_train==1], X_train[:,1][Y_train==1], c='b', marker='o', edgecolors='k', label="class 1 train")
	plt.scatter(X_val[:,0][Y_val==1], X_val[:,1][Y_val==1], c='b', marker='^', edgecolors='k', label="class 1 validation")
	plt.scatter(X_train[:,0][Y_train==-1], X_train[:,1][Y_train==-1], c='r', marker='o', edgecolors='k', label="class -1 train")
	plt.scatter(X_val[:,0][Y_val==-1], X_val[:,1][Y_val==-1], c='r', marker='^', edgecolors='k', label="class -1 validation")

	plt.legend()
	plt.show()



(X, X_norm, features, Y) = load()
(num_train, feats_train, feats_val, Y_train, Y_val, X_train, X_val) = split_data(features, Y)
var = optimize(feats_train, feats_val, Y_train, Y_val, features, Y)
visualize_trained(var, X_train, X_val, Y_train, Y_val)
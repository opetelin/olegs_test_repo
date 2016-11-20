
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap



class Perceptron:
	"""
	Implements a perceptron that classifies data into either -1 or 1
	
		z = w_0 + w_1*x_1 + ... w_i*x_i

	Where w's are weights and x's are inputs corresponding to each "dendrite"
	If z >= 0, we output +1, and -1 otherwise
	Note that w_0 is a special weight that serves as a "threshold function"
		(i.e. if w_1*x_1 + .... >= -w_0, we output +1, and -1 otherwise)
	It is interesting that the zero-weight w_0 can be scaled... I'm not exactly sure why this is needed... can test?

	Learning is done via rosenblatt's simple perceptron rule:
		change in weight w_j = learning_rate * (y_ideal - y_predicted) * x_j

	While this perceptron is most-natively used for a binary classification, we can use
	n perceptrons to deal with n separate classes (i.e. classifying 10 different types of flowers).
	In such a case, each perceptron can be trained to classify one single class -- to output +1 for the desired
	class, and -1 for all the others. Then if we want to classify a new sample, one perceptron should ideally
	output +1 and all the others -1. (In the event that multiple perceptrons give +1, we can probably choose
	the one that exceeds the threshold by the greatest amount). Conceptually, it seems like this method
	can be used for a wide range of classification tasks (perhaps even recognizing single hand-written digits?)
		- But it is important to remember that the samples must be "linearly separable" ie there's some line/plane/hyperplane
		  that separates each class from all the rest. So perhaps the usefullness is questionable?
	"""
	def __init__(self, learning_rate, 		#defines how agressively we update weights based on disagreement between ideal and predicted data
	                   num_epochs):			#defined the number of passes we make over the training data
		self.learning_rate = learning_rate
		self.num_epochs = num_epochs

	def fit(self, X,	#training inputs. 2-d array [num_samples, num_features]
	              y):	#training outputs. 1-d vector [num_samples] with correct output data for each input sample in X
		#Note: the Adaline neuron, which uses gradient descent to optimize a simple convex cost function (based on squared difference between neuron activation
		# and the ideal output), would simply re-implement this self.fit method. All else would remain the same. 

		self.w_ = np.zeros(1 + X.shape[1])	#weights. one for each feature in X, plus one more for the zero-weight
		self.errors_ = []

		#do training
		for dummy in range(self.num_epochs):
			errors = 0
			for ix, target in zip(X, y):	#ix will be row of X, target will be entry in y
				update_w = self.learning_rate * (target - self.predict(ix))
				self.w_[1:] += update_w * ix	#update all weights (except w_0) by the same value
				self.w_[0] += update_w		#updating the threshold, basically
				errors += int(update_w != 0)
			self.errors_.append(errors)
		return self

	def net_input(self, sample):
		#print(sample)
		#print(self.w_[1:])
		result = np.dot(sample, self.w_[1:]) + self.w_[0]
		return result
				
	def predict(self, sample):
		result = -1
		#print(sample)
		#print(self.net_input(sample))
		if self.net_input(sample) >= 0:
			result = 1
		return result
	
def get_flower_data():
	df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
	y = df.iloc[0:100, 4].values			#rows 0-99, column 4 (flower name)
	y = np.where(y == 'Iris-setosa', -1, 1)		#is or is not setosa flower
	X = df.iloc[0:100, [0,2]].values		#get sepal length and petal length of each flower

	return [X, y]

def visualize_flower_data():
	[X, y] = get_flower_data()

	plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
	plt.scatter(X[50:100, 0], X[50:100,1], color='blue', marker='x', label='versicolor')
	plt.xlabel('petal length [cm]')
	plt.ylabel('sepal length [cm]')
	plt.legend(loc='best')
	plt.show()

def train_perceptron():
	[X, y] = get_flower_data()

	ppn = Perceptron(0.1, 10)
	ppn.fit(X,y)

	return [ppn, X, y]

def plot_perceptron_epochs(ppn):
	plt.plot(range(1, len(ppn.errors_)+1), ppn.errors_, marker='o')
	plt.xlabel('Num epochs')
	plt.ylabel('Num misclassifications')
	plt.show()

def plot_decision_regions(X, y, classifier, resolution=0.02):

    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

def main():
	#visualize_flower_data()
	[ppn, X, y] = train_perceptron()
	plot_perceptron_epochs(ppn)
	#print(X)
	#print(y)
	#print(ppn.w_)
	#plot_decision_regions(X, y, ppn)	#not working...

	ind = 33
	print('actual %d   predicted %d' % (y[ind], ppn.predict(X[ind])))		#but simple predictions work fine.
	#^ though doing it this way, we're basically validating on the training data, which is a no-no




if __name__ == '__main__':
	main()


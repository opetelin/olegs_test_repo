
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron

from sklearn.linear_model import LogisticRegression


#Basically the same as classifier1.py, except we use the built-in scikit-learn class.
#NOTE: this implements multiclass classification using binary classifiers at its core.
# With N classes, we have N binary classifiers. Each classifier treats it's own class as positive
# and all the other classes as negative. However, actual classification is performed based on the 
# POSITIVE DISTANCE from each classifier boundary. The farther we are into a classifier's region, 
# the more CONFIDENCE we have that the sample belongs to this class. Then we just pick the class
# with the highest associated confidence. Neato burrito.

#added logistic regression test as well. Logistic regression is still a linear algorithm for binary classification.
# it assumes that the probability that the estimated probability of sample x belonging to its (correct) class y is related to the net-input z as
#       logit[ p(y | x) ] = z = w0 + w1x1 + w2x2 + ...			y \in {0,1}
#
# so that
#       p(y|x) = logistic(z)  <-- the sigmoid function
#
# the cost function that learns our weights is then related to the probability that each sample was classified correctly
#	(i.e. the product of the probabilities that each sample belongs to its correct class \in {0,1})



def get_data():
	iris = datasets.load_iris()

	X = iris.data[:, [2,3]]
	y = iris.target

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

	scaler = StandardScaler()
	scaler.fit(X_train)		#gets average/std_dev of the train set

	#get scaled inputs
	X_train_std = scaler.transform(X_train)
	X_test_std = scaler.transform(X_test)

	return [X_train_std, y_train, X_test_std, y_test]


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.01):

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

	#highlight test samples
	if test_idx:
		X_test, y_test = X[test_idx, :], y[test_idx]
		plt.scatter(X_test[:,0], X_test[:,1], c='', alpha=1.0, linewidth=1, marker='o', s=55, label='test set')


def main():
	[X_train_std, y_train, X_test_std, y_test] = get_data()
	
	#Adaline perceptron
	ppn = Perceptron(n_iter=40, eta0=0.1, random_state=0)
	ppn.fit(X_train_std, y_train)
	y_pred = ppn.predict(X_test_std)
	print('Adaline misscasified: %d' % (y_test != y_pred).sum())

	#logistic regression
	lr = LogisticRegression(C=1000, random_state=0)		#a higher C decreases the importance of the regularization term in the cost function being minimized (as 1/C)
	lr.fit(X_train_std, y_train)
	y_pred = lr.predict(X_test_std)
	print('Logistic regression misscasified: %d' % (y_test != y_pred).sum())

	#classifier = ppn
	classifier = lr

	X_combined_std = np.vstack((X_train_std, X_test_std))
	y_combined = np.hstack((y_train, y_test))
	plot_decision_regions(X_combined_std, y_combined, classifier, test_idx=range(105,150))
	plt.xlabel('petal length [standardized]')
	plt.ylabel('sepal length [standardized]')
	plt.legend(loc='best')
	plt.show()


if __name__ == '__main__':
	main()


import numpy as np
import scipy.io as sio
import math
import sys



class Layer:
	"""A layer of neurons. This can be used to represent 1D layers as well as 2D, though underlying representation will be 1D."""
	def __init__(self,
	             name,
	             num_columns,			#number of columns in this layer
		     num_rows = 1,			#1 for normal layer; can have 2-d layer if layer is convolution/pool/input
		     layer_type = 'normal',		#implemented: normal, convolution, average_pool, input
	             neuron_type = 'logistic',		#implemented: logistic, softmax, linear
		     momentum = 0.9,			#for backprop
		     learning_rate = 0.00003,		#for backprop
		     init_weight = 0.01,		#what to initialize weights to
		     bias = None,
		     twoD_stride = None,		#2D stride. if layer is convolution/pool (relative to layer below)
		     twoD_feature_side_length = None,	#if layer is convolution/pool (how many units to a side does each neuron in this layer take?)
		     twoD_num_maps = 1			#if layer is convolution/pool (number of feature maps in parallel, with dimensions specified above)
		     ):	

		self.name = name
		self.layer_type = layer_type
		self.num_columns = num_columns
		self.num_rows = num_rows
		self.twoD_stride = twoD_stride
		self.twoD_feature_side_length = twoD_feature_side_length
		self.twoD_num_maps = twoD_num_maps

		self.set_dimensions(num_columns, num_rows, layer_type, twoD_num_maps)

		self.neuron_type = neuron_type
		self.momentum = momentum
		self.learning_rate = learning_rate
		self.init_weight = init_weight
		self.bias = bias

		#weights W
		self.W = None
		
		#deltaW from previous iteration of backpropagation
		self.last_deltaW = None

		#M. captures connectivity between this layer and the next (prevents non-existent weights from being updated)
		self.weight_mask = None	

		#y = f(z); z is the net input to each neuron
		self.y = None

		self.z_below = None

		#link to above/below layers
		self.layer_above = None
		self.layer_below = None

		self.tied_weights = None


	def set_dimensions(self, num_columns, num_rows, layer_type, twoD_num_maps):
		if self.layer_type == 'normal':
			assert(self.twoD_stride is None)
			assert(self.twoD_feature_side_length is None)
			assert(num_rows == 1)

		self.num_neurons = num_columns * num_rows * twoD_num_maps


	#########################################
	######## INTER-LAYER CONNECTIONS ########
	#########################################

	def connect_to_layer(self, layer_above,		#class object representing layer above
	                    from_subset=None,		#range of neurons in this layer (as [start, end) in the 1D-representation; NOT inclusive) 
			    to_subset=None):		#range of neurons in target layer (as [start, end) in the 1D-representation; NOT inclusive)
		"""Implements connections from this layer to the layer above.
		Connectivity is defined using the weight mask matrix (connections with entries = 1; 0 otherwise)
		
		This function can implement connections from/to the following layers:
		  * normal --> normal. In this case, can use 'from_subset' and 'to_subset' arguments to define full connectivity between
		    the specified ranges of neurons on this and above layer. If source/target neuron ranges aren't specified, then we'll have
		    full connectivity between all neurons in these two layers.
		  * convolution --> average_pool. This will be specified using the dimensions of the two layers, as well as the "feature" dimensions
		    and twoD stride of the target layer.
		  * average_pool --> convolution. Same as above
		  * convolution --> normal. This will specify full connectivity between all neurons on this layer and the range of neurons
		    specified on the next layer (i.e. 'to_subset' can be used).
		  * average_pool --> normal. Same as above.
		"""

		self.layer_above = layer_above
		layer_above.layer_below = self

		#get from/to types, dimensions, other data
		from_layer_type = self.layer_type
		to_layer_type = layer_above.layer_type

		from_size = self.num_neurons		#i
		to_size = layer_above.num_neurons	#j

		#some error checking
		if from_layer_type != 'normal' and from_layer_type != 'input':
			assert(from_subset is None)
		if to_layer_type != 'normal':
			assert(to_subset is None)
		if from_subset is not None:
			assert(from_subset[0] >= 0)
			assert(from_subset[1] <= from_size)
		if to_subset is not None:
			assert(to_subset[0] >= 0)
			assert(to_subset[1] <= to_size)
	
		#define outgoing weight matrix dimensions (i x j)
		if self.weight_mask is None:
			self.weight_mask = np.zeros((from_size, to_size))

			#add weights for the bias
			if self.layer_above is not None and self.layer_above.bias is not None:
				bias_weights = self.layer_above.bias * np.ones((1,to_size))
				self.weight_mask = np.concatenate( (self.weight_mask, bias_weights), axis=0 )


		#set outgoing weight mask
		if to_layer_type == 'normal':
			if from_subset is None:
				from_subset = [0, from_size]
			if to_subset is None:
				to_subset = [0, to_size]

			#need to "turn on" the matrix entries where from_subset and to_subset ranges intersect
			for i in range(from_subset[0], from_subset[1]):
				for j in range(to_subset[0], to_subset[1]):
					#print('%d %d' % (i,j))
					self.weight_mask[i,j] = 1.0

		elif from_layer_type != 'normal' and to_layer_type != 'normal':
			#TODO: account for multiple 2d maps in parallel
			#TODO: shared weights. Can implement another matrix that holds an index for each weight
			#mapping between 2D layers
			if from_layer_type == 'input':
				assert(self.num_rows > 1)
			assert(to_layer_type != 'input')

			from_sizei = self.num_rows
			from_sizej = self.num_columns

			to_sizei = self.layer_above.num_rows
			to_sizej = self.layer_above.num_columns
			to_f_size = self.layer_above.twoD_feature_side_length
			to_stride = self.layer_above.twoD_stride

			#iterate column-wise
			for j in range(0, to_sizej, to_stride):
				for i in range(0, to_sizei, to_stride):
					#i and j represent the offset of our feature
					#map the feature at (i,j) of the layer above
					for dj in range(0, to_f_size):
						for di in range(0, to_f_size):
							#2D layers are laid out in 1D using a column-wise order
							to_index = i + j*to_sizei
							from_index = (i+di) + (j+dj)*from_sizei
							self.weight_mas[from_index, to_index] = 1.0

			#now need to replicate weight mask across all feature maps
			#ad;lkjasdl;js;aldkjsa;ldkjfsa;lkdfjsa;dlfkj
		else:
			print('Cant connect layer type %s to layer type %s' % (from_layer_type, to_layer_type))
			sys.exit()

		#self.W = self.init_weight * self.weight_mask
		self.W = self.init_weight * np.random.rand(self.weight_mask.shape[0], self.weight_mask.shape[1]) * self.weight_mask


	def tie_weights_in_range(self, ranges_to_connect):
		"""ranges_to_connect -- [ranges_0, ranges_1, ranges_2,...]
		   ranges_k -- [[from_i, to_i], [from_j, to_j]] (NOT inclusive!! i.e. [from_i, to_i))

		   each ranges_k defines a sub-matrix in the weight matrix W, and each should be of the same dimension.
		   Element (i,j) in sub-matrix k will be tied to elements (i,j) in all other sub-matrices forall k.

		   This information is used during backpropagation.
		"""

		self.tied_weights = ranges_to_connect

	
	###############################
	######## COST FUNCTION ########
	###############################

	def get_cost(self, target_outputs):
		"""Returns cross-entropy cost for softmax layer"""
		assert(self.neuron_type == 'softmax')
		assert(self.y.shape == target_outputs.shape)

		result = None

		if self.z_below is not None:
			self.y = self.get_y(z_below=self.z_below)

			#print(target_outputs.T.shape)
			#print(self.y.shape)
			#print(np.log(self.y))
			small_num = math.e ** -20.0
			cost_at_each_sample = -1.0 * (target_outputs.T).dot( np.log(self.y + small_num) )
			cost_at_each_sample = cost_at_each_sample.diagonal()	#only want ith output paired with ith target, which is the diagonal of this matrix. not very efficient...
			#print(cost_at_each_sample)

			num_samples = cost_at_each_sample.shape[0]

			#return average cross-entropy across all samples
			result = np.sum(cost_at_each_sample) / float(num_samples)
		return result


	def get_cost_derivative(self, target_outputs):
		"""Returns derivative of cross-entropy cost for softmax layer w.r.t. neuron net inputs (i.e. dE/dz)"""
		assert(self.neuron_type == 'softmax')
		assert(self.y.shape == target_outputs.shape)

		Dez = self.y - target_outputs
		return Dez


	#####################################
	######## FORWARD PROPAGATION ########
	#####################################
	
	def get_z_to_next_layer(self, z_below=None, input_data=None):
		"""returns column vector corresponding to net input to next layer above"""
		result = None
		if self.layer_type == 'input':
			assert(input_data is not None)
			#add bias
			if self.layer_above.bias is not None:
				num_samples = input_data.shape[1]
				bias = np.ones( (1,num_samples) )
				input_data = np.concatenate( (input_data, bias), axis=0 )
			self.y = input_data
			result = (self.W.T).dot( input_data )
		else:
			assert(z_below is not None)
			self.y = self.get_y(z_below)
			result = (self.W.T).dot( self.y )
		return result


	def get_y(self, z_below):	#net input from layer below (column vector)
		"""returns y = f(z) based on the neuron type of this layer"""

		result = None
		if self.neuron_type == 'logistic':
			result = 1 / (1 + ( math.e ** (-z_below) ))

			#add-in the bias that will go to the next layer
			if self.layer_above.bias is not None:
				num_samples = result.shape[1]
				bias = np.ones( (1,num_samples) )
				result = np.concatenate( (result, bias), axis=0 )

		elif self.neuron_type == 'linear':
			result = z_below
			#add-in the bias that will go to the next layer
			if self.layer_above.bias is not None:
				num_samples = result.shape[1]
				bias = np.ones( (1,num_samples) )
				result = np.concatenate( (result, bias), axis=0 )


		elif self.neuron_type == 'softmax':
			#need to make sure we don't overflow	#XXX check that this is correct!
			max_z = np.max(z_below)
			z_below -= max_z
			result = math.e ** (z_below)

			#normalize. remember that z can be a matrix, with each column representing a different sample
			for col in range(0, np.shape(result)[1] ):
				result[:,col] = result[:,col] / np.sum( result[:,col] )

		else:
			print('Unexpected neuron type %s' % (self.neuron_type))
			sys.exit()

		return result

	def forwardprop_update(self, z_below=None, input_data=None):
		self.z_below = z_below
		if self.layer_above:
			z_to_above = self.get_z_to_next_layer(z_below, input_data)
			#print('Propagating from %s to %s' % (self.name, self.layer_above.name))
			self.layer_above.forwardprop_update( z_below=z_to_above )
		else:
			self.y = self.get_y(z_below)


	#################################
	######## BACKPROPAGATION ########
	#################################

	def get_Dez(self, Dez_above=None, targets=None):
		"""dE/dz of this layer based on neuron type. If 'targets' are specified, then we
		   assume that this is an output layer. If 'Dez_above' is specified, then we assume
		   this is an intermediate layer"""

		result = None
		if targets is not None:
			assert(self.neuron_type == 'softmax')
			assert(self.y.shape == targets.shape)
			result = self.y - targets

		elif Dez_above is not None:
			if self.neuron_type == 'logistic':
				if self.layer_above.bias is not None:
					result = self.W[0:-1,:].dot( Dez_above ) * self.y[0:-1,:] * (1- self.y[0:-1,:])
				else:
					result = self.W.dot( Dez_above ) * self.y * (1- self.y)

			if self.neuron_type == 'linear':
				if self.layer_above.bias is not None:
					result = self.W[0:-1,:].dot( Dez_above )
				else:
					result = self.W.dot( Dez_above )

		else:
			print('Not enough arguments provided.')
			sys.exit()

		return result
	
	def backprop_update(self, Dez_above=None, targets=None):
		"""update this layer's weights, and do backpropagation for layer below"""
		if self.neuron_type == 'softmax':
			assert(targets is not None)
		else:
			assert(Dez_above is not None)

		#dE/dw of outgoing weights (i x j matrix)
		if self.layer_above is not None:
			#Dew is the average across all samples
			num_samples = self.y.shape[1]
			self.Dew = self.y.dot( Dez_above.T ) / float(num_samples)

		#update this layer's weights (pool layer weights are not updated)
		if 'pool' not in self.layer_type and self.neuron_type != 'softmax':
			new_deltaW = self.Dew
			if self.last_deltaW is not None:
				new_deltaW += self.momentum * self.last_deltaW		#TODO: that's how momentum works, right?

			#account for any tied weights
			if self.tied_weights:
				new_deltaW = self.adjust_deltaW_for_tied_weights(new_deltaW)

			#perform update
			self.W = (self.W - self.learning_rate * new_deltaW) * self.weight_mask	#weight mask makes sure we don't update weights that shouldn't exist
			self.last_deltaW = new_deltaW

		#do backprop to next layer below
		if self.layer_below:
			self.Dez = self.get_Dez(Dez_above=Dez_above, targets=targets)
			self.layer_below.backprop_update(Dez_above=self.Dez)

	def adjust_deltaW_for_tied_weights(self, deltaW):
		"""Looks at self.tied_weights to make sure that updates to tied weights are the same"""
		assert(self.tied_weights is not None)

		num_submatrices = len(self.tied_weights)

		#add all other submatrices to 0th submatrix
		for iadd in range(0, num_submatrices):
			if iadd != 0:
				from_range_i = self.tied_weights[iadd][0]
				from_range_j = self.tied_weights[iadd][1]

				to_range_i = self.tied_weights[0][0]
				to_range_j = self.tied_weights[0][1]

				deltaW[to_range_i[0]:to_range_i[1], to_range_j[0]:to_range_j[1]] += deltaW[from_range_i[0]:from_range_i[1], from_range_j[0]:from_range_j[1]]

		#replicate 0th submatrix to other submatrices
		for ireplicate in range(0, num_submatrices):
			if ireplicate != 0:
				from_range_i = self.tied_weights[0][0]
				from_range_j = self.tied_weights[0][1]

				to_range_i = self.tied_weights[ireplicate][0]
				to_range_j = self.tied_weights[ireplicate][1]

				deltaW[to_range_i[0]:to_range_i[1], to_range_j[0]:to_range_j[1]] = deltaW[from_range_i[0]:from_range_i[1], from_range_j[0]:from_range_j[1]]


		#finish taking the average (excluding the bias weights row)
		if self.bias is not None:
			deltaW[:-1,:] /= num_submatrices
		else:
			deltaW /= num_submatrices

		return deltaW
			



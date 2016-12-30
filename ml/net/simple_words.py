import time
import sys
from base import *


def main():
	#get matlab data
	data = sio.loadmat('data.mat')
	_vocab = data['data'][0,0]['vocab']
	vocab = []
	for i in range(_vocab.shape[1]):
		vocab += [ _vocab[0,i][0] ]

	#samples are in rows
	train_data = data['data'][0,0]['trainData'].T
	validate_data = data['data'][0,0]['validData'].T
	test_data = data['data'][0,0]['testData'].T

	num_words = len(vocab)
	net = make_layers(num_words)
	

	#test word conversion
	#test_words = np.array([[1,2],[4,5],[7,8]])
	#print(test_words)
	#one_hot = get_one_hot(test_words, 10)
	#print(one_hot)
	#print(one_hot.shape)
	#back_to_test = get_word_indices_from_one_hot(one_hot, 10)
	#print(back_to_test)

	train(net, train_data, validate_data, test_data, batch_size=100, num_words=num_words, num_epochs=10)
	np.savetxt("hidden.csv", net[2].W, delimiter='\t')
	np.savetxt("hidden_y.csv", net[2].y, delimiter='\t')
	np.savetxt("embed.csv", net[1].W, delimiter='\t')
	np.savetxt("embed_y.csv", net[1].y, delimiter='\t')
	np.savetxt("out_y.csv", net[3].y, delimiter='\t')

	#print(net[0].W)
	#print(net[1].W)
	#print(net[2].W)


def train(net, train_data, validate_data, test_data, batch_size, num_words, num_epochs=1):

	train_size = train_data.shape[0]
	num_batches = float(train_size) / float(batch_size)
	num_batches = math.floor(num_batches)

	[valid_inputs, valid_targets] = get_one_hot_data(validate_data[0:10000,:].T, num_words)	#TODO

	for iepoch in range(0, num_epochs):
		for ibatch in range(0, num_batches):
			batch_train_data = np.array
			if ibatch != num_batches-1:
				batch_train_data = train_data[ibatch*batch_size : (ibatch+1)*batch_size, :]
			else:
				#last batch... may have incomplete batch
				batch_train_data = train_data[ibatch*batch_size :, :]

			#split train data into input and targets
			[train_inputs, train_targets] = get_one_hot_data(batch_train_data.T, num_words)

			#do forward propagation
			net[0].forwardprop_update(input_data = train_inputs)

			#do back propagation
			net[-1].backprop_update(targets = train_targets)

			#print stuff
			if ibatch % 100 == 0:
				cost = net[-1].get_cost(train_targets)
				if cost is not None:
					print('epoch %d   batch %d  cost %f' % (iepoch, ibatch, cost))
			if (ibatch - 1) % 1000 == 0 and ibatch > 0:
				net[0].forwardprop_update(input_data = valid_inputs)
				cost = net[-1].get_cost(valid_targets)
				if cost is not None:
					print('epoch %d   batch %d  validate cost %f' % (iepoch, ibatch, cost))

			#return


		
def get_one_hot_data(samples, vocab_size):
	inputs = samples[0:-1,:]
	targets = samples[-1,:]

	one_hot_inputs = get_one_hot(inputs, vocab_size)
	one_hot_targets = get_one_hot(targets, vocab_size)

	assert(np.array_equal(inputs, get_word_indices_from_one_hot(one_hot_inputs, vocab_size)))

	return [one_hot_inputs, one_hot_targets]


def get_one_hot(word_matrix, vocab_size):
	shape = word_matrix.shape
	if len(shape) > 1:
		numi, numj = shape
	else:
		word_matrix = word_matrix[np.newaxis]	#need to convert array into a matrix
		numi, numj = word_matrix.shape
	
	result = np.zeros( (numi*vocab_size, numj) )

	for j in range(0,numj):
		new_col = np.array
		for i in range(0,numi):
			word = word_matrix[i,j]
			result[i*vocab_size + word-1, j] = 1.0
	return result


def get_word_indices_from_one_hot(one_hot_matrix, vocab_size):
	shape = one_hot_matrix.shape
	num_samples = shape[1]
	reshaped = one_hot_matrix.reshape(vocab_size,-1, order='F')

	result = np.argmax(reshaped, axis=0)
	result = result.reshape(-1, num_samples, order='F')
	result += 1

	return result


def get_output_words(output_layer):
	output = output_layer.y
	num_samples = output.shape[1]
	word_inds = []
	for isamp in range(0,num_samples):
		word_inds += [np.argmax( output[:,isamp] ) + 1]
	return word_inds


def make_layers(num_words):
	input_size = num_words
	embedding_size = 50
	hidden_size = 200
	output_size = num_words
	learning_rate = 0.09

	#create layers
	input_layer = Layer(name='input', num_columns = input_size*3, layer_type = 'input', learning_rate=learning_rate, neuron_type='linear')
	embedding_layer = Layer(name='embedding', num_columns = embedding_size*3, learning_rate=learning_rate, neuron_type='linear')
	hidden_layer = Layer(name='hidden', num_columns = hidden_size, learning_rate=learning_rate, bias=1.0, neuron_type='logistic')
	output_layer = Layer(name='output', num_columns = output_size, neuron_type = 'softmax', learning_rate=learning_rate, bias=1.0)

	#connect inputs
	#input_layer.connect_to_layer(embedding_layer)
	input_layer.connect_to_layer(embedding_layer, from_subset=[0,input_size], to_subset=[0,embedding_size])
	input_layer.connect_to_layer(embedding_layer, from_subset=[input_size, 2*input_size], to_subset=[embedding_size, 2*embedding_size])
	input_layer.connect_to_layer(embedding_layer, from_subset=[2*input_size, 3*input_size], to_subset=[2*embedding_size, 3*embedding_size])

	#tie together weights on the input layer
	#input_layer.tie_weights_in_range([
	#                                 [[0,input_size], [0,embedding_size]],
	#                                 [[input_size, 2*input_size], [embedding_size, 2*embedding_size]],
	#                                 [[2*input_size, 3*input_size], [2*embedding_size, 3*embedding_size]]
	#				 ])


	#connect embedding layer
	embedding_layer.connect_to_layer(hidden_layer)

	#connect output layer
	hidden_layer.connect_to_layer(output_layer)
	
	print("Finished connecting layers")

	net = [input_layer, embedding_layer, hidden_layer, output_layer]
	return net



if __name__ == '__main__':
	main()

"""
Created on Thu Jan 21 10:14:30 2022

@author: Nelson
"""

""" A collection of useful functions for keras"""

from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

#creates a plot with the required metric from the object returned 
#by .fit() function. If an outfile if passed, the figure is saved,
#otherwise pyplot .show() is invoked
def plot_loss_history(h, metric = 'loss', outfile = None):
	pyplot.plot(h.history[metric], label = 'Train ' + metric)
	pyplot.plot(h.history['val_' + metric], label = 'Validation ' + metric)
	pyplot.xlabel('Epochs')
	pyplot.title(metric)
	pyplot.legend()

	if outfile is not None:
		pyplot.savefig(outfile)
	else:
		pyplot.show()

#instantiate a network, which will then need to be compiled
def instantiate_network(input_shape, conv_section = [32, 64], dense_section = [128], conv_kernel = (3, 3), maxpooling_kernel = (2,2), dropout_rate = 0.25):
	model = Sequential()
	
	#first node is different, because it requires input shape
	model.add(Conv2D(
		conv_section.pop(0), 
		kernel_size=kernel_size,
		activation='relu',
		input_shape=input_shape))
	model.add(MaxPooling2D(pool_size=maxpooling_kernel))
	model.add(Dropout(dropout_rate))

	
	#convolutionary section
	for nodes in conv_section:
		model.add(Conv2D(nodes, kernel_size, activation='relu'))
		model.add(MaxPooling2D(pool_size=maxpooling_kernel))
		model.add(Dropout(dropout_rate))
		
	#a flatten layer separates conv section from dense section
	model.add(Flatten())
	
	#dense section
	for nodes in dense_section:
		model.add(Dense(nodes, activation='relu'))
		model.add(Dropout(dropout_rate))
	
	#final output
	model.add(Dense(1, activation='linear'))
		
	return(model)

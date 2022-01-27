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
#by .fit() function. If an outfile if passed, the figure is saved
#before invoking pyplot .show() 
def plot_loss_history(h, metric = 'loss', outfile = None):
	pyplot.plot(h.history[metric], label = 'Train ' + metric)
	pyplot.plot(h.history['val_' + metric], label = 'Validation ' + metric)
	pyplot.xlabel('Epochs')
	pyplot.title(metric)
	pyplot.legend()

	if outfile is not None:
		pyplot.savefig(outfile)
	pyplot.show()
	
	
	
#instantiate a network, which will then need to be compiled
#default parameters:
# - input_shape : this is required
# - conv_layers = [32, 64]
# - dense_layers = [128]
# - conv_filter = (3, 3)
# - conv_padding = 'same'
# - pool_filter = (2,2)
# - pool_step = 2
# - drop_rate = 0.25
def instantiate_network(config_dict):
	
	#cleanup of the config dictionary, so that we use local variables
	input_shape  = config_dict['input_shape']
	conv_layers  = config_dict.get('conv_layers', [32, 64]).copy() #copied so that we can pop
	conv_filter  = config_dict.get('conv_filter', (3, 3))
	conv_padding = config_dict.get('conv_padding', 'same')
	dense_layers = config_dict.get('dense_layers', [128])
	pool_filter  = config_dict.get('pool_filter', (2,2))
	pool_step    = config_dict.get('pool_step', 2)
	drop_rate    = config_dict.get('drop_rate', 0.25)
	
	#building the model
	model = Sequential()
	
	#step counter for the maxpooling layers
	mp_cnt = 0
	
	#first node is different, because it requires input shape
	model.add(Conv2D(
		conv_layers.pop(0), 
		kernel_size=conv_filter,
		activation='relu',
		input_shape=input_shape, 
		padding=conv_padding
	))
	mp_cnt += 1
	model.add(Dropout(drop_rate))

	#convolutionary section
	for nodes in conv_layers:
		model.add(Conv2D(nodes, conv_filter, activation='relu', padding=conv_padding))
		mp_cnt += 1
		if mp_cnt >= pool_step:
			model.add(MaxPooling2D(pool_size=pool_filter))
			mp_cnt = 0
		model.add(Dropout(drop_rate))
		
	#a flatten layer separates conv section from dense section
	model.add(Flatten())
	
	#dense section
	for nodes in dense_layers:
		model.add(Dense(nodes, activation='relu'))
		model.add(Dropout(drop_rate))
	
	#final output
	model.add(Dense(1, activation='linear'))
		
	return(model)

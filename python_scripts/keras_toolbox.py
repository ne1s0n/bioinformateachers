"""
Created on Thu Jan 21 10:14:30 2022

@author: Nelson
"""

""" A collection of useful functions for keras"""

from matplotlib import pyplot
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Input
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Conv2D, MaxPooling2D
from keras.regularizers import l1, l2, l1_l2

#creates a plot with the required metric from the object returned 
#by .fit() function. If an outfile if passed, the figure is saved
#before invoking pyplot .show()
#If a title is not present we report the metric 
def plot_loss_history(h, metric = 'loss', outfile = None, title = None):
	pyplot.plot(h.history[metric], label = 'Train ' + metric)
	pyplot.plot(h.history['val_' + metric], label = 'Validation ' + metric)
	pyplot.xlabel('Epochs')
	if title is None:
		title = metric
	pyplot.title(title)
	pyplot.legend()
	if outfile is not None:
		pyplot.savefig(outfile, bbox_inches='tight')
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
# - regularizer_l1 = 0.01 (None to turn off)
# - regularizer_l2 = 0.01 (None to turn off)
def instantiate_network(config_dict):
	
	#cleanup of the config dictionary, so that we use local variables
	input_shape  = config_dict['input_shape']
	conv_layers  = config_dict.get('conv_layers', [32, 64])
	conv_filter  = config_dict.get('conv_filter', (3, 3))
	conv_padding = config_dict.get('conv_padding', 'same')
	dense_layers = config_dict.get('dense_layers', [128])
	pool_filter  = config_dict.get('pool_filter', (2,2))
	pool_step    = config_dict.get('pool_step', 2)
	drop_rate    = config_dict.get('drop_rate', 0.25)
	regularizer_l1 = config_dict.get('regularizer_l1', 0.01)
	regularizer_l2 = config_dict.get('regularizer_l2', 0.01)
	
	#getting layer regularizers
	L1L2 = get_regularizers(regularizer_l1, regularizer_l2)
	
	#step counter for the maxpooling layers
	mp_cnt = 0
	
	#building the model
	model = Sequential()
	model.add(Input(shape = input_shape))

	#convolutionary section
	for nodes in conv_layers:
		model.add(Conv2D(
			nodes, 
			conv_filter, 
			activation='relu', 
			padding=conv_padding, 
			kernel_regularizer=L1L2
		))
		mp_cnt += 1
		if mp_cnt >= pool_step:
			model.add(MaxPooling2D(pool_size=pool_filter))
			mp_cnt = 0
		model.add(Dropout(drop_rate))
		
	#a flatten layer separates conv section from dense section
	model.add(Flatten())
	
	#dense section
	for nodes in dense_layers:
		model.add(Dense(nodes, activation='relu', kernel_regularizer=L1L2))
		model.add(Dropout(drop_rate))
	
	#final output
	model.add(Dense(1, activation='linear', kernel_regularizer=L1L2))
		
	return(model)

#returns a node regularizer based on the passed L1/L2 parameters, supports
#one or zero Nones
def get_regularizers(regularizer_l1, regularizer_l2):
	if (regularizer_l1 is not None) and (regularizer_l2 is not None):
		#both L1 and L2 regularization are active
		return l1_l2(l1=regularizer_l1, l2=regularizer_l2)
		
	if regularizer_l1 is not None :
		#L1 only
		return l1(l1=regularizer_l1)
		
	if regularizer_l2 is not None :
		#L2 only
		return l2(l2=regularizer_l2)

import numpy as np
import random

#split the data in two pieces of the required proportion (x is split
#along the first axis)
def train_val_split(x, y, validation_split):
	#how many samples are going to be selected
	n = int(np.floor(len(y) * validation_split))
	
	#a list of indexes
	items = list(range(len(y)))
	
	#the selection slices
	sel_val   = random.sample(items, n)
	sel_train = list(set(items) - set(sel_val))
	
	#use it on x and y, directly and reverse
	train_x = x[sel_train]
	train_y = [y[i] for i in sel_train]
	val_x   = x[sel_val]
	val_y   = [y[i] for i in sel_val]
	
	#all Ys should be a numpy array
	train_y = np.array(train_y)
	val_y = np.array(val_y)
	
	#and we are done
	return(train_x, train_y, val_x, val_y)

#data augmentation on y, adding normal noise. The number of
#times the whole dataset is copied is regulated by "reps".
#The original dataset is included, untouched	
def augment_add_normal_noise(x, y, reps=1, mu=0, sigma=0.1):
	result_x = x
	result_y = y
	for i in range(reps):
		#adding the required noise
		y_now = y.copy()
		for j in range(len(y)):
			y_now[j] = y_now[j] + random.gauss(mu, sigma)
		
		#putting all together
		result_x = np.concatenate((result_x, x))
		result_y = np.concatenate((result_y, y_now))
	return(result_x, result_y)

#creates or updates a class object that mimicks what is returned by
#keras model.fit() method, so that it's feedable to parse_history()
#train_set_history   : returned by model.fit() on train data
#val_set_evaluation  : returned by model.evaluate() on validation data
#metrics             : list of names for the measured metrics, taken from model.metrics_names
#past_merged_history : the object to be updated (from a previous call of this very function)
def merge_history(train_set_history, val_set_evaluation, metrics, past_merged_history = None):
	
	#support class, in case we don't have a past history to enlarge
	class MockTrainingHistory:
		history = {}
		
	if past_merged_history is None:
		past_merged_history = MockTrainingHistory()
		
	#at this point all new data should be added to past_merged_history
	for i in range(len(metrics)):		
		#retrieving the label
		met = metrics[i]
		
		#adding the last value from training set
		values = past_merged_history.history.get(met, [])
		values.append(train_set_history.history[met][-1])
		past_merged_history.history[met] = values
		
		#adding the proper value from validation set
		values = past_merged_history.history.get('val_' + met, [])
		values.append(val_set_evaluation[i])
		past_merged_history.history['val_' + met] = values
	
	return(past_merged_history)

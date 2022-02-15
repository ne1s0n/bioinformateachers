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
	
	#use it on x and y, directly and reverrse
	train_x = x[sel_train]
	train_y = [y[i] for i in sel_train]
	val_x   = x[sel_val]
	val_y   = [y[i] for i in sel_val]
	
	#and we are done
	return(train_x, train_y, val_x, val_y)
	
def add_normal_noise(x, y, reps=1, mu=0, sigma=0.1):
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
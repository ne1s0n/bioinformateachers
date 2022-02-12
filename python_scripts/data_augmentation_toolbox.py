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

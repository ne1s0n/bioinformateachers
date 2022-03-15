"""
Created on Thu Jan 20 17:14:30 2022

@author: Nelson
"""

""" A collection of custom metrics for keras """

import math
import numpy as np
import keras.backend as KB

#pearson's correlation
def pearson(x, y):
  #formula https://www.statology.org/pearson-correlation-coefficient/

  #NUMERATOR: SUM[ (x - x_mean) * (y - y_mean)]
  #DENOMINATOR: SQRT(A) * SQRT(B)
  #with:
  #  A = SUM[ (x - x_mean) ^ 2]
  #  B = SUM[ (y - y_mean) ^ 2]

  num = KB.sum( (x - KB.mean(x)) * (y - KB.mean(y)) )
  den = KB.sqrt(KB.sum((x - KB.mean(x)) ** 2)) * KB.sqrt(KB.sum((y - KB.mean(y)) ** 2))

  return(num / den)

#Root Mean Square Error, to ease comparison with GROAN
def rmse(x, y):
  return KB.mean(KB.sqrt((x - y) ** 2))

## NDCG: normalised discounted cumulative gain
def ndcg(y, y_hat, k=0.20):
    
    print('the selected value for k is {}'.format(k))
    n = len(y) # number of predicted examples
    nk = round(k*n) ## select the k top examples
    print(nk)
    y_inds = y.argsort()
    y_sort_y = y[y_inds]
    y_hat_inds = y_hat.argsort()
    y_sort_y_hat = y[y_hat_inds]
    
    temp = 0
    for i in range(nk):
        ix = i+1
        d = 1/(KB.log(ix)+1) ## should be log2 !! (TODO: find if with keras.backend this is possible)
        num = KB.sum(y_sort_y_hat[0:ix])*d
        den = KB.sum(y_sort_y[0:ix])*d

        temp = (i*temp + num/den ) / (ix)
    
    return(temp)

"""
Created on Thu Jan 20 17:14:30 2022

@author: Nelson
"""

""" A collection of custom metrics for keras """

import tensorflow as tf
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
    nk = round(k*float(n))
    ## select the k top examples
    print(nk)
    y_inds = tf.argsort(y)
    y_sort_y = tf.gather(y, y_inds)
    y_hat_inds = tf.argsort(y_hat)
    y_sort_y_hat = tf.gather(y, y_hat_inds)
    
    seq = tf.range(1.0, nk+1)
    d = KB.log(seq+1)
    k2 = KB.log(2.0)
    d = k2/d ## 1/(d/k2) --> 1* k2/d
    
    num = KB.sum(y_sort_y_hat[0:nk]*d)
    den = KB.sum(y_sort_y[0:nk]*d)

    temp = num/den
    
    return(temp)

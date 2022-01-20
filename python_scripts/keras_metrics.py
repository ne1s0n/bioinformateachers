"""
Created on Thu Jan 20 17:14:30 2021

@author: Nelson
"""

""" A collection of custom metrics for keras """

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

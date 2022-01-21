"""
Created on Thu Jan 21 10:14:30 2022

@author: Nelson
"""

""" A collection of useful functions for keras"""

from matplotlib import pyplot as plt

#plot the required metric from the object returned by .fit() function
def plot_loss_history(h, metric = 'loss'):
    plt.plot(h.history[metric], label = 'Train ' + metric)
    plt.plot(h.history['val_' + metric], label = 'Validation ' + metric)
    plt.xlabel('Epochs')
    plt.title(metric)
    plt.legend()
    plt.show()

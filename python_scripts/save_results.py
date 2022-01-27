#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:50:14 2022

@author: filippo
"""

""" Function(s) to collect results from deep learning runs """

import os
import pandas as pd

#get results to be saved
def parse_history(h, phenotypes, trait, config_dict, max_val_pearson, nparams, replicate):
    
    ## get metrics from history object
    df = pd.DataFrame(h.history)
    n_epochs = df.shape[0]
    temp = df.iloc[(n_epochs-6):(n_epochs-1),:].mean(axis=0)
    temp = temp.to_frame()
    temp.rename(columns={0: 'value'}, inplace=True)
    temp = temp.transpose()
    
    ## add columns to dataframe
    temp['max_val_pearson'] = max_val_pearson
    temp['n_epochs'] = h.params['epochs']
    temp['sample_size'] = len(phenotypes)
    temp['validation_split'] = config_dict['val_split']
    temp['trait'] = trait
    temp['nparams'] = nparams
    temp['replicate'] = replicate
    
    ## NN hyperparameters
    temp['learn_rate'] = repr(config_dict['learn_rate'])
    temp['conv_filter'] = "_".join([str(x) for x in config_dict['conv_filter']])
    temp['pool_filter'] = "_".join([str(x) for x in config_dict['pool_filter']])
    temp['drop_rate'] = repr(config_dict['drop_rate'])
    temp['dense_nodes'] = "_".join([str(x) for x in config_dict['dense_nodes']])
    temp['conv_layers'] = "_".join([str(x) for x in config_dict['conv_layers']])
    
    column_names = ["trait","sample_size","learn_rate","drop_rate","conv_filter",
                    "conv_layers","pool_filter","dense_nodes","validation_split",
                    "n_epochs","loss","pearson","rmse","val_loss","val_pearson",
                    "val_rmse","max_val_pearson","nparams","replicate"]
    
    temp = temp.reindex(columns=column_names)
    
    return temp

def writeout_results(res, filename):
    
    if os.path.exists(filename):
        res.to_csv(filename, mode='a', header=False)
        return "File '{}' already exists, appending results to it".format(filename)
    
    else:
        os.makedirs(os.path.dirname(filename))
        res.to_csv(filename, mode='w', header=True)
        return "Creating file '{}' and writing results to it".format(filename)
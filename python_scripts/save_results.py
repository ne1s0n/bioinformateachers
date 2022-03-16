#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 11:50:14 2022

@author: filippo
"""

""" Function(s) to collect results from deep learning runs """

import os
import re
import json
import numpy as np
import pandas as pd

def make_file_names(trait,config_dict,replicate,extension='png'):
    
    print("making file names for trait ", trait)
    ## from config dict keep: num_epochs, val_split, learn_rate, conv_filter,
    ## pool_filter, drop_rate, dense_layers, conv_layers
    params = [x for x in config_dict.keys() if x not in ['input_shape',
                                                    'conv_padding','batch_size']]
    naam = "_".join([repr(config_dict[x]) for x in params])
    
    ## process string to strip special characters and replace with '_'
    naam = re.sub("[,\]\[\(\)]", "", naam)
    naam = re.sub(" ", "_", naam)
    
    ## attach replicate number and desired extension
    naam = naam + '_' + replicate + '.' + extension
    
    return naam

#get results to be saved
def parse_history(h, phenotypes, trait, config_dict, max_val_pearson, nparams, replicate):
    
    ## get metrics from history object
    df = pd.DataFrame(h.history)
    n_epochs = df.shape[0]
    temp = df.iloc[(n_epochs-10):(n_epochs-1),:].mean(axis=0)
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
    #temp['learn_rate'] = repr(config_dict['learn_rate'])
    #temp['conv_filter'] = "_".join([str(x) for x in config_dict['conv_filter']])
    #temp['pool_filter'] = "_".join([str(x) for x in config_dict['pool_filter']])
    #temp['drop_rate'] = repr(config_dict['drop_rate'])
    #temp['dense_layers'] = "_".join([str(x) for x in config_dict['dense_layers']])
    #temp['conv_layers'] = "_".join([str(x) for x in config_dict['conv_layers']])
    #temp['conv_padding'] = config_dict['conv_padding']
    
    #total config in a single column
    temp['config'] = json.dumps(config_dict)
    
    column_names = ["trait","sample_size",
                    "validation_split",
                    "n_epochs","loss","pearson","rmse","val_loss","val_pearson",
                    "val_rmse","max_val_pearson","nparams","replicate", "config"]
    
    temp = temp.reindex(columns=column_names)
    
    return temp

def writeout_results(res, filename):
    
    if os.path.exists(filename):
        res.to_csv(filename, mode='a', header=False)
        return "File '{}' already exists, appending results to it".format(filename)
    
    else:
        basedir = os.path.dirname(filename)
        if os.path.isdir(basedir):
            res.to_csv(filename, mode='w', header=True)
            return "Creating file '{}' and writing results to it".format(os.path.basename(filename))
        else:
            os.makedirs(os.path.dirname(filename))
            res.to_csv(filename, mode='w', header=True)
            return "Creating folder '{}' and writing results to file {}".format(basedir, os.path.basename(filename))

def get_predictions(model, val_x, val_y, config):
    
    ## calculate predictions and make DF with y and y_hat
    predictions = model.predict(val_x)
    predictions = np.concatenate(predictions, axis=0 )
    temp = pd.DataFrame({'y':val_y, 'y_hat':predictions})
    
    print('dataframe with {} predictions created'.format(len(temp)))
    
    ## make dataframe with config options
    d = dict([[k,[str(v)]] for k,v in config.items()])
    df = pd.DataFrame.from_dict(d)
    
    ## replicate configs for number of rows (predictions)
    df = pd.concat([df]*len(temp), ignore_index=True)
    
    ## combine y, y_hat and configs into one dataframe
    preds = pd.concat([temp, df], axis=1)
    
    return preds
    

    
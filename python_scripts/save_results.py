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
def parse_history(h, phenotypes, val_split, trait):
    
    ## get metrics from history object
    df = pd.DataFrame(h.history)
    n_epochs = df.shape[0]
    temp = df.iloc[int(n_epochs/2):(n_epochs-1),:].mean(axis=0)
    temp = temp.to_frame()
    temp.rename(columns={0: 'value'}, inplace=True)
    temp = temp.transpose()
    
    ## add columns to dataframe
    temp['n_epochs'] = h.params['epochs']
    temp['sample_size'] = len(phenotypes)
    temp['validation_split'] = val_split
    temp['trait'] = trait
    
    column_names = ["trait","sample_size","validation_split","n_epochs","loss",
                    "pearson","rmse","val_loss","val_pearson","val_rmse"]
    
    temp = temp.reindex(columns=column_names)
    
    return temp

def writeout_results(res, filename):
    
    if os.path.exists(filename):
        res.to_csv(filename, mode='a', header=False)
    else:
        res.to_csv(filename, mode='w', header=True)
        
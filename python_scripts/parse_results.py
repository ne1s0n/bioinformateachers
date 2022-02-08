#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 14:54:22 2022

@author: filippo
"""

""" Function(s) to parse results files from deep learning runs """

#%% libraries
import os
import re
import json
import pandas as pd

#%% function to parse results from keras
def parse_results(filepath):
    
    basename = os.path.basename(filepath)
    basefolder = os.path.dirname(filepath)
    
    print("Reading file '{}' from folder '{}'".format(basename, basefolder))
    temp = pd.read_csv(filepath)
    temp = temp.drop(temp.columns[[0]], axis=1)
    curr_cols = [x for x in temp.columns]  
    
    print(" - making new columns")
    new_cols = set()
    for row in temp['config']:
        rr = json.loads(row)
        for naam in rr.keys():
            if not naam in curr_cols: 
                new_cols.add(naam)
    
    print(" - populating new columns")
    config_res = dict() 
    for row in temp['config']:
        rr = json.loads(row)
        for k,v in rr.items():
            if isinstance(v, list):
                val = '_'.join([repr(x) for x in v])
            else:
                val = repr(v)
                
            config_res.setdefault(k, []).append(val)

    temp = temp.drop('config', axis=1)
    res = pd.concat([temp.reset_index(drop=True), pd.DataFrame(config_res)], axis=1)
    
    print(" - returning dataframe of results")
    
    return res


#%%
fname = "/home/filippo/Documents/deep_learning_for_breeding/results/results_temp.csv"
res = parse_results(fname)
avg = res.groupby(['num_epochs'])['val_pearson'].mean()
print(avg)

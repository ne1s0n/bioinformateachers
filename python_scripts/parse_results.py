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

#%% function to read results and return a Pandas dataframe for further analysis
#%% optionally if an outiflepath is passed the dataframe is saved as csv
def parse_results(filepath, outfilepath = None):
    
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
    
    print(new_cols)
    print(" - populating new columns")
    config_res = dict() 
    for row in temp['config']:
		#local copy of the list of variable params
        new_cols_cur = new_cols.copy()
		
		#parsing the values in the current row
        rr = json.loads(row)
        for k,v in rr.items():
            new_cols_cur.remove(k)
            if isinstance(v, list):
                val = '_'.join([repr(x) for x in v])
            else:
                val = repr(v)
            config_res.setdefault(k, []).append(val)
        
        #adding the columns that were not present in this row as blanks
        for k in new_cols_cur:
            config_res.setdefault(k, []).append(None)
         

    temp = temp.drop('config', axis=1)
    
    #putting together fixed and variable columns
    a = temp.reset_index(drop=True)
    b = pd.DataFrame(config_res)
    res = pd.concat([a, b], axis=1)
    
    #should we save a csv?
    if outfilepath is not None:
        res.to_csv(outfilepath)
    
    print(" - returning dataframe of results")
    return res


#%%
#fname = "/home/filippo/Documents/deep_learning_for_breeding/results/results_temp.csv"
#res = parse_results(fname)
#avg = res.groupby(['num_epochs'])['val_pearson'].mean()
#print(avg)

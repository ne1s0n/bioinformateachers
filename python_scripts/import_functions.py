#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 16:02:49 2021

@author: filippo
"""

"""
importing relevant libraries
"""
import os
import glob
import requests
import itertools

import numpy as np
import pandas as pd

"""
FUNCTIONS
"""

## function to create list of file names
def make_filenames():
    
    ktype = ['additive','dominance','epistasis_AA','epistasis_AD','epistasis_DD']
    minMAF = ['0.01','0.05']
    maxMAF = ['0.05', '0.5']

    temp = ["kinship_"+x for x in ktype]
    tmp = []
    for l in itertools.product(temp,minMAF):
        tmp.append('_minMAF'.join(l))

    fnames = []
    for l in itertools.product(tmp,maxMAF):
        min_maf = float(l[0][-4:])
        if min_maf < float(l[1]):
            fnames.append('_maxMAF'.join(l))

    del(temp,tmp)
    fnames = [x+'.csv.gz' for x in fnames]
    
    return fnames

"""
testing the function
"""
# fnames = make_filenames()
# print("List of file names to download", fnames)

## function that downloads data files
def download_files(target_dir,remote_data_folder):
    
    print('create folder', target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    fnames = make_filenames()
    
    filenames = glob.glob(target_dir + '*')
    filenames = [os.path.basename(x) for x in filenames]
    
    for name in fnames:
        if name.strip(".gz") in filenames:
            continue
        else:
            url = remote_data_folder + name
            print("Downloading", url)
            r = requests.get(url)
            open(target_dir + name.strip(".gz"), 'wb').write(r.content)


## function to stack kinships into a 3D array
def stack_kinship(base_dir):
    
    filenames = glob.glob(base_dir + '*')
    filenames = [os.path.basename(x) for x in filenames]
    
    array_list = []
    for filex in filenames:
        print("reading", filex)
        path_to_file = base_dir + filex
        temp = pd.read_csv(path_to_file, index_col=0).to_numpy()
        array_list.append(temp)
    
    k = np.array(array_list)
    print("The shape of the resulting 3-D array is:")
    print(k.shape)
    
    return k


## function that downloads the phenotype data files
## by default the sorted phenotypes (otherwise unsorted)
def download_phenotype_files(target_dir,remote_data_folder,fnaam='phenotypes',is_sorted=True):
    
    print('create folder', target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    fnames = [fnaam + "_sorted.csv"] if is_sorted == True else [fnaam + ".csv"] 
    
    filenames = glob.glob(target_dir + '*.csv')
    filenames = [os.path.basename(x) for x in filenames]
    
    for name in fnames:
        print("File", name)
        if name in filenames:
            continue
        else:
            url = remote_data_folder + name
            print("Downloading", url)
            r = requests.get(url)
            open(target_dir + name, 'wb').write(r.content)
    print("Done!")


## load the phenotypic data
## read the file and select the trait
## convert to either a 1d or 2d array
def load_phenotypes_and_select_trait(base_dir, trait, fnaam='phenotypes', is_sorted=True, df_output=False):
    
    fname = fnaam + '_sorted.csv' if is_sorted == True else fnaam + '.csv'
    print("select trait {} from phenotype file {}".format(trait,base_dir+fname))
    
    path_to_file = base_dir + fname
    temp = pd.read_csv(path_to_file, index_col=0)
    
    print("The selected trait is ", trait)
    
    ## if we want a pandas dataframe with two columns (sample, trait)
    if df_output == True:
        temp.reset_index(inplace=True)
        temp = temp.rename(columns = {'index':'sample'})
        phen = temp[["sample", trait]]
    else:
    ## convert to numpy.array and return (1d array, sorted as the input file and as the kinship matrix)
        phen = temp[trait].to_numpy()
    
    return phen
    
    

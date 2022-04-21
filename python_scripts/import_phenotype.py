#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:00:47 2021

@author: filippo
"""

"""
Python script that uses import functions to download data files from a remote URL
and then reads them into Python
The final phenotype data is a 1d array (sorted) or a 2d pandas dataframe 
with ['sample_name', 'trait']

If set is_sorted to True (default) the sorted phenotypes are loaded
"""

import os
import argparse
from import_functions import download_phenotype_files, load_phenotypes_and_select_trait


# Create the parser
parser = argparse.ArgumentParser(description='Import data for deep learning')

# Add arguments
parser.add_argument('-r', '--remote_folder', type=str, required=True, 
                    help='name of the remote folder from where sorted kinship matrices are downloaded')
parser.add_argument('-s', '--target_dir', type=str, required=True, 
                    help='directory where data are to be stored (created if needed)')
parser.add_argument('-d', '--dataset', type=str, required=True, 
                    help='dataset (e.g. cattle, maize, tropical_maize, etc.)')
parser.add_argument('--fname', type=str, required=True, default='phenotypes',
                    help='basename (without extension) of phenotype file to be downloaded')
parser.add_argument('--sorted', type=bool, required=False, default=True,
                    help='should the sorted (default) or unsorted phenotype data be downloaded?')
parser.add_argument('-p', '--trait', type=str, required=True,
                    help='Name of the trait to use for predictions (column of the phenotype file)')
parser.add_argument('--outtype', type=str, required=False, default=False,
                    help='Should the function return a 2d Pandas dataframe (True) or a 1d numpy array (False, default)')
# Parse the argument
args = parser.parse_args()

# Print to check arguments values
print('Remote folder is:', args.remote_folder)
print('Target folder is:', args.target_dir)
print('Dataset is:', args.dataset)
print('Name of file to download is:', args.fname)
print('Sorted or not?', 'sorted' if args.sorted == True else 'non sorted')
print('Selected trait:', args.trait)
print('Output type:', '2d Pandas dataframe' if args.outtype == True else '1d numpy array')

#### Set up of parameters and libraries
## SETTINGS #######################

# where the kinship data are stored
#DATAFOLDER_URL = 'http://www.jackdellequerce.com/data/cattle/phenotypes/'
remote_data_folder = os.path.join(args.remote_folder,'')

# where to place the data
#downloaded_data = '/content/data/'
downloaded_data = args.target_dir
#downloaded_data = '/home/filippo/Documents/deep_learning_for_breeding/'

# specific dataset
#dataset='cattle/'
dataset = args.dataset

#base_dir = downloaded_data + dataset
base_dir = os.path.join(downloaded_data, dataset, '')
####################################


print('Data will be downloaded to:', base_dir)

# ### Load the phenotype data
#
# The phenotype data are read from a csv file; the desired trait is then selected, 
# and an ordered one-dimensional array (or a `Pandas` dataframe with two columns: `sample` and `trait`) 
# is created where the phenotype data are stored

download_phenotype_files(base_dir, remote_data_folder, fnaam=args.fname, is_sorted=args.sorted)

#trait = 'simphe_mean0_hSquare0.7_cv0.1_QTN100_A10_D0_AA0_AD0_DA0_DD0_epoch1642079623'
trait = args.trait
phenotypes = load_phenotypes_and_select_trait(base_dir, trait, fnaam=args.fname, is_sorted=args.sorted, 
                                              df_output=args.outtype)

#print(phenotypes)
print("Data have been loaded!")
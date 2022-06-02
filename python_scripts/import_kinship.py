#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:00:47 2021

@author: filippo
"""

"""
Python script that uses import functions to download data files from a remote URL
and then reads them into Python
These files are amtrices (2D arrays) that are then stacked together
into a 3D array

By changing the variable part of the parameter 'base_dir'
you can store kinship data files (with the same name structure)
into different subfolders (e.g. /cattle/)
"""

import os
import argparse
from import_functions import make_filenames, download_files, stack_kinship, download_files2


# Create the parser
parser = argparse.ArgumentParser(description='Import data for deep learning')

# Add arguments
parser.add_argument('-r', '--remote_folder', type=str, required=True, 
                    help='name of the remote folder from where sorted kinship matrices are downloaded')
parser.add_argument('-s', '--target_dir', type=str, required=True, 
                    help='directory where data are to be stored (created if needed)')
parser.add_argument('-d', '--dataset', type=str, required=True, 
                    help='dataset (e.g. cattle, maize, tropical_maize, etc.)')
# Parse the argument
args = parser.parse_args()

# Print to check arguments values
print('Remote folder is:', args.remote_folder)
print('Target folder is:', args.target_dir)
print('Dataset is:', args.dataset)

#### Set up of parameters and libraries
## SETTINGS #######################

# where the kinship data are stored
#remote_data_folder = 'http://www.jackdellequerce.com/data/cattle/kinships_sorted/'
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

# ### Load the genotype data
#
# Kinship matrices are read from gzipped csv files, and then stacked together in a 3D array

make_filenames()
#download_files(target_dir=base_dir, remote_data_folder=remote_data_folder)
download_files2(target_dir=base_dir, remote_data_folder=remote_data_folder)
kinship = stack_kinship(base_dir=base_dir)

print("the object 'kinship' has been created, with dimensions {}".format(kinship.shape))
print("Kinship has been loaded!")


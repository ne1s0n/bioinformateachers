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

# ### Set up of parameters and libraries

## SETTINGS #######################
# where the kinship data are stored
remote_data_folder = 'http://www.jackdellequerce.com/data/cattle/kinships_sorted/'

# where to place the data
downloaded_data = '/content/data/'
#downloaded_data = '/home/filippo/Documents/deep_learning_for_breeding/'
dataset='cattle/'
#dataset='temp/'
base_dir = downloaded_data + dataset
####################################

from import_functions import make_filenames, download_files, stack_kinship

# ### Load the genotype data
#
# Kinship matrices are read from gzipped csv files, and then stacked together in a 3D array

# make_filenames()
download_files(target_dir=base_dir, remote_data_folder=remote_data_folder)
kinship = stack_kinship(base_dir=base_dir)

print("the object 'kinship' has been created, with dimensions {}".format(kinship.shape))

# ### Load the phenotype data
#
# The phenotype data are read from a csv file; the desired trait is then selected, and an ordered one-dimensional array (or a `Pandas` dataframe with two columns: `sample` and `trait`) is created

# +
# where the phenotype data are stored
DATAFOLDER_URL = 'http://www.jackdellequerce.com/data/cattle/phenotypes/'

from import_functions import download_phenotype_files, load_phenotypes_and_select_trait
# -

download_phenotype_files(base_dir, DATAFOLDER_URL,is_sorted=True)

trait = 'simphe_mean0_hSquare0.7_cv0.1_QTN100_A10_D0_AA0_AD0_DA0_DD0_epoch1642079623'
phenotypes = load_phenotypes_and_select_trait(base_dir, trait, is_sorted=True, df_output=False)

print(phenotypes)

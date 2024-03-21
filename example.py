# %reset -f

#This is how you can add data to an HDF5!
#There are 3 main steps. Data reading, data input into HDF5's, and then interacting with the database!
#Interacting with the database includes searching it, plotting everything from a specific filename, plotting individual traces, etc.

#First step, read the data and output it in a useable format!

#os is for controlling windows explorer mainly
import os
#plt is for plotting
import matplotlib.pyplot as plt
#for regexp operator stuff
import re
import numpy as np
import time

directory=r'C:\Users\jadse\Desktop\\' #Make sure this ends in a '\'
fileNameee='test.asc' #test.asc was 240229_2.asc
data, notebook, technique, notebookHeaders = Reader_HEKA_JonFormat(directory,fileNameee)



#Second step, put the data into an HDF5 file!

import h5py
import random

#If an HDF5 file doesn't exist, you can call this function. It will overwrite the HDF5 file if you let it.

HDF5_creator(r'C:\Users\jadse\Desktop','testHDF5.hdf5')

#Once it exists, you can put the data you created earlier into it!

# DBLocation=r'C:\Users\jadse\Desktop\Postdoc\Data\HEKAmaster.hdf5'
DBLocation=r'C:\Users\jadse\Desktop\testHDF5.hdf5'
DBEntryName='tests'
metadata=[['FileName',fileNameee],
          ['Date',fileNameee[:-4]],
          ['Operator','Jman'],
          ['Technique','CV'],
          ['Project','Medtronics'],
          ['Instrument','ELP3_Glovebox'],
          ['Sample','TNO'],
          ['Sample Preparation','Au'],
          ['Redox Mediator','NA'],
          ['Mediator Concentration','NA'],
          ['Capillary Radius','10'],
          ['Reference Electrode','AlLi/Li'],
          ['Approach Speed','3'],
          ['Approach Potential','3'],
          ['Solvent','PC']]
         
Add2HDF5(DBLocation, DBEntryName, data, notebook, notebookHeaders, metadata)


#Check what entries have been added.
with h5py.File(r'C:\Users\jadse\Desktop\testHDF5.hdf5', "r") as f:
    print(f.keys())

#This is to delete an HDF5 entry if you wanted to. You can delete attributes and groups the same way.

with h5py.File(r'C:\Users\jadse\Desktop\testHDF5.hdf5', "a") as f:
    del f[DBEntryName]
    print('Deletion was successful.')

#Check if it was deleted.
with h5py.File(r'C:\Users\jadse\Desktop\testHDF5.hdf5', "r") as f:
    print(f.keys())

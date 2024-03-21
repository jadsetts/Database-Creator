#If an HDF5 file hasn't been created, then call this function!

def HDF5_creator(dir,fn):
    f = h5py.File(dir+'\\'+fn, "w")
    print('Your HDF5 was successfully created in '+dir+'\\'+fn+'.')

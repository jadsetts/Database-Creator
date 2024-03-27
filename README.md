# Database-Creator

This series of files will read data into a specific format. Ideally, in the future, there will be many types of reader programs that all have the exact same output. These readers will output the exact same objects. These objects will then be placed into an HDF5 file that will be acting as a database to store all data, notebook information and data-specific information. This database is searchable and will ideally be used by research groups to be able to look at past students work, or perform large data analyses on many data scans.

HDF5_Creator will create an HDF5 file if you want to create a new HDF5 for a new project or just the initial one.

Reader_HEKA_JonFormat will read a HEKA file from the glovebox ELP3 that was exported with Universal.onl. The outputs are appropriately formatted for direct use with ADD2HDF5. If you don't use the HEKA or are going to use another instrument, you must spend time ensuring your outputs are identical to the outputs of this program and that the HDF5 file you are creating with ADD2HDF5 is appropriate and what you want.

ADD2HDF5 will add the outputs from Reader_HEKA_JonFormat and input them into an HDF5 file. An electronic notebook will also be created and added to the highest level of the new input for the HDF5 file.

example.py goes over an example workflow of how you could be reading data from a random file and inputting it into the HDF5 file.


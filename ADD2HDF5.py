#HEKA ASC notebook file import.
#This takes everything you just created in the cell above and adds it to the master HDF5 file you specify.
#Make sure the file is opened in 'a' mode and not 'w' mode. 'w' mode deletes all other HDF5 entries.

def Add2HDF5(dir, fileName, data, notebook, notebook_header, metaD):

    #Putting something here that checks if the file exists would be nice.
    
    #This will get us the column we want from the numpy array called 'data' created earlier.
    def getColumnData(seriesNumber,sweepNumber,columnNumber):
        newList=[]
        for iiii in range(len(data[seriesNumber][sweepNumber])):
            newList.append(data[seriesNumber][sweepNumber][iiii][columnNumber])
        return newList
    
    with h5py.File(dir,'a') as f: #Make sure this is an 'a' and not 'w'. Only use 'w' once!!!
        
        #Build a framework to eventually put variables in.
        #If the filename doesn't exist, create a new entry
        #If it already exists, 
        if f.__contains__(fileName): #make sure the filename hasn't already been created
            metaData = f[fileName]
            dataDirectory= f[fileName]['Data']
            notebookDirectory = f[fileName]['Notebook']
        else:
            uniqueID=random.randint(0,1000000) #This is currently not used but could be used for your project!
            metaData = f.create_group(fileName)
            dataDirectory= metaData.create_group('Data')
            notebookDirectory = metaData.create_group('Notebook')

        
        #Add the data into the HDF5!
        for i in range(len(data)): #Series
            #Check to see if the data has alreadyb been added. We don't need to add it again.
            if f.__contains__(fileName+'/Data/Serie '+str(i)):
                print('This has already been added and was not overwritten.')
            else:
                series=dataDirectory.create_group('Serie '+str(i))
                
                for j in range(len(data[i])): #Sweep
                    # print(j) #good for troubleshooting
                    for k in range(len(data[i][j][0])): #Columns
                        series.create_dataset('Sweep'+str(j)+'Column'+str(k),data=getColumnData(i,j,k))

        #Add the notebook into the HDF5
        for i in range(len(notebook)):
            if f.__contains__(fileName+'/Notebook/Serie '+str(i)):
                myFavoriteColor='The most intense color for humans.'
            else:
                notebookSeries=notebookDirectory.create_group('Serie '+str(i)) 

                for j in range(len(notebook[i])): #Sweep
                    # print(j) #good for troubleshooting
                    if notebook:
                        for l in range(len(notebook[i][j])): #Notebook placements, I suppose just like columns.
                            notebookSeries.attrs[notebook_header[0][l].strip()+str(j)] = notebook[i][j][l] 

        #Add the metadata into the HDF5!
        for i in range(len(metaD)):
            metaData.attrs[metaD[i][0]] = metaD[i][1]

        #Check to see if the file was successfully added.
        flag=0
        for i in f.keys():
            print(i)
            if i == fileName:
                print(fileName+' was successfully added to the HDF5 file specified.')
                flag=1
        if flag == 0:
            print(fileName+' was not added to the HDF5 file specified.')
    

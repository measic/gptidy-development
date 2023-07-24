%matplotlib inline

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
from sklearn import datasets, linear_model
from sklearn.cross_validation import KFold    
import sklearn
from sklearn.metrics import mean_squared_error

# THIS IS TO READ FROM A DAT FILE AND GET A LIST OF LIST WITH WITH EACH COULOUMN AS A LIST
getListFromAFile= lambda filename:np.loadtxt(filename, unpack=True)

# returning the list of all the file  in the folder
getListOfFiles = lambda directoryPath :[f for f in os.listdir(directoryPath) if os.path.isfile(os.path.join(directoryPath, f))] # this is to list all files

# GENRAL CUSTOM 2D PLOTS SCATTER PLOTS
def createPlots(inputList_x,inputList_y,xlabel="x-axis -->",ylabel="y-axis -->",title="file-Name-Title",plotterRef=None):
    #this is for linear regression
    if plotterRef is not None:
        plt.scatter(inputList_x,plotterRef(inputList_x),alpha=0.5,color ='r')   
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(inputList_x,inputList_y,alpha=0.5,color ='b')
    plt.show()

def showDataInFile(directoryPath):
    with open("Data/"+directoryPath,'r') as f:
        next(f) # skip first row
        df = pd.DataFrame(l.rstrip().split() for l in f)
        df.boxplot
        print(df)

# this like the the execution main
# displaying all the files in Data/ folder  and ploting them
for s in getListOfFiles('Data/'):
    data = getListFromAFile("Data/"+s)
    createPlots(data[0],data[1],'x-axis -->','y-axis -->',s)
    #showDataInFile(s)
    clf = linear_model.LinearRegression()
    clf.fit(data[0].reshape(-1,1),data[1])
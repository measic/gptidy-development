#dtype converts this from a integer to boolean array
err = np.array([1,0,0,0,0,0,0,1,0,1,0,0],dtype=bool)
print(err)
#Let's set all of the data with errors to np.nan so that they will be ignored in subsequent calc
# first convert the data to float type which is compatible with np.nan insertion (unlike integer arrays)
newdat = np.array(data,dtype=float)
print(newdat)
# insert the np.nan where the errors are according to mask err.
newdat[err==True] = np.nan
print(newdat)
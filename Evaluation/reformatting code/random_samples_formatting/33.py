#importing clustering libaries 
from scipy.cluster.hierarchy import dendrogram, linkage 
from matplotlib import pyplot as plt
from scipy import cluster
shc = cluster.hierarchy

#preproccesing data for clustering
labels = vector.values[:,0]
data = vector.values[:,1:160]
plt.figure(figsize=(20, 10))  
plt.title("Clustering Hotels")  

# "ward" - minimizes the variance between clusters, that means that each two clusters were combine if their variance is close to each other 
Z = shc.linkage(data, method='ward')
dend = shc.dendrogram(Z, labels=labels) 
plt.show(dend)


# NOTES
# The purpose of finding groups of hotels with similarity in their pricing policy is to be able 
# to break a vacation into multiple different hotels which gurantees a minimum price.
# The naive solution is finding all the combinations for the desired date range.
# An alternative way is finding the cheapest hotel for the desired date and 
# performing a naive search of all the combinations within the current hotel's cluster, instead of searching all the hotels.

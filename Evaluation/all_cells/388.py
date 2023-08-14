from sklearn.cluster import AgglomerativeClustering

#running the algorithem again in a diffrent way
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
clusters = cluster.fit_predict(vector.values[:,1:160])  

hotels = pd.DataFrame.from_records(vector.values)

hotels["cluster"] = clusters
hotels = hotels[[0,"cluster"]]
hotels.sort_values(by=["cluster"],ascending=True,inplace=True)

hotels["Count"] = hotels.groupby("cluster")[0].transform("count")
hotels

# NOTES
# In order to understand our data and get a cleaer picture of out data, we have mapped the hotel names to clusters in a data frame.  
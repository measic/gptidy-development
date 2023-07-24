from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering


pca = PCA(n_components=2).fit(data)
pca_2d = pca.transform(data)

cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  
cluster.fit_predict(pca_2d)  

plt.figure(figsize=(10, 7))  
plt.scatter(pca_2d[:,0],pca_2d[:,1],c=cluster.labels_, cmap='rainbow')  

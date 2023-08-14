from sklearn.mixture import GMM
import matplotlib.pyplot as plt

gmm = GMM(2, covariance_type='full', random_state=0)
A=data1[["total_mass","center_of_Mass"]]
gmm.fit(A.values)
cluster_label = gmm.predict(A.values)
A.values[:, 0]
plt.scatter(A.values[:, 0], A.values[:, 1], c=cluster_label);
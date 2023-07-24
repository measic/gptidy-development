plt.rcParams["axes.facecolor"] = (1,1,.99) 
plt.rcParams["font.size"] = 15 
plt.rcParams["figure.figsize"] = (12,6) 
plt.rcParams["ytick.labelsize"] = 15 
plt.rcParams["xtick.labelsize"] = 15 
plt.rcParams["lines.linewidth"] = 2 
plt.rcParams["axes.titlesize"] = 20

#Histogram of probability predictions
probs = AdaModel.predict_proba(X_test)

fig, ax = plt.subplots(1,1, figsize = (12,6))
fig.suptitle("Histogram Shows How Model Assigns Probs to Match Likelihood", fontsize = 20)


ax.hist(probs[: ,1])
ax.set_title("Probs of Match")
ax.grid(alpha = 0)

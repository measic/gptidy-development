fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,8))

dfBabies.loc[dfBabies["smoke"]==0].hist(column="weight", ax=axes[0], facecolor="steelblue", edgecolor="white")                                                   
axes[0].set_title("Baby Weight of Non-Smokers", fontsize=20)
axes[0].set_xlabel("Baby Weight (in ounces)", fontsize=16)
axes[0].set_ylabel("Frequency", fontsize=16)
axes[0].set_axisbelow(True)


dfBabies.loc[dfBabies["smoke"]==1].hist(column="weight", ax=axes[1], facecolor="darkseagreen", edgecolor="white")
axes[1].set_title("Baby Weight of Smokers", fontsize=20)
axes[1].set_xlabel("Baby Weight (in ounces)", fontsize=16)
axes[1].set_ylabel("Frequency", fontsize=16)
axes[1].set_axisbelow(True)

# Set  axis limits to match
axes[0].set_xlim([30,180])
axes[1].set_xlim([30,180]);

fig.subplots_adjust(hspace=.5)
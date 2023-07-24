#plot important features except for playlist_pid
fig, ax = plt.subplots(1,1, figsize = (20,15))
y_pos = np.arange(len(not_pid_features) - 3)
ax.barh(not_pid_features[3:], not_pid_importances[3:], align = "center", color = "mediumspringgreen")
for tick in ax.get_xticklabels():
    tick.set_rotation(90)
ax.grid(alpha = 0)
ax.set_xlabel("Importance", fontsize = 20)
ax.set_ylabel("Features", fontsize = 20)
ax.yaxis.set_tick_params(labelsize=12)
ax.xaxis.set_tick_params(labelsize=15)

fig.savefig("Feature Importance.png", bbox_inches="tight")
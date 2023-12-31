fig = plt.figure(figsize=(5, 3))
plt.plot(y_score.sum(axis=0) / y_score.shape[0])
plt.xlim((0, y_score.shape[1]))
plt.xlabel('timestep')
plt.ylim((0, 1))
plt.ylabel('classifier score')
plt.grid(True)
plt.savefig(os.path.join(msig.out_dir, 'mean_accuracy_vs_timestep.png'))
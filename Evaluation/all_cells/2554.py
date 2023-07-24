barwidth = 0.75; 
fig, ax = plt.subplots(figsize=(9, 7));
rects1 = ax.bar(0.5,ACCanalysis.Valid.mean(),barwidth,yerr=ACCstderror.Valid,ecolor='k',edgecolor=sns.xkcd_rgb['green'],linewidth = 2, facecolor='none',error_kw=dict(lw=3));
rects2 = ax.bar(1.5,ACCanalysis.Invalid.mean(),barwidth,color=sns.xkcd_rgb['green'],yerr=ACCstderror.Invalid,ecolor='k',error_kw=dict(lw=3));
sns.set(context='notebook', style='white', font='Myriad Pro', font_scale=2, color_codes=False, rc=None);
ax.set_ylim(0.65,1.00);
ax.set_xlim(0,2.5);
ax.set_xticklabels(('Valid', 'Invalid'));
ax.set_xticks([0.5 + barwidth/2, 1.5 + barwidth/2]);
ax.set_yticks(np.arange(0.65, 1.01, 0.05));
plt.title('S-S Phase Accuracy', fontsize=26,fontweight="bold")
plt.ylabel('Reaction Time (ms)', fontsize=24,fontweight="bold")
plt.xlabel('Trial Type', fontsize=24,fontweight="bold")
sns.despine();

plt.show()
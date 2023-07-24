barwidth = 0.75; 
fig, ax = plt.subplots(figsize=(9, 7));
rects1 = ax.bar(0.5,RTanalysis.Valid.mean(),barwidth,yerr=RTstderror.Valid,ecolor='k',edgecolor=sns.xkcd_rgb['green'],linewidth = 2, facecolor='none',error_kw=dict(lw=3));
rects2 = ax.bar(1.5,RTanalysis.Invalid.mean(),barwidth,color=sns.xkcd_rgb['green'],yerr=RTstderror.Invalid,ecolor='k',error_kw=dict(lw=3));
sns.set(context='notebook', style='white', font='Myriad Pro', font_scale=2, color_codes=False, rc=None);
ax.set_ylim(550,610);
ax.set_xlim(0,2.5);
ax.set_xticklabels(('Valid', 'Invalid'));
ax.set_xticks([0.5 + barwidth/2, 1.5 + barwidth/2]);
ax.set_yticks(np.arange(550, 611, 10));
plt.title('S-S Phase RT', fontsize=26,fontweight="bold")
plt.ylabel('Reaction Time (ms)', fontsize=24,fontweight="bold")
plt.xlabel('Trial Type', fontsize=24,fontweight="bold")
sns.despine();

plt.show()
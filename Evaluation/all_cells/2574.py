SCFC = posttest.groupby(['subjID'])['Q3_SC_ForcedChoicePerformance'].mean()
SCFCSEM = pd.Series.std(SCFC) / n
SCTFC = posttest.groupby(['subjID'])['Q3_SCT_ForcedChoicePerformance'].mean()
SCTFCSEM = pd.Series.std(SCTFC) / n

barwidth = 0.75; 
fig, ax = plt.subplots(figsize=(8, 6));
rects1 = ax.bar(0.5,SCFC.mean(),barwidth,color=sns.xkcd_rgb['green'],yerr=SCFCSEM,ecolor='k',error_kw=dict(lw=3));
rects4 = ax.bar(1.5,SCTFC.mean(),barwidth,yerr=SCTFCSEM,ecolor='k',edgecolor=sns.xkcd_rgb['green'],linewidth = 2,facecolor='none', error_kw=dict(lw=3));
sns.set(context='notebook', style='white', font='Myriad Pro', font_scale=2, color_codes=False, rc=None);
ax.set_ylim(0,4.1);
ax.set_xlim(0,2.5);
plt.plot([0,1,2,2.5],[2,2,2,2], 'r--');
ax.set_xticklabels(('S-C','S-CT'));
ax.set_xticks([0.5 + barwidth/2, 1.5 + barwidth/2]);
ax.set_yticks(np.arange(0, 5, 1));
plt.title('Q3: Match the Scene/Face/House to Its\nMost Likely Trial Type', fontsize=18,fontweight="bold")
plt.ylabel('Performance (# Pairs Correct)', fontsize=17,fontweight="bold")
plt.xlabel('Task Phase', fontsize=17,fontweight="bold")
sns.despine();

plt.show()
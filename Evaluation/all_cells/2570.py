barwidth = 0.75; 
fig, ax = plt.subplots(figsize=(9, 7));
rects1 = ax.bar(0.5,SkyPresence.mean(),barwidth,color=sns.xkcd_rgb['green'],yerr=SkyPresenceSEM,ecolor='k',error_kw=dict(lw=3));
rects2 = ax.bar(1.5,ColorScheme.mean(),barwidth,color=(0.3,0.9,0.3),yerr=ColorSchemeSEM,ecolor='k',error_kw=dict(lw=3));
rects3 = ax.bar(2.5,TreeFreq.mean(),barwidth,color=(0.15,1,0.15),yerr=TreeFreqSEM,ecolor='k',error_kw=dict(lw=3));
rects4 = ax.bar(4,ImageType.mean(),barwidth,yerr=ImageTypeSEM,ecolor='k',edgecolor=sns.xkcd_rgb['green'],linewidth = 2,facecolor='none', error_kw=dict(lw=3));
rects5 = ax.bar(5,FeatureType.mean(),barwidth,yerr=FeatureTypeSEM,ecolor='k',edgecolor=(0.3,0.9,0.3),linewidth = 2,facecolor='none', error_kw=dict(lw=3));
rects6 = ax.bar(6,LightType.mean(),barwidth,yerr=LightTypeSEM,ecolor='k',edgecolor=(0.15,1,0.15),linewidth = 2, facecolor='none',error_kw=dict(lw=3));
sns.set(context='notebook', style='white', font='Myriad Pro', font_scale=2, color_codes=False, rc=None);
ax.set_ylim(0,100);
ax.set_xlim(0,7.5);
ax.set_xticklabels(('SP','CS','TF','IT','FT','LT'));
ax.set_xticks([0.5 + barwidth/2, 1.5 + barwidth/2, 2.5 + barwidth/2, 4 + barwidth/2, 5 + barwidth/2, 6 + barwidth/2]);
ax.set_yticks(np.arange(0, 101, 10));
plt.title('Q2: Rate the Frequency at Which These Perceptual Categories\nPredicted an Easy/Hard Color-Word Trial', fontsize=18,fontweight="bold")
plt.ylabel('<-- Less Likely      More Likely -->', fontsize=17,fontweight="bold")
plt.xlabel('S-C Phase                 S-CT Phase', fontsize=17,fontweight="bold")
sns.despine();

plt.show()
from pylab import polyfit, poly1d
fig, ax = plt.subplots(figsize=(9, 7));
plt.scatter(RTValidityEffect, posttest.ExplicitMem, s=50,c=sns.xkcd_rgb['green'],alpha=0.6,edgecolors='k');
sns.set(context='notebook', style='white', font='Myriad Pro', font_scale=2, color_codes=False, rc=None);
fit = polyfit(RTValidityEffect, posttest.ExplicitMem, 1);
fit_fn = poly1d(fit);
plt.plot(RTValidityEffect, fit_fn(RTValidityEffect), 'k');
plt.plot([-50,0,50,100,150],[2,2,2,2,2], 'r--');
ax.set_ylim(-0.1,4.1);
ax.set_xlim(-50,150);
plt.title('RT Validity Effect Predicts S-S Memory', fontsize=26,fontweight="bold");
plt.ylabel('S-S Memory Performance\n(# Pairs Correct)', fontsize=24,fontweight="bold");
plt.xlabel('S-S RT Validity Effect (ms)', fontsize=24,fontweight="bold");
sns.despine();

plt.show()
stats.linregress(RTValidityEffect,posttest.ExplicitMem) #see stats below graph
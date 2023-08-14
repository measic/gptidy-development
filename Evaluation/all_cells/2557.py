from pylab import polyfit, poly1d
fig, ax = plt.subplots(figsize=(10, 8));
plt.scatter(ACCValidityEffect, posttest.ExplicitMem, s=50,c=sns.xkcd_rgb['green'],alpha=0.6,edgecolors='k');
sns.set(context='notebook', style='white', font='Myriad Pro', font_scale=2, color_codes=False, rc=None);
fit = polyfit(ACCValidityEffect, posttest.ExplicitMem, 1);
fit_fn = poly1d(fit);
plt.plot(ACCValidityEffect, fit_fn(ACCValidityEffect), 'k');
plt.plot([-0.4,-0.3,-0.2,-0.1,0,0.1,0.2],[2,2,2,2,2,2,2], 'r--');
ax.set_ylim(-0.1,4.1);
ax.set_xlim(-0.4,0.2);
plt.title('ACC Validity Effect Predicts S-S Memory', fontsize=26,fontweight="bold");
plt.ylabel('S-S Memory Performance\n(# Pairs Correct)', fontsize=24,fontweight="bold");
plt.xlabel('S-S Accuracy Validity Effect (Proportion Correct)', fontsize=24,fontweight="bold");
sns.despine();

plt.show()
stats.linregress(ACCValidityEffect,posttest.ExplicitMem) #see stats below graph
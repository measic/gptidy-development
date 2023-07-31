plt.subplots(figsize=(16,8))
dfBabies.boxplot(column="weight", by="smoke", ax=ax, return_type="dict")

for _ in bp:
    for box in _['boxes']:
        box.set(color='steelblue', linewidth=2)
    
    for whisker in _['whiskers']:
        whisker.set(color='gray', linewidth=2)

    for cap in _['caps']:
        cap.set(color='gray', linewidth=2)

    for cap in _['medians']:
        cap.set(color='green', linewidth=2, alpha=0.5)

    for cap in _['fliers']:
        cap.set(markerfacecolor='steelblue', linewidth=2, marker='s', markersize=6, alpha=0.5)

plt.title('Weight of Smoker\'s Babies vs Non-Smoker\'s Babies', fontsize=18)
plt.ylabel("Weight (in Ounces)", fontsize=16)

plt.xticks(range(1,len(_)+1),_, rotation=90, fontsize=16)

plt.suptitle("")
plt.xlabel("")

plt.grid(alpha=0.25)
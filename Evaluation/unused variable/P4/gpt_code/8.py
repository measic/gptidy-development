_, ax = plt.subplots(figsize=(16,8))
bp = dfBabies.boxplot(column="weight", by="smoke", ax=ax, return_type="dict")

for column in bp:
    for box in column['boxes']:
        box.set(color='steelblue', linewidth=2)
    
    for whisker in column['whiskers']:
        whisker.set(color='gray', linewidth=2)

    for cap in column['caps']:
        cap.set(color='gray', linewidth=2)

    for cap in column['medians']:
        cap.set(color='green', linewidth=2, alpha=0.5)

    for cap in column['fliers']:
        cap.set(markerfacecolor='steelblue', linewidth=2, marker='s', markersize=6, alpha=0.5)

ax.set_title('Weight of Smoker\'s Babies vs Non-Smoker\'s Babies', fontsize=18)
ax.set_ylabel("Weight (in Ounces)", fontsize=16)

short_names = ["Non-Smoker", "Smoker"]
plt.xticks(range(1,len(short_names)+1),short_names, rotation=90, fontsize=16)

plt.suptitle("")
ax.set_xlabel("")

ax.grid(alpha=0.25)
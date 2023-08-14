fig, ax = plt.subplots(figsize=(7, 3));
Q1 = [18, 58];
labels = ['Yes','No']
colors = ['lightcoral', 'lightskyblue'];
patches, texts = plt.pie(Q1, colors=colors, startangle=90)
plt.legend(patches, labels, loc='lower left')
plt.title('Q1: Noticed Any Regularities, Sequences, or Pairs?', fontsize=17,fontweight="bold");
plt.axis('equal');
plt.show()
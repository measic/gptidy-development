variable_def = get_frequencies(y_train_augmented, sign_dict)
fig, ax = plt.subplots(figsize=(15, 10))
classes = list(sign_dict.values())
ind = np.arange(len(classes))
width = 0.8
rects = ax.bar(ind, variable_def.values(), width, align='edge', alpha=0.5)
ax.set_ylabel('Frequency')
ax.set_title('Traffic Sign Classes')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(variable_def.keys(), rotation=90)
plt.show()
plt.figure(figsize=(5,15))
x = np.arange(75)
labels = [elem[0] for elem in sorted_list[-75:][::-1]]
heights = [elem[1] for elem in sorted_list[-75:][::-1]]
bars = plt.barh(x, heights)

plt.yticks(x, labels)
plt.title("Top 75 least frequent words")
plt.show()
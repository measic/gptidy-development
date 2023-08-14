data = [len(s) for c in translate_conv for s in c]

plt.violinplot(data,showmedians=True, showextrema=False)
plt.ylabel("length of sentences")
plt.title("ViolinPlot (Showing density of tokenized sentences length)")
plt.show()
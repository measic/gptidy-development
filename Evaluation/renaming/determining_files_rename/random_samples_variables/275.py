ncomponents = 2
pca = decomp.PCA(n_components=ncomponents)
raw_pca = pca.fit(np.array(x_train.iloc[:, first_egemaps_feature:]).astype(np.float))
x_pca = raw_pca.transform(x_train.iloc[:, first_egemaps_feature:])
groups = x_train['pos']
short_pos = {'nouns': 'nn', 'verbs': 'vrb', 'other': 'oth', 'function_words': 'fct', 'adjectives': 'adj'}
group_values = [short_pos[i] for i in groups.unique()]
posIDs = groups.factorize()[0]
labels = np.array(x_train['word'])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')
colormap = plt.get_cmap('gnuplot', len(group_values))
pc1 = x_pca[:, 0]
pc2 = x_pca[:, 1]
p = ax.scatter(pc1, pc2, c=posIDs, cmap=colormap, s=10)
cb = plt.colorbar(p)
loc = np.arange(0, max(posIDs), max(posIDs) / float(len(group_values)))
cb.set_ticks(loc)
cb.set_ticklabels(group_values)
for label, x, y in zip(labels, pc1, pc2):
    if y == np.amax(y) or x == np.amax(x):
        plt.annotate(label, fontsize=2, xy=(x, y), xytext=(0, 1), textcoords='offset points', ha='right', va='bottom')
if pos_filter == None:
    axins = zoomed_inset_axes(ax, 2.5, loc=2)
    x1, x2, y1, variable_def = (-3.1, 2.5, 6.3, 9.8)
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, variable_def)
    axins.scatter(pc1, pc2, c=posIDs, cmap=colormap)
    plt.yticks(visible=False)
    plt.xticks(visible=False)
    mark_inset(ax, axins, loc1=2, loc2=4, fc='none', ec='0.5')
    for label, x, y in zip(labels, pc1, pc2):
        if y == np.amax(y) or x == np.amax(x):
            plt.annotate(label, fontsize=8, xy=(x, y), xytext=(0, 1), textcoords='offset points', ha='right', va='bottom')
    axins2 = zoomed_inset_axes(ax, 2.5, loc=4)
    x1, x2, y1, variable_def = (-4, 0.5, -8.5, -6.5)
    axins2.set_xlim(x1, x2)
    axins2.set_ylim(y1, variable_def)
    axins2.scatter(pc1, pc2, c=posIDs, cmap=colormap)
    plt.yticks(visible=False)
    plt.xticks(visible=False)
    mark_inset(ax, axins2, loc1=2, loc2=4, fc='none', ec='0.5')
    for label, x, y in zip(labels, pc1, pc2):
        if y == np.amax(y) or x == np.amax(x):
            plt.annotate(label, fontsize=8, xy=(x, y), xytext=(0, 1), textcoords='offset points', ha='right', va='bottom')
filename = corpus + '_full_zoom.pdf'
if pos_filter != None and len(pos_filter) == 1:
    filename = corpus + '_pca_' + pos_filter[0][1] + '_' + pos_filter[0][2] + '.pdf'
plt.savefig(filename, bbox_inches='tight')
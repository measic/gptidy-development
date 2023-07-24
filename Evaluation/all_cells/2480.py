ncomponents = 2

# you can select features of interest in this list and change iloc to loc in pca.fit and pca.transform below
# good_features = ['loudness_sma3_meanRisingSlope', 
#                  'spectralFluxV_sma3nz_stddevNorm',
#                  'mfcc2_sma3_amean',
#                  'mfcc4V_sma3nz_amean', 
#                  'MeanVoicedSegmentLengthSec']

# good_features = ['freq','equivalentSoundLevel_dBp']


pca     = decomp.PCA(n_components=ncomponents)
raw_pca = pca.fit(np.array(x_train.iloc[:,first_egemaps_feature:]).astype(np.float))
x_pca   = raw_pca.transform(x_train.iloc[:,first_egemaps_feature:])

# we want to check if natural data groupings can be recovered
# in the space spanned by the first two principle components
groups        = x_train['pos']

# get individual POS values
short_pos     = {'nouns':'nn', 'verbs':'vrb', 'other':'oth', 'function_words':'fct', 'adjectives':'adj'}
group_values  = [short_pos[i] for i in groups.unique()]

# map pos values to IDs
posIDs         = groups.factorize()[0]

# we want to label all data points in the plot with their word string
labels = np.array(x_train['word'])


# plot first two principle components
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('PC 1')
ax.set_ylabel('PC 2')

colormap = plt.get_cmap('gnuplot', len(group_values))

pc1 = x_pca[:,0]
pc2 = x_pca[:,1]

p = ax.scatter(pc1, pc2, c=posIDs, cmap=colormap, s=10)#, ) #, 

# add color bar
cb = plt.colorbar(p)
loc = np.arange(0,
                max(posIDs),
                (max(posIDs)/float(len(group_values))))
cb.set_ticks(loc)
cb.set_ticklabels(group_values)

for label, x, y in zip(labels, pc1, pc2):
    if y==np.amax(y) or x==np.amax(x) :
        plt.annotate(label,
                     fontsize=2,
                     xy=(x, y), xytext=(0, 1),
                     textcoords='offset points', ha='right', va='bottom')

if pos_filter == None:
    # add zoom number 1
    axins = zoomed_inset_axes(ax, 2.5, loc=2) # zoom-factor: 2.5, location: upper-left
    x1, x2, y1, y2 = -3.1, 2.5, 6.3, 9.8  # specify the limits
    axins.set_xlim(x1, x2) # apply the x-limits
    axins.set_ylim(y1, y2) # apply the y-limits
    axins.scatter(pc1, pc2, c=posIDs, cmap=colormap)
    plt.yticks(visible=False)
    plt.xticks(visible=False)
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

    for label, x, y in zip(labels, pc1, pc2):
        if y==np.amax(y) or x==np.amax(x) :
            plt.annotate(label,
                         fontsize=8,
                         xy=(x, y), xytext=(0, 1),
                         textcoords='offset points', ha='right', va='bottom')

    # add zoom number 2
    axins2 = zoomed_inset_axes(ax, 2.5, loc=4) # zoom-factor: 2.5, location: lower-right
    x1, x2, y1, y2 = -4, 0.5, -8.5, -6.5  # specify the limits
    axins2.set_xlim(x1, x2) # apply the x-limits
    axins2.set_ylim(y1, y2) # apply the y-limits
    axins2.scatter(pc1, pc2, c=posIDs, cmap=colormap)
    plt.yticks(visible=False)
    plt.xticks(visible=False)
    mark_inset(ax, axins2, loc1=2, loc2=4, fc="none", ec="0.5")


    for label, x, y in zip(labels, pc1, pc2):
        if y==np.amax(y) or x==np.amax(x) :
            plt.annotate(label,
                         fontsize=8,
                         xy=(x, y), xytext=(0, 1),
                         textcoords='offset points', ha='right', va='bottom')

filename = corpus+'_full_zoom.pdf'
if pos_filter != None and len(pos_filter)==1 :
    filename = corpus+'_pca_'+pos_filter[0][1]+'_'+pos_filter[0][2]+'.pdf'
    
plt.savefig(filename, bbox_inches='tight')
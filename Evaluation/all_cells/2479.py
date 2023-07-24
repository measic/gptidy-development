# compute and plot correlations


# if you like select a subset of features like this
# featureset = ['freq', 
#                'length']
#               'mfcc2_sma3_amean',
#               'mfcc4V_sma3nz_amean', 
#               'MeanVoicedSegmentLengthSec']
# x_selected = x_train[featureset].copy()
# print(x_selected.head(5))

# otherwise take the whole training set
x_selected  = x_train

# get correlation matrix
correlations= x_selected.corr()

# do the plotting
fig      = plt.figure()
ax1      = fig.add_subplot(111)
ax1.grid(True)
colormap = cm.get_cmap('jet', len(correlations.columns))
cax      = ax1.imshow(correlations, 
                      interpolation="nearest", 
                      cmap=colormap)
plt.title('EGEMAPS Feature Correlation')
labels=[str(i) for i in range(len(correlations.columns))]
fig.colorbar(cax)
fig.show()

# print features values with correlation higher than some threshold
threshold = 0.9
print("Features with abs(correlation) > 0.9 ")
for row in range(correlations.shape[0]):
    for col in range(correlations.shape[1]):
        val = correlations.iloc[row, col]
        if val != 1.0 and (val > threshold or val < (-threshold)):
            print(" --- ".join([str(val), 
                                str(row),
                                str(col),
                                correlations.index[row], 
                                correlations.columns[col]]))




y = pd.DataFrame(y_train)
y.columns = ['class']
y['index'] = y.index

gb = y.groupby(['class'])
#print(gb['index'].agg([np.min,np.max]))

num_image = 5
for c in range(n_classes):
    # filter 
    yf = y[y['class']== c].sample(num_image)
    idx = (yf['index'])
    fig = plt.figure()
    for i in range(num_image):
        fig.add_subplot(1,num_image,i+1)
        plt.imshow(X_train[idx][i])
        plt.text(0,1,signnames[str(c)],color='w',backgroundcolor='r', fontsize=5, weight="bold") 
        plt.axis('off')
    plt.tight_layout()
    plt.show()
    
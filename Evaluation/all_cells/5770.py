print('Selecting only the top 5 predictions and rerunning softmax')
num_own_examples = len(X2_norm)
for i in range(num_own_examples):
    
    probas = proba[i]
    names = np.asarray([signnames[str(p)] for p in predicts[1][i]])
    
    plt.figure(1)

    plt.subplot(221)
    plt.imshow(X2[i])
    plt.axis('off')
    
    plt.subplot(222)
    y_pos = np.arange(len(names))[::-1]
    plt.barh(y_pos,probas, align='center')
    plt.yticks(y_pos, names, fontsize=7)
    plt.xlabel('Probability')
    plt.title('Top 5 predictions')
    
    
    plt.tight_layout()
    plt.show()
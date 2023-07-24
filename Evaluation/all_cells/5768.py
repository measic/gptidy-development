for i in range(num_own_examples):
    
    probas = proba[i]
    
    highest_class = signnames[str(np.argmax(probas, axis =0))]
    
    plt.figure(1)

    plt.subplot(221)
    plt.imshow(X2[i])
    plt.title('Input image')
    plt.axis('off')
    
    plt.subplot(222)
    y_pos = np.arange(n_classes)
        
    plt.bar(y_pos,probas, align='center')
    plt.xlabel('Class')
    plt.ylabel('Softmax Probability')
    plt.title('Prediction: '+highest_class)
    plt.xlim([0,n_classes])
    
    plt.tight_layout()
    plt.show()
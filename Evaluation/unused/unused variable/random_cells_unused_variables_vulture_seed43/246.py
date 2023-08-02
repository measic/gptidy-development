def showPrecisionRecallPairByLabel(precision_by_label, recall_by_label, label_encoder, classifier_name, colors):
    labels = []
    for i in range(len(precision_by_label)):
        label = label_encoder.inverse_transform([i])[0]
        labels.append(label)
    
    y_pos = np.arange(len(labels))    

    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=False)

    ax1.invert_xaxis()
    ax1.yaxis.tick_right()
    
    ax1.set_yticks(y_pos)
    ax1.set_yticklabels(labels)
    
    ax2.set_yticks(y_pos)
    ax2.set_yticklabels(labels)
        
    ax1.barh(y_pos, precision_by_label, color=colors[0] , label="precision")
    ax2.barh(y_pos, recall_by_label,    color=colors[1],  label='recall')

    ax1.set_title('Precision( ' + classifier_name + ')')
    ax2.set_title('Recall (' + classifier_name + ')')
    
    plt.grid()
    plt.show()
    
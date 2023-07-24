fig = plt.figure(figsize=(15, 15))

gr = gridspec.GridSpec(1, 6)
for i in range(num_own_examples):
    probas = proba[i]
    highest_class = signnames[str(np.argmax(probas, axis =0))]
    plt.subplot(1,6,i+1)
    plt.imshow(X2[i])
    plt.axis('off')
    plt.text(0,1,highest_class,color='k',backgroundcolor='y')
fig.suptitle('In yellow: prediction made by the model', x=0.5,y=0.6, fontsize=20)
plt.tight_layout()
plt.show()    
 
fig = plt.figure(figsize=(15, 15))

for i in range(5):
    oi = np.random.randint(0,y_error_pred.shape[0])
    fig.add_subplot(1,5,i+1)
    plt.imshow(X_error_original[oi])
    #plt.imshow(X_error[oi].reshape(32,32), cmap = 'gray')
    plt.text(0,-5,signnames[str(y_error_true[oi])],color='w',backgroundcolor='g', fontsize=10, weight="bold") 
    plt.text(0,-2,signnames[str(y_error_pred[oi])],color='w',backgroundcolor='r', fontsize=10, weight="bold") 
    plt.axis('off')

fig.suptitle('Plotting examples where the model is wrong \n Green = actual class / Red = model prediction', x=0.5,y=0.7, fontsize=20)
plt.tight_layout()
plt.show() 
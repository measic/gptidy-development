save_file= './train_model_best.ckpt'
saver = tf.train.Saver()

with tf.Session() as session:
    saver.restore(session, save_file)
    weights_layer_1 = session.run(weights['layer_1'])

    # min/max values of weights
    wmin = np.min(weights_layer_1)
    wmax = np.max(weights_layer_1)

    fig, axes = plt.subplots(7,7)

    for i, ax in enumerate(axes.flat):
        if i < 48:
            image = weights_layer_1[:,:,0,i].reshape([3,3]) 
            ax.imshow(image, vmin=wmin, vmax=wmax, cmap='seismic')
            ax.axis('off')

    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
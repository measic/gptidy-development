for i in range(len(multiplier)):
    scale = multiplier[i]
    imageToTest = cv.resize(oriImg, (0, 0), fx=scale, fy=scale, interpolation=cv.INTER_CUBIC)
    imageToTest_padded, pad = padRightDownCorner(imageToTest, 8, 128)
    transposeImage = np.transpose(np.float32(imageToTest_padded[:, :, :]), (2, 0, 1)) / 256 - 0.5
    testimage = transposeImage
    cmodel = mx.mod.Module(symbol=sym, label_names=[])
    cmodel.bind(data_shapes=[('data', (1, 3, testimage.shape[1], testimage.shape[2]))])
    cmodel.init_params(arg_params=arg_params, aux_params=aux_params)
    variable_def = DataBatch(mx.nd.array([testimage[:, :, :]]), 0)
    cmodel.forward(variable_def)
    result = cmodel.get_outputs()
    heatmap = np.moveaxis(result[1].asnumpy()[0], 0, -1)
    heatmap = cv.resize(heatmap, (0, 0), fx=model['stride'], fy=model['stride'], interpolation=cv.INTER_CUBIC)
    heatmap = heatmap[:imageToTest_padded.shape[0] - pad[2], :imageToTest_padded.shape[1] - pad[3], :]
    heatmap = cv.resize(heatmap, (oriImg.shape[1], oriImg.shape[0]), interpolation=cv.INTER_CUBIC)
    heatmap_avg = heatmap_avg + heatmap / len(multiplier)
    f = plt.figure(i)
    plt.imshow(oriImg[:, :, [2, 1, 0]])
    ax2 = plt.imshow(heatmap[:, :, 18], alpha=0.5)
    f.show()
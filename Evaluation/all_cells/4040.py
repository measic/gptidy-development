for i in range(len(multiplier)):
    scale = multiplier[i]
    imageToTest = cv.resize(oriImg, (0,0), fx=scale, fy=scale, interpolation=cv.INTER_CUBIC)
    
    imageToTest_padded, pad = padRightDownCorner(imageToTest, 8, 128)
    
    transposeImage = np.transpose(np.float32(imageToTest_padded[:,:,:]), (2,0,1))/256 - 0.5
    #print transposeImage.shape
    testimage = transposeImage
    cmodel = mx.mod.Module(symbol=sym, label_names=[])
    cmodel.bind(data_shapes=[('data', (1,3,
                                   testimage.shape[1],testimage.shape[2]))])
    cmodel.init_params(arg_params=arg_params, aux_params=aux_params)
    onedata = DataBatch(mx.nd.array([testimage[:,:,:]]), 0)
    
    cmodel.forward(onedata)
    result=cmodel.get_outputs()
    
    paf = np.moveaxis(result[0].asnumpy()[0], 0, -1)
    paf = cv.resize(paf, (0,0), fx=model['stride'], fy=model['stride'], interpolation=cv.INTER_CUBIC)
    paf = paf[:imageToTest_padded.shape[0]-pad[2], :imageToTest_padded.shape[1]-pad[3], :]
    paf = cv.resize(paf, (oriImg.shape[1], oriImg.shape[0]), interpolation=cv.INTER_CUBIC)
    print paf.shape
        
    paf_avg = paf_avg + paf / len(multiplier)
    
    
    f = plt.figure(i)
    plt.imshow(oriImg[:,:,[2,1,0]])
    plt.imshow(paf[:,:,16], alpha=.5)
    f.show()
    print(paf.shape)
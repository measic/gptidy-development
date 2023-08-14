# get predictions
y_preds = predict_with_dropout_imgs(model_unet, data_test_overlap, batch_size=500, n_iter=20)
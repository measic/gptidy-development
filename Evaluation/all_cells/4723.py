# get all predictions in training and test set
# training set
y_pred_tr = model_unet.predict(data_train_overlap.im_patches, verbose=1)
y_pred_tr = remove_overlap(data_train.imgs, y_pred_tr, 64, 32)
y_pred_label_tr = get_y_pred_labels(y_pred_tr, background=True)

# validation set
y_pred_val = model_unet.predict(data_val_overlap.im_patches, verbose=1)
y_pred_val = remove_overlap(data_val.imgs, y_pred_val, 64, 32)
y_pred_label_val = get_y_pred_labels(y_pred_val, background=True)

# test set
y_pred_te = model_unet.predict(data_test_overlap.im_patches, batch_size=20, verbose=1)
y_pred_te = remove_overlap(data_test.imgs, y_pred_te, 64, 32)
y_pred_label_te = get_y_pred_labels(y_pred_te, background=True)
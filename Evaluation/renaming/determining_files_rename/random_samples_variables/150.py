act_train_all = get_activations_batch(model_unet, -2, data_train_overlap.im_patches, 20, verbose=True)
act_train_all = remove_overlap(data_train.imgs, act_train_all, patch_size=64, stride=32)
variable_def = act_train_all[pred_t_tr]
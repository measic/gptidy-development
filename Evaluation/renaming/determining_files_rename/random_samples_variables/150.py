variable_def = get_activations_batch(model_unet, -2, data_train_overlap.im_patches, 20, verbose=True)
variable_def = remove_overlap(data_train.imgs, variable_def, patch_size=64, stride=32)
act_train = variable_def[pred_t_tr]
# get activations
act_val_all = get_activations_batch(model_unet, -2, data_val_overlap.im_patches, 20, verbose=True)

# retain only activation weights for which there is a ground truth
act_val_all = remove_overlap(data_val.imgs, act_val_all, patch_size=64, stride=32)
act_val = act_val_all[pred_t_val]
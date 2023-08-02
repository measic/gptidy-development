# get indices of correctly / incorrectly predicted pixels
# with error in known classes
# only known classes (novely detection)
# get indices of correctly / incorrectly predicted pixels
# with error in known classes
# only known classes (novely detection)

pred_t_tr = (data_train.gt_patches != 0) & (data_train.gt_patches == y_pred_label_tr)
pred_f_tr = (data_train.gt_patches != 0) & (data_train.gt_patches != y_pred_label_tr)

pred_t_val = (data_val.gt_patches != 0) & (data_val.gt_patches == y_pred_label_val)
pred_f_val = (data_val.gt_patches != 0) & (data_val.gt_patches != y_pred_label_val)

pred_t_te = (data_test.gt_patches != 0) & (data_test.gt_patches == y_pred_label_te)
pred_f_te = (data_test.gt_patches != 0) & (data_test.gt_patches != y_pred_label_te)
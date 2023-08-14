chk_data = normed_test_data[normed_test_data['f9'] > 0]
#chk.index
chk_test = test_labels['focus'][chk_data.index] 
chk_pred = models['focus'].predict(chk_data).flatten()
chk_diff = chk_test - chk_pred
chk_diff.std()
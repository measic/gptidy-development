y_2, point_2 = predict_cluster(advi.approx, 1000, X, model, K, cov="cov_diagonal")
img_advi_2 = get_segment_img(y_2, img, point_2)
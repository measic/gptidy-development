y, point = predict_cluster(advi.approx, 1000, X, model, K, cov="cov_diagonal")
img_advi = get_segment_img(y,img, point)
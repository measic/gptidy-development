svm = grid_svm.best_estimator_
plot_validation_curve(svm,X_dev_np, y_dev_np, "C", [pow(10,x/2) for x in range(-12,0)],
                      "Curvas para SVM", "C")


plot_validation_curve(svm,X_dev_np, y_dev_np, "C", [pow(10,x/2) for x in range(-10,-4)],
                      "Curvas para SVM", "C")
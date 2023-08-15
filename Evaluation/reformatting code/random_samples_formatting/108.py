def show_results(label):
    loss, mae, mse = models[label].evaluate(normed_test_data, test_labels[label], verbose=0)

    print("Testing set Mean Abs Error: {:5.2f} um".format(mae))
    print("Testing set RMS: {:5.2f} um".format(np.sqrt(mse)))

    test_predictions = models[label].predict(normed_test_data).flatten()

    plt.scatter(test_labels[label], test_labels[label] - test_predictions)
    plt.xlabel('True Values [um]')
    plt.ylabel('Residuals [um]')
    minx, maxx = min(test_labels[label]), max(test_labels[label])
    plt.plot([minx, maxx], [0, 0])
    plt.show()
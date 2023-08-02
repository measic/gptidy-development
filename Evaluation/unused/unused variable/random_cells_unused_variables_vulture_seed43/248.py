fig = plt.figure()
for i in range(9):
    plt.subplot(3,3,i+1)
    plt.tight_layout()
    plt.imshow(example_data[i][0], cmap='gray', interpolation='none')
    plt.title("Prediction: {}/{}".format(le.inverse_transform(output.data.max(1, keepdim=True)[1][i])[0],
                                         le.inverse_transform(example_targets[i].view(-1, 1)[0])[0]))
    plt.xticks([])
    plt.yticks([])
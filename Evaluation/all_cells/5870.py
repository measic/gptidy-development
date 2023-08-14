for pred, img in zip(result[1], test_images):
    plt.imshow(img)
    plt.show()
    for i in pred:
        print(sign_name[i])
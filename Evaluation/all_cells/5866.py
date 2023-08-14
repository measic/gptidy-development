for idx, img in zip(result, test_images):
    print(idx, sign_name[idx])
    plt.imshow(img)
    plt.show()
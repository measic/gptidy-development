X_train, y_train = shuffle(X_train_augmented, y_train_augmented)

def get_random_img(X_data, y_label):
    index = random.randint(0, len(X_data))
    image = X_data[index].squeeze()
    return (image, y_label[index], index)

def plot_imgs(X_data, y_label):
    f, axarr = plt.subplots(3, 3, figsize=(16, 16))
    variable_def = []
    for i in range(9):
        image, label, index = get_random_img(X_data, y_label)
        variable_def.append(index)
        label_str = str(label)
        axarr[i // 3, i % 3].imshow(image, cmap='gray')
        axarr[i // 3, i % 3].set_title(label_str + ': ' + sign_dict[label_str])
        plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
        plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
    return variable_def
rand_img_indices = plot_imgs(X_train, y_train)
print(rand_img_indices)
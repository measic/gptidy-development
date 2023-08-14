### plot some figures we got wrong

fig = plt.figure(figsize=(20, 12))

for i, ix in enumerate(np.random.choice(test_tensors.shape[0], size=24, replace=False)):
    ax = fig.add_subplot(4, 6, i+1, xticks=[], yticks=[])
    ax.imshow(np.squeeze(test_tensors[ix]))
    # correct img ix
    true_index = np.argmax(test_targets[ix])
    # predicted img ix
    pred_index = predictions[ix]
    ax.set_title('{}\n[{}]'.format(dog_names[pred_index], dog_names[true_index]),
                color=('blue' if pred_index == true_index else 'red'))
plt.tight_layout()
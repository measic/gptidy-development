arr = np.reshape(z2_layers[..., 5], (1000, 1000))
fig = plt.figure(figsize=(14, 8))

ax = plt.subplot(111)
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()
# plt.savefig(os.path.join(msig.out_dir, 'gen_loss_acc.png'))
# plt.show()
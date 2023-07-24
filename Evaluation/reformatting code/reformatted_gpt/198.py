# GANDeconv_t9900_h100_train3_ep48.critic5
# GANDeconv_t9900_h100_train3_ep45
# GANDeconv_t9900_h100_train3_ep21
# GANDeconv_t9900_h100_train3_ep45
filename = 'GANDeconv_t9900_h100_train3_ep45'  # 'GANDeconvolution_t2000_h100_ep20.c5'
hidden_dim = 100
G, D, train_hist = GAN_CelebA.loadCheckpoint(filename, hidden_dim, use_cuda=use_cuda)
epoch_num = len(train_hist['D_losses'])
GAN_CelebA.show_result(G, D, epoch_num, hidden_dim, show=True, save=True, path='figures/' + filename + '.pdf', use_cuda=use_cuda)

plt.plot(range(0, epoch_num), train_hist['D_losses'], label='D_loss')
plt.plot(range(0, epoch_num), train_hist['G_losses'], label='G_loss')
# plt.plot(range(0, epoch_num), train_hist['Inc_score'], linestyle='--', label='Inc_score')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Deconvolution GAN, total time:' + str(int(train_hist['total_ptime'][-1] / 60)) + 'minutes')
plt.legend()
plt.savefig('figures/' + filename + '_Loss.pdf')
plt.show()

# test_z = torch.randn(10000, 100, 1, 1)
# inception_score(test_z, G, D, batch_size=128, cuda=use_cuda, resize=False, splits=10)
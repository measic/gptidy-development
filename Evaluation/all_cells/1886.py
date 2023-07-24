# Dynamic critic of grandiant descent between Distriminator and Generator.
filename='GANDeconv_t9999_h100_train2_ep36'
hidden_dim = 100

G,D,train_hist = GAN_CelebA.loadCheckpoint(filename,hidden_dim,use_cuda=use_cuda)
epoch_num=len(train_hist['D_losses'])
GAN_CelebA.show_result(G,D,epoch_num, hidden_dim, show=True,save=True, path='figures/'+filename+'.pdf', use_cuda=use_cuda)

plt.plot(range(0,epoch_num),train_hist['D_losses'],label='D_loss')
plt.plot(range(0,epoch_num),train_hist['G_losses'],label='G_loss')
# plt.plot(range(0,epoch_num),train_hist['Inc_score'],linestyle='--',label='Inc_score')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('DCGAN dynamic, total time:'+str(int(train_hist['total_ptime'][-1]/60))+'minutes')
plt.legend()
plt.savefig('figures/'+filename+'_Loss.pdf')
plt.show()
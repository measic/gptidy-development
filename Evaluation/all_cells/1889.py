#GAN_W_fixlr_t10000_h200_trainw_ep48
#GAN_W_fixlr_t10000_h200_b64_c5_ep48
filename='GAN_W_fixlr_t10000_h200_b64_c5_ep50' #'GANDeconvolution_t2000_h100_ep20.c5'
hidden_dim=200
G,D,train_hist = GAN_CelebA.loadCheckpoint(filename,hidden_dim,use_cuda=use_cuda)
epoch_num=len(train_hist['D_losses'])
GAN_CelebA.show_result(G,D,epoch_num, hidden_dim, show=True,save=True, path='figures/'+filename+'.pdf', use_cuda=use_cuda)

plt.plot(range(0,epoch_num),train_hist['D_losses'],label='Wasserstein distance')
plt.plot(range(0,epoch_num),train_hist['G_losses'],label='G_loss')
#plt.plot(range(0,epoch_num),train_hist['Inc_score'],linestyle='--',label='Inc_score')
plt.xlabel('Epochs')
plt.ylabel('Wasserstein distance')
plt.title('Wasserstein GAN h=200, total time:'+str(int(train_hist['total_ptime'][-1]/60))+'minutes')
plt.legend()
plt.savefig('figures/'+filename+'_Loss.pdf')
plt.show()

#GAN_W_fixlr_t10000_h100_trainw_ep48
#GAN_W_fixlr_t10000_h100_b64_c5_ep48
filename = 'GAN_W_fixlr_t10000_h100_b64_c5_ep50' #'GAN_W_t1000_h100_trainw_ep9'
hidden_dim = 100
G,D,train_hist = GAN_CelebA.loadCheckpoint_W(filename,hidden_dim,use_cuda=use_cuda)
epoch_num=len(train_hist['D_losses'])
GAN_CelebA.show_result(G,D,epoch_num, hidden_dim, show=True,save=True, path='figures/'+filename+'.pdf', use_cuda=use_cuda)

plt.plot(range(0,epoch_num),train_hist['D_losses'],label='Wasserstein distance')
plt.plot(range(0,epoch_num),train_hist['G_losses'],label='G_loss')
#plt.plot(range(0,epoch_num),train_hist['Inc_score'],linestyle='--',label='Inc_score')
plt.xlabel('Epochs')
plt.ylabel('Wasserstein Distance')
plt.title('Wasserstein GAN, total time:'+str(int(train_hist['total_ptime'][-1]/60))+'minutes')
plt.legend()
plt.savefig('figures/'+filename+'_Loss.pdf')
plt.show()
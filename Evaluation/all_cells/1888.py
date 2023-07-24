#'GANBilinear_t9900_h100_train3_ep6.critic5'
#'GANBilinear_t4000_h100_ep30.c4'
#GANbilinear_t10000_h100_ep50_new
#'GANBilinear_t9000_h100_train3_ep18'
filename = 'GANBilinear_t9900_h100_train3_ep33'
hidden_dim = 100
G,D,train_hist = GAN_CelebA.loadCheckpoint_Upsampling_old(filename,hidden_dim,use_cuda=use_cuda,mode='bilinear')
epoch_num=len(train_hist['D_losses'])
GAN_CelebA.show_result(G,D,epoch_num, hidden_dim, show=True,save=True, path='figures/'+filename+'.pdf', use_cuda=use_cuda)

plt.plot(range(0,epoch_num),train_hist['D_losses'],label='D_loss')
plt.plot(range(0,epoch_num),train_hist['G_losses'],label='G_loss')
# plt.plot(range(0,epoch_num),train_hist['Inc_score'],linestyle='--',label='Inc_score')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('DCGAN Bilinear, total time:'+str(int(train_hist['total_ptime'][-1]/60))+'minutes')
plt.legend()
plt.savefig('figures/'+filename+'_Loss.pdf')
plt.show()
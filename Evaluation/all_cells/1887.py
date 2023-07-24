#GANnearest_t9900_h100_train3_ep9
#GANnearest_t10000_h100_ep50_new
filename='GANnearest_t10000_h100_ep50_new' #'GANnearest_t4000_h100_ep30.c1' #'GANnearest_t10000_h100_train2_ep3' #GANnearest_t4000_h100_ep30.c1
hidden_dim = 100

G,D,train_hist = GAN_CelebA.loadCheckpoint_Upsampling(filename,hidden_dim,use_cuda=use_cuda,mode='nearest')
epoch_num=len(train_hist['D_losses'])
GAN_CelebA.show_result(G,D,epoch_num, hidden_dim, show=True,save=True, path='figures/'+filename+'.pdf', use_cuda=use_cuda)

plt.plot(range(0,epoch_num),train_hist['D_losses'],label='D_loss')
plt.plot(range(0,epoch_num),train_hist['G_losses'],label='G_loss')
# plt.plot(range(0,epoch_num),train_hist['Inc_score'],linestyle='--',label='Inc_score')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('DCGAN Nearest, total time:'+str(int(train_hist['total_ptime'][-1]/60))+'minutes')
plt.legend()
plt.savefig('figures/'+filename+'_Loss.pdf')
plt.show()
importlib.reload(GAN_CelebA)

x_0 = dataset[3][0]
x_1 = dataset[6][0]

# GAN_W_fixlr_t10000_h100_b64_c5_ep50
#GAN_W_fixlr_t10000_h100_trainw_ep42 #3
filename = 'GAN_W_fixlr_t10000_h100_b64_c5_ep50' #'GAN_W_t1000_h100_trainw_ep9'
hidden_dim = 100
G,D,train_hist = GAN_CelebA.loadCheckpoint_W(filename,hidden_dim,use_cuda=use_cuda)
GAN_CelebA.compareRandomPoint(x_0,x_1,G,23, hidden_dim, show = True, save = True, \
            path = 'figures/compare2point_wgan.pdf',use_cuda=use_cuda,label='model WGAN with hiden='+str(hidden_dim))

filename='GANDeconv_t9900_h100_train3_ep45'
hidden_dim = 100
G,D,train_hist = GAN_CelebA.loadCheckpoint(filename,hidden_dim,use_cuda=use_cuda)
GAN_CelebA.compareRandomPoint(x_0,x_1,G,5, hidden_dim, show = True, save = True, \
            path = 'figures/compare2point_dcgan.pdf',use_cuda=use_cuda,label='model DCGAN with hiden='+str(hidden_dim))

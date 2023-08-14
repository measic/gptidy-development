# from bishop import thetas
thetas = np.array([(1., 4., 0., 0.), 
                   (9., 4., 0., 0.), 
                   (1., 64., 0., 0.), 
                   (1., 0.25, 0., 0.), 
                   (1., 4., 10., 0.), 
                   (1., 4., 0., 5.)])

n_samples = 5 # number of functions we sample per plot.
N_test = 100
x_test = np.linspace(-1, 1, N_test) 

for idx, theta in enumerate(thetas):
    K = computeK(x_test,x_test,theta)
    plt.subplot(2, 3, idx+1).title.set_text(str(theta))
    
    for i in range(n_samples):
        plt.plot(x_test,np.random.multivariate_normal(np.zeros(len(K)),K))
    
    variance = K.diagonal()
    plt.fill_between(x_test, -2*np.sqrt(variance), 2*np.sqrt(variance), color='r', alpha=0.1 )
    plt.plot(x_test, np.zeros(len(x_test)), '--')

plt.suptitle("Function Samples from GP")
plt.show()
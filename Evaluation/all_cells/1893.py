
filename = 'GAN_model_scores'
checkpoint = torch.load('./checkpoint/'+filename)
inception_scores_u = checkpoint['inception_scores_u']
inception_scores_s = checkpoint['inception_scores_s']
w_distances = checkpoint['w_distances']
model_num=len(inception_scores['group1'])
model_files=checkpoint['model_files']

bad=[]
for i in range(model_num):
    if i< model_num/2:
        bad.append(inception_scores_u['group4'][0])
    else:
        bad.append(inception_scores_u['group4'][-1])

plt.plot(range(1,model_num+1),inception_scores_u['group1'],label='Best models')
plt.plot(range(1,model_num+1),inception_scores_u['group2'],label='Middle models')
plt.plot(range(1,model_num+1),inception_scores_u['group3'],linestyle='--',label='Worse models')
plt.plot(range(1,model_num+1),bad,linestyle='--',label='Bad models')
plt.xlabel('Models')
plt.ylabel('Mean values')
plt.title('Inception scores')
plt.legend()
plt.savefig('figures/'+filename+'_Inception_u.pdf')
plt.show()

bad=[]
for i in range(model_num):
    if i< model_num/2:
        bad.append(inception_scores_s['group4'][0])
    else:
        bad.append(inception_scores_s['group4'][-1])

plt.plot(range(1,model_num+1),inception_scores_s['group1'],label='Best models')
plt.plot(range(1,model_num+1),inception_scores_s['group2'],label='Middle models')
plt.plot(range(1,model_num+1),inception_scores_s['group3'],linestyle='--',label='Worse models')
plt.plot(range(1,model_num+1),bad,linestyle='--',label='Bad models')
plt.xlabel('Models')
plt.ylabel('Sigma values')
plt.title('Inception scores')
plt.legend()
plt.savefig('figures/'+filename+'_Inception_s.pdf')
plt.show()

bad=[]
for i in range(model_num):
    if i< model_num/2:
        bad.append(w_distances['group4'][0])
    else:
        bad.append(w_distances['group4'][-1])

plt.plot(range(1,model_num+1),w_distances['group1'],label='Best models')
plt.plot(range(1,model_num+1),w_distances['group2'],label='Middle models')
plt.plot(range(1,model_num+1),w_distances['group3'],linestyle='--',label='Worse models')
plt.plot(range(1,model_num+1),bad,linestyle='--',label='Bad models')
plt.xlabel('Models')
plt.ylabel('Wasserstein distance')
plt.title('Wasserstein distance')
plt.legend()
plt.savefig('figures/'+filename+'_Wasserstein_distance.pdf')
plt.show()

# print scores 
s=inception_scores_s['group1']+inception_scores_s['group2']+inception_scores_s['group3']+inception_scores_s['group4']
u=inception_scores_u['group1']+inception_scores_u['group2']+inception_scores_u['group3']+inception_scores_u['group4']
w=w_distances['group1']+w_distances['group2']+w_distances['group3']+w_distances['group4']
print('Mean\tSigma\twDistance\tModel name')
for n,u,s,w in zip(model_files,u,s,w):
    print('%.3f\t%.3f\t%.3f\t%s' % (u,s,w,n.strip()))
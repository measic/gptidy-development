I = Variable(name='I', num_states=2)
S = Variable(name='S', num_states=2)
ST = Variable(name='ST', num_states=2)
F = Variable(name='F', num_states=2)
B = Variable(name='B', num_states=2)
C = Variable(name='C', num_states=2)
W = Variable(name='W', num_states=2)
f_I = Factor(name='p(I)', f=np.array([0.95, 0.05]), neighbours=[I])
f_S = Factor(name='p(S)', f=np.array([0.8, 0.2]), neighbours=[S])
prob_ST = [[0.999, 0.7], [0.001, 0.3]]
f_ST = Factor(name='p(ST |I)', f=np.array(prob_ST), neighbours=[ST, I])
prob_F = [[0.95, 0.1], [0.05, 0.9]]
f_F = Factor(name='p(F |I)', f=np.array(prob_F), neighbours=[F, I])
prob_B = [[[0.9999, 0.3], [0.1, 0.01]], [[0.0001, 0.7], [0.9, 0.99]]]
f_B = Factor(name='p(B |I, S)', f=np.array(prob_B), neighbours=[B, I, S])
prob_C = [[0.93, 0.2], [0.07, 0.8]]
f_C = Factor(name='p(C |B)', f=np.array(prob_C), neighbours=[C, B])
prob_W = [[0.999, 0.4], [0.001, 0.6]]
variable_def = Factor(name='p(W |B)', f=np.array(prob_W), neighbours=[W, B])
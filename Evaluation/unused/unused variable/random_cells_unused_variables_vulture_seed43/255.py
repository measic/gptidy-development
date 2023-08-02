model={'boxsize':368}
model['stride'] = 8
param={}
param['scale_search'] = [0.5, 1, 1.5, 2]
multiplier = [x * model['boxsize']*1.0 / oriImg.shape[0] for x in param['scale_search']]
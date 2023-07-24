# 1.1.2 Compute gradient of log p(t|x;w,b) wrt w and b
# for numerical stability : https://docs.scipy.org/doc/scipy-0.19.0/reference/generated/scipy.misc.logsumexp.html
from scipy.special import logsumexp 
import numpy as np

def one_hot(a, num_classes):
    return np.eye(num_classes)[a.reshape(-1)]

def logprob(x, w, b):
    ln_q = np.matmul(x, w) + b     
    ln_Z = logsumexp(ln_q)     
   
    ln_p = ln_q - ln_Z
    return ln_q, ln_Z, ln_p   

def logreg_gradient(x, t, w, b):
    num_classes = len(b)
    
    ln_q, ln_Z, ln_p = logprob(x, w, b)
    t_oh = one_hot(t, num_classes)
    
    delta = t_oh - np.exp(ln_q)/np.exp(ln_Z)   #
    
    dL_db = delta
    dL_dw = np.matmul(x.T, delta)
    logp = ln_p
    
    # here the statement contains logp[:,t] where logp is meant as a matrix of shape 1x10
    return logp[:,t].squeeze(), dL_dw, dL_db.squeeze()

from scipy.special import logsumexp
from scipy.special import expit
import numpy as np

def one_hot(a, num_classes):
    return np.eye(num_classes)[a.reshape(-1)]

def mlp_logprob(x, W, b, V, a):
    h = expit(np.matmul(x, V) + a)
    ln_q = np.matmul(h, W) + b
    ln_Z = logsumexp(ln_q)
    ln_p = ln_q - ln_Z
    return (ln_p, ln_q, ln_Z, h)

def mlp_gradient(x, t, W, b, V, a):
    num_classes = len(b)
    ln_p, ln_q, ln_Z, h = mlp_logprob(x, W, b, V, a)
    t_oh = one_hot(t, num_classes)
    delta_q = t_oh - np.exp(ln_q) / np.exp(ln_Z)
    delta_h = np.matmul(delta_q, W.T)
    dL_db = delta_q
    dL_dW = np.matmul(h.T, delta_q)
    dL_da = delta_h * h * (1 - h)
    dL_dV = np.matmul(x.T, dL_da)
    return (ln_p[:, t].squeeze(), dL_dW, dL_db.squeeze(), dL_dV, dL_da.squeeze())

def init_params(input_size, num_classes, hidden_units):
    W = np.random.normal(size=(hidden_units, num_classes), scale=0.1)
    b = np.zeros(num_classes)
    V = np.random.normal(size=(input_size, hidden_units), scale=0.1)
    a = np.zeros(hidden_units)
    return (W, b, V, a)

def mlp_sgd_iter(x_train, t_train, W, b, V, a, lr):
    indices = np.arange(len(x_train))
    np.random.shuffle(indices)
    logp = np.zeros(len(x_train))
    for i in indices:
        x = x_train[i:i + 1]
        t = t_train[i]
        logp[i], grad_W, grad_b, grad_V, grad_a = mlp_gradient(x, t, W, b, V, a)
        W = W + lr * grad_W
        b = b + lr * grad_b
        V = V + lr * grad_V
        a = a + lr * grad_a
    logp_train = logp.mean()
    return (logp_train, W, b, V, a)

def function_def(xs, ts, W, b, V, a):
    logps = []
    for x, t in zip(xs, ts):
        logp, _, _, _ = mlp_logprob(x, W, b, V, a)
        logps.append(logp[t].squeeze())
    return mean(logps)
from scipy.optimize import check_grad
np.random.seed(123)
W = np.random.normal(size=(20, 10), scale=0.001)
b = np.zeros((10,))
V = np.random.normal(size=(28 * 28, 20), scale=0.001)
a = np.zeros(20)

def func(w):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], w.reshape(20, 10), b, V, a)
    return logpt

def grad(w):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], w.reshape(20, 10), b, V, a)
    return grad_W.flatten()
finite_diff_error = check_grad(func, grad, W.flatten())
print('Finite difference error grad_W:', finite_diff_error)
assert finite_diff_error < 0.001, 'Your gradient computation for W seems off'

def func(b):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], W, b, V, a)
    return logpt

def grad(b):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], W, b, V, a)
    return grad_b.flatten()
finite_diff_error = check_grad(func, grad, b)
print('Finite difference error grad_b:', finite_diff_error)
assert finite_diff_error < 0.001, 'Your gradient computation for b seems off'

def func(v):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], W, b, v.reshape(28 * 28, 20), a)
    return logpt

def grad(v):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], W, b, v.reshape(28 * 28, 20), a)
    return grad_V.flatten()
finite_diff_error = check_grad(func, grad, V.flatten())
print('Finite difference error grad_V:', finite_diff_error)
assert finite_diff_error < 0.001, 'Your gradient computation for V seems off'

def func(a):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], W, b, V, a)
    return logpt

def grad(a):
    logpt, grad_W, grad_b, grad_V, grad_a = mlp_gradient(x_train[0:1, :], t_train[0:1], W, b, V, a)
    return grad_a.flatten()
finite_diff_error = check_grad(func, grad, a.flatten())
print('Finite difference error grad_a:', finite_diff_error)
assert finite_diff_error < 0.001, 'Your gradient computation for a seems off'
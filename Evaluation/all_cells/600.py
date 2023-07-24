import sympy as sp
import numpy as np
from scipy.sparse import spdiags
import matplotlib.pyplot as plt
from scipy.sparse.linalg import spsolve

x = sp.Symbol('x') # global variable


# N discrete points of [a, b]
a, b, N = -5.0, 5.0, 10; 

# Compute the source based on a given exact solution
x = sp.Symbol('x')
ue = sp.sin(x)+ sp.cos(x)

f = -sp.diff(ue, x, 2);
lam_ue = sp.lambdify(x, ue, modules=['numpy'])
      
xd, u_fem = FEM(f, a, b, N, lam_ue)  

xd, u_fdm = FDM(f, a, b, N, lam_ue)  

xe = np.linspace(a, b, 100)
ue_fine = lam_ue(xe)

plt.plot(xe, ue_fine,'-',xd, u_fem,'--o',xd, u_fdm,'-.s')
plt.gca().legend(('Exact','FEM','FDM'))
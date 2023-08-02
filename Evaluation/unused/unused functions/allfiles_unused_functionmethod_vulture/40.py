def FEM(f, a, b, N, u_bc):
# Solving -u''=f in (a, b) by Linear Finite Element Method
# Dirichlet boundary conditions at two ending points
# Van-Dang Nguyen 2019  
  
  xd= np.linspace(a, b, num=N)
  # A = sps.coo_matrix((N, N)) # empty matrix
  # rhs = sps.coo_matrix((N, 1)) # empty matrix
  A = np.zeros( (N, N) )
  rhs = [0]*N;
  for ele in range(0, N-1):
    node0, node1 = ele, ele+1;
    x0, x1 = xd[node0], xd[node1]
    phi = basis_func(x0, x1)
    dphi = diff_basis_func(x0, x1)
    b0 = sp.integrate(phi[0]*f, (x, x0, x1))
    b1 = sp.integrate(phi[1]*f, (x, x0, x1))
        
    A00 = sp.integrate(dphi[0]*dphi[0], (x, x0, x1))
    A01 = sp.integrate(dphi[0]*dphi[1], (x, x0, x1))
    A10 = sp.integrate(dphi[1]*dphi[0], (x, x0, x1))
    A11 = sp.integrate(dphi[1]*dphi[1], (x, x0, x1))
    
    A[node0, node0] += A00
    A[node0, node1] += A01
    A[node1, node0] += A10
    A[node1, node1] += A11

    
    rhs[node0] += float(b0);
    rhs[node1] += float(b1);

  # Boundary conditions for the left-hand side 
  A[0,:] = 0; # zero out row 0 corresponding to x=a.
  A[0,0]=1
  A[N-1,:]=0; # zero out row N-1 corresponding to x=b.
  A[N-1,N-1]=1
 
  # Boundary conditions for the right-hand side  
  rhs[0], rhs[N-1]=float(u_bc(xd[0])), float(u_bc(xd[N-1])) # Dirichlet values

  ## solving the linear system
  u= spsolve(A, rhs, permc_spec=None, use_umfpack=True)
  return xd, u

def basis_func(x0, x1):
  L = x1 - x0
  phi = [0] * 2
  phi[0] = -(x-x1)/L
  phi[1] = (x-x0)/L  
  return phi

def diff_basis_func(x0, x1):
  L = x1 - x0
  dphi = [0] * 2
  dphi[0] = -1./L
  dphi[1] = 1./L  
  return dphi
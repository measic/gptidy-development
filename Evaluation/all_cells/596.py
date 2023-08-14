def FDM(f, a, b, N, u_bc):
# Solving -u''=f in (a, b) by Finite Difference Method 
# Dirichlet boundary conditions at two ending points
# Van-Dang Nguyen 2019  
  xd= np.linspace(a, b, num=N)
  # Grid size
  h=xd[1]-xd[0]
  ones=np.ones(N)

  # Create left-hand side digonal matrix [1 -2 1]
  data = -1/(h*h)*np.array([ones,-2*ones,ones])
  diags = np.array([-1, 0, 1])
  A=spdiags(data, diags, N, N,format="csr").toarray()
   
  # Boundary conditions for the left-hand side 
  A[0,:] = 0; # zero out row 0 corresponding to x=a.
  A[0,0]=1
  A[N-1,:]=0; # zero out row N-1 corresponding to x=b.
  A[N-1,N-1]=1
  
  # Boundary conditions for the right-hand side  
  lam_f = sp.lambdify(x, f, modules=['numpy'])
  rhs = lam_f(xd); # rhs = source 
  rhs[0], rhs[N-1]=u_bc(xd[0]), u_bc(xd[N-1]) # Dirichlet values
  
  ## solving the linear system
  u= spsolve(A, rhs, permc_spec=None, use_umfpack=True)
  return xd, u
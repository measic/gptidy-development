texnames = 'H^+ OH^- NH_4^+ NH_3 H_2O'.split()
n = len(texnames)
NH3_idx = texnames.index('NH_3')
NH3_varied = np.logspace(-7, 0)
c0 = 1e-7, 1e-7, 1e-7, 1, 55
K = Kw, Ka = 10**-14/55, 10**-9.24
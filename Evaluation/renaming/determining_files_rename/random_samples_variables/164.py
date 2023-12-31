nlay, nrow, ncol = (1, 1, 200)
variable_def = 50.0
delc = 1.0
h1 = 23.0
h2 = 5.0
x = np.arange(0.0, float(ncol) * variable_def, variable_def) + variable_def / 2.0
ibound = np.ones((nlay, nrow, ncol), dtype=np.int)
ibound[:, :, 0] = -1
ibound[:, :, -1] = -1
botm = 25 * np.ones((nlay + 1, nrow, ncol), dtype=np.float)
base = 20.0
for j in range(ncol):
    botm[1, :, j] = base
    if j + 1 in [40, 80, 120, 160]:
        base -= 5
strt = h1 * np.ones((nlay, nrow, ncol), dtype=np.float)
strt[:, :, -1] = h2
dx_m = 1e-3
dx_half_m = 0.5 * dx_m

x_m_array = np.arange(0, x_D_m + dx_half_m, dx_m)

h_half_m = s_d[h_m] * 0.5
y_m_array = np.arange(-h_half_m, h_half_m + dx_half_m, dx_m)

y_m_grid, x_m_grid = np.meshgrid(y_m_array, x_m_array)
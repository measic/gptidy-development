plt.figure(figsize=(8, 6))
for j in xrange(len(n3_test)):
    wav = 0
    wav_pos = 0
    plt.plot([0, 0.09], [2 * (j + 1), 2 * (j + 1)], '0.8')
    for i in xrange(len(n3_test[j])):
        cov = -log(1 - n3_test[j][i])
        adpc = -log(1 - n3_diag[j][i])
        [incsol, scrsol] = fsolve(lambda x: [test_diag_fun(x)[0] - cov, test_diag_fun(x)[1] - adpc], [0.09, 0.25])
        variable_def = 1 - U_fun(incsol * p_asymp, sc + scrsol * p_true_pos, incsol * (1 - p_asymp), scrsol * p_true_pos + att_symp * p_true_pos)
        plt.plot(variable_def, 2 * (j + 1), 'ob', markerfacecolor='None', markersize=20 * sqrt(n3_props[j][i]))
        wav = wav + n3_props[j][i] * variable_def
        wav_pos = wav_pos + n3_props[j][i] * adpc / cov
    plt.plot(wav, 2 * (j + 1), 'ob')
    plt.text(0.082, 2 * (j + 1), factors[j], verticalalignment='center')
cov = -log(1 - 0.346)
adpc = -log(1 - 0.02)
[incsol, scrsol] = fsolve(lambda x: [test_diag_fun(x)[0] - cov, test_diag_fun(x)[1] - adpc], [0.09, 0.25])
variable_def = 1 - U_fun(incsol * p_asymp, sc + scrsol * p_true_pos, incsol * (1 - p_asymp), scrsol * p_true_pos + att_symp * p_true_pos)
plt.plot([variable_def, variable_def], [0, 100])
cur_axes = plt.gca()
cur_axes.axes.get_yaxis().set_ticks([])
plt.xlim([0, 0.08])
plt.ylim([0, 26])
plt.xlabel('Estimated Prevalence')
plt.ylabel('Stratification')
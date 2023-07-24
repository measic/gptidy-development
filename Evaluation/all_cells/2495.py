%matplotlib inline
def solve_and_plot(nsys):
    fig = plt.figure(figsize=(12, 4))
    ax_out = plt.subplot(1, 2, 1, xscale='log', yscale='log')
    ax_err = plt.subplot(1, 2, 2, xscale='log')
    ax_err.set_yscale('symlog', linthreshy=1e-14)
    xres, extra = nsys.solve_and_plot_series(
        c0, c0+K, NH3_varied, NH3_idx, 'scipy', 
        plot_kwargs=dict(ax=ax_out), plot_residuals_kwargs=dict(ax=ax_err))
    for ax in (ax_out, ax_err):
        ax.set_xlabel('[NH3]0 / M')
    ax_out.set_ylabel('Concentration / M')
    ax_out.legend(loc='best')
    ax_err.set_ylabel('Residuals')
    
    avg_nfev = np.average([nfo['nfev'] for nfo in extra['info']])
    avg_njev = np.average([nfo['njev'] for nfo in extra['info']])
    success = np.average([int(nfo['success']) for nfo in extra['info']])
    return {'avg_nfev': avg_nfev, 'avg_njev': avg_njev, 'success': success}

    
solve_and_plot(neqsys)
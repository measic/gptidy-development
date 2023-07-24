splot.plot(
    (sigma_AB_Pa.subs(s_d), (x, 0, x_B_m)),
    (sigma_BD_Pa.subs(s_d), (x, x_B_m, x_D_m)),
    xlabel='x(m)', ylabel='$\\sigma$(Pa)'
)
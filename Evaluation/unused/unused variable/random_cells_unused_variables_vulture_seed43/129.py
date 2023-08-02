M_Nm = sy.Piecewise((M_AB_Nm.subs(s_d), x<=x_B_m),
                    (M_BD_Nm.subs(s_d), x_B_m<x))
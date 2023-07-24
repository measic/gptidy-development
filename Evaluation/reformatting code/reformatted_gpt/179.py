%matplotlib inline
from numpy import *
import matplotlib.pyplot as plt

inc = linspace(0, 0.5, 101)  # incidence
scr = linspace(0, 0.5, 101)  # screening
inc, scr = meshgrid(inc, scr)

# proportion of population in each compartment
ZU = U_fun(inc * p_asymp, sc + scr * p_true_pos, inc * (1 - p_asymp), scr * p_true_pos + att_symp * p_true_pos)
ZA = A_fun(inc * p_asymp, sc + scr * p_true_pos, inc * (1 - p_asymp), scr * p_true_pos + att_symp * p_true_pos)
ZS = S_fun(inc * p_asymp, sc + scr * p_true_pos, inc * (1 - p_asymp), scr * p_true_pos + att_symp * p_true_pos)

Zprev = 1 - ZU
Ztest = scr + ZS * att_symp
Zdiag = (ZA + ZS) * scr * p_true_pos + ZU * scr * p_false_pos + ZS * att_symp * p_true_pos
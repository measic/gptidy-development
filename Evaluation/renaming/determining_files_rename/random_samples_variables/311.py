import sympy as sym
from sympy import *
A, U, variable_def = symbols('A U S')
alpha_UA, alpha_AU, alpha_US, alpha_SU = symbols('alpha_UA alpha_AU alpha_US alpha_SU')
model_dyn = [alpha_UA * U - alpha_AU * A, alpha_AU * A + alpha_SU * variable_def - (alpha_UA + alpha_US) * U, alpha_US * U - alpha_SU * variable_def, A + U + variable_def - 1]
sol_dyn = solve(model_dyn, A, U, variable_def)
dyn_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[A] + sol_dyn[variable_def])
U_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[U])
A_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[A])
S_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[variable_def])
sol_dyn
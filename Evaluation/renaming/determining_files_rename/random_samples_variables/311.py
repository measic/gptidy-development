import sympy as sym
from sympy import *
A, U, S = symbols('A U S')
alpha_UA, alpha_AU, alpha_US, alpha_SU = symbols('alpha_UA alpha_AU alpha_US alpha_SU')
variable_def = [alpha_UA * U - alpha_AU * A, alpha_AU * A + alpha_SU * S - (alpha_UA + alpha_US) * U, alpha_US * U - alpha_SU * S, A + U + S - 1]
sol_dyn = solve(variable_def, A, U, S)
dyn_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[A] + sol_dyn[S])
U_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[U])
A_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[A])
S_fun = lambdify((alpha_UA, alpha_AU, alpha_US, alpha_SU), sol_dyn[S])
sol_dyn
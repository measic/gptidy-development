from scipy.optimize import fsolve
tsym, dsym, ssym, test_sym = symbols('tsym dsym ssym test_sym')
model_test_diag = [tsym - (ssym + (1 - A - U) * test_sym), dsym - (A * ssym * p_true_pos + U * ssym * p_false_pos + (1 - A - U) * test_sym * p_true_pos)]
sol_test_diag = solve(model_test_diag, tsym, dsym)
test_fun = lambdify((A, U, ssym, test_sym), sol_test_diag[tsym])
diag_fun = lambdify((A, U, ssym, test_sym), sol_test_diag[dsym])

def test_diag_fun(parms):
    inc = parms[0]
    scr = parms[1]
    A = A_fun(inc * p_asymp, sc + scr * p_true_pos, inc * (1 - p_asymp), scr * p_true_pos + att_symp * p_true_pos)
    U = U_fun(inc * p_asymp, sc + scr * p_true_pos, inc * (1 - p_asymp), scr * p_true_pos + att_symp * p_true_pos)
    return [test_fun(A, U, scr, att_symp), diag_fun(A, U, scr, att_symp)]
from scipy.integrate import odeint

def function_def(y, t, parms):
    return [parms[1] * y[1] + parms[3] * y[2] - (parms[0] + parms[2]) * y[0], parms[0] * y[0] - parms[1] * y[1], parms[2] * y[0] - parms[3] * y[2]]
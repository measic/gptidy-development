from IPython.display import display
from IPython.display import HTML
from ipywidgets import interact
import ipywidgets as widgets

def get_cuota_mensual_total(p, i, n):
    num = p * i * (i+1)**n
    den = (i+1)**n - 1
    return num/den

def get_deuda_capital(p, i, n, t):
    coef = (((1+i)**t) - 1) / (((1+i)**n) - 1)
    return p * ( 1 - coef )

def mostrar_evolucion_credito(P, I, N):
    
    p = P
    i = I / 12.0 * 0.01
    n = N * 12
    
    cuota_total = get_cuota_mensual_total(p, i, n)
    print("Tu cuota mensual es de AR$ " + str(cuota_total) + "\n")

    cuota_capital = []
    cuota_interes = []
    deuda_capital = []
    t_array = []
    print("Este es tu listado de cuotas por mes: \n")
    print("MES \t CAPITAL \t INTERESES \t CAPITAL ADEUDADO")

    for t in range(1, n+1):    

        t_array.append(t)
        cuota_capital.append(get_deuda_capital(p, i, n, t-1) - get_deuda_capital(p, i, n, t))
        cuota_interes.append(cuota_total - cuota_capital[t-1])
        deuda_capital.append(get_deuda_capital(p, i, n, t))

        print(str(t) + "         " + \
              str('%.2f'%(cuota_capital[t-1])) + "         " + \
              str('%.2f'%(cuota_interes[t-1])) + "         " + \
              str('%.2f'%(deuda_capital[t-1]))
             )

def get_cuota_mensual_total_2(xs):
    print("hi")
    p=1000000
    i=0.14
    out = []
    for n in xs:
        num = p * i * (i+1)**n
        den = (i+1)**n - 1
        out.append(num/den)
    return out
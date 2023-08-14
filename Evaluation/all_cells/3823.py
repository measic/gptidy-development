from IPython.display import display
from IPython.display import HTML
from ipywidgets import interact
import ipywidgets as widgets

#import matplotlib.pyplot as plt
#import numpy as np
#import nbinteract as nbi

# funciones necesarias

# esta es la funcion de cuota mensual total
def get_cuota_mensual_total(p, i, n):
    num = p * i * (i+1)**n
    den = (i+1)**n - 1
    return num/den

# esta es la funcion de deuda capital en el mes t
def get_deuda_capital(p, i, n, t):
    coef = (((1+i)**t) - 1) / (((1+i)**n) - 1)
    return p * ( 1 - coef )

# esta funcion muestra la evolucion mes a mes del credito
def mostrar_evolucion_credito(P, I, N):
    
    p = P
    i = I / 12.0 * 0.01
    n = N * 12
    
    # calculo cuota mensual total
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

#meses = np.linspace(1, 20*12, 20*12)
#def get_mes(N):
 #   return np.linspace(1, N, N)

def get_cuota_mensual_total_2(xs):
    print("hi")
    p=1000000
    i=0.14
    out = []
    for n in xs:
        #print(n)
        num = p * i * (i+1)**n
        den = (i+1)**n - 1
        out.append(num/den)
    return out

#nbinteract --spec BrunoAlvarez89/PrestamoBanco/master prestamo_banco.ipynb
#nbi.line(get_mes, get_cuota_mensual_total_2, N=(1, 240))
r = 2
deg = 2
op_pol = polarization_operators(r, deg)
V_pol = PolarizedSpace(V_iso, op_pol)
for value in V_pol.values():
    show(value.basis())
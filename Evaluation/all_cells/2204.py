op_pol = polarization_operators(2, max_deg=v.degree())
W2 = PolarizedSpace(IsotypicComponent(W1, 3), op_pol)
character(W2)
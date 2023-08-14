V_iso = IsotypicComponent(V, 3, use_antisymmetry=True)
for value in V_iso.values():
    show(value.basis())
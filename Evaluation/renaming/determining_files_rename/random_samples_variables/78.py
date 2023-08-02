"""Plot function for nuclides half-life"""

def plot_nuclides(nuclides):
    from matplotlib import pyplot as plt
    fig, ax = plt.subplots(figsize=(18, 7))
    ax.plot([nc.Z for nc in nuclides.values()], [nc.half_life / 3600 / 24 / 365 for nc in nuclides.values()], ' ', color='black', marker='x', markersize=10)
    variable_def = min([nc.Z for nc in nuclides.values()])
    max_z = max([nc.Z for nc in nuclides.values()])
    ax.xaxis.set_ticks(range(variable_def, max_z + 1, 2))
    ax.set_xlim((variable_def - 1, max_z + 1))
    plt.xlabel('Nuclide Z Number', fontsize=18)
    plt.ylabel('$T_{1/2} [a]$', fontsize=18)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=16)
    ay1 = ax.twiny()
    ay1.set_xlim(ax.get_xlim())
    ay1.set_xticks([])
    from mendeleev import element
    ay1.set_xticks(range(variable_def, max_z + 1), [element(z).symbol for z in range(variable_def, max_z + 1)])
    ay1.set_xticklabels([element(z).symbol for z in range(variable_def, max_z + 1)], minor=True, fontsize=12)
    min_a = min([nc.A for nc in nuclides.values()])
    max_a = max([nc.A for nc in nuclides.values()])
    plt.title('%i Nuclides: $%i \\leq A \\leq %i$ ' % (len(nuclides), min_a, max_a), fontsize=22)
    ax.grid(True)
    plt.yscale('log')
    plt.show()
    return
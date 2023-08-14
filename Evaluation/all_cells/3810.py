from prettytable import PrettyTable
x = PrettyTable(["Filters","PYTHIA MB (%)", "PYTHIA PU = 2 (%)","PYTHIA PU = 3 (%)", "pp LowPU (%)", "pp MB (%)"])
x.padding_width = 1 # One space between column edges and contents (default)
x.add_row(["pileUpFilter_vtx1",98.7,35.5,7.4,94.9,71.5])
x.add_row(["pileUpFilter_Gplus",99.9,42.8,10.4,96.7,74.3])
x.add_row(["olvFilter_dz1p0",99.9,97.6,92.0,99.8,98.3])
print x

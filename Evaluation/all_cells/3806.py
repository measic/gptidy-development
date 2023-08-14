from prettytable import PrettyTable
x = PrettyTable(["Samples", "pileup", "Events(M)"])
x.align["City name"] = "l" # Left align city names
x.padding_width = 1 # One space between column edges and contents (default)
x.add_row(["pythia8 MinBias",1, 4.2])
x.add_row(["pythia8 MinBias",2, 4.1])
x.add_row(["pythia8 MinBias",3, 5.0])
x.add_row(["pp low pileup run", 0.1, 8.1])
x.add_row(["pp nominal pileup run", 1.4, 50.0])

print x
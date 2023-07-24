from prettytable import PrettyTable
from prettytable import ALL

Lx=PrettyTable(["nTrk","dz(cm)"])
Lx.padding_width = 1
Lx.hrules = ALL

#LnTrk = ["0-2","3","4","5","6-8","9","10","11-12","13","14-19","20-30","30+"]
#Ldz = ["N/A","4.8","1.9","1.2","0.8","0.6","0.5","0.4","0.3","0.2","0.1","0.0"]

TnTrk = ["0-1","2","3","4","5","6","7","8-10","11-13","14-22","22+","N/A"]
Tdz = ["N/A","4.0","1.5","1.0","0.6","0.5","0.4","0.3","0.2","0.1","0.0","N/A"]

Space = ["","","","","","","","","","","",""]

for num in range(len(TnTrk)):
	Lx.add_row([ TnTrk[num], Tdz[num]])

print Lx
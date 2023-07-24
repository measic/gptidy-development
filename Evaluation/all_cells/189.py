# Get the Min/Max Quarterly Revenue
QHrev= dfq.Revenue.max()[3]
QHLoss = dfq.Revenue.min()[3]
Qmax = max(dfq.idxmax())
Qmin = min(dfq.idxmin())

print('Highest Grossing Quarterly Revenue of $%.0f was observed on the %s %s-quarter.' %(QHrev,Qmax[0], Qmax[1] ))
print('Biggest Quarterly Loss of $%.00f was observed on the %s %s-quarter.' %(QHLoss,Qmin[0], Qmin[1] ))
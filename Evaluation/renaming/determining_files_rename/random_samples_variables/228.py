QHrev = dfq.Revenue.max()[3]
QHLoss = dfq.Revenue.min()[3]
Qmax = max(dfq.idxmax())
variable_def = min(dfq.idxmin())
print('Highest Grossing Quarterly Revenue of $%.0f was observed on the %s %s-quarter.' % (QHrev, Qmax[0], Qmax[1]))
print('Biggest Quarterly Loss of $%.00f was observed on the %s %s-quarter.' % (QHLoss, variable_def[0], variable_def[1]))
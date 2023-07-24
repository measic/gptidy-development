# Highest Grossing year
ymax = dfyy.idxmax()[3]
rmax = dfyy.max()[1]
rmaxt = dfyy.max()[3]
print("%s is the Highest Grossing Year in terms of Revenue Average and Total, $%0.2f and $%0.2f respectively." %(ymax,rmax,rmaxt))
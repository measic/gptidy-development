bankdata = loadDataFiles() # Load files
(minDate, maxDate) = getIntervalDates(bankdata) # Get dates interval
bankdata = fillEmpty(bankdata, maxDate) # Fill missing data with the same value

#plot_general(bankdata, minDate, maxDate)
#plot_piggy(bankdata)
plot_super_view(bankdata, minDate, maxDate)
#plot_profit(bankdata)
#plot_incomesExpenses(bankdata)
plot_incomesExpensesProfits(bankdata)
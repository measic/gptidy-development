def getIntervalDates(bankdata):
    minDate = ''
    maxDate = ''
    first = True
    
    for accountType in ACCOUNTTYPES:
        for bank in bankdata[accountType]:
            dates = np.array(bankdata[accountType][bank]['date'])
            
            if first:
                minDate = dates.min()
                maxDate = dates.max()
                
                first = False
            else:
                if minDate > dates.min():
                    minDate = dates.min()

                if maxDate < dates.max():
                    maxDate = dates.max()

    return (minDate, maxDate)
def fillEmpty(bankdata, maxDate):
    for accountType in ACCOUNTTYPES:
        for bank in bankdata[accountType]:
            if bankdata[accountType][bank]['date'][-1] != maxDate:
                bankdata[accountType][bank]["balance"] = bankdata[accountType][bank]["balance"] + (bankdata[accountType][bank]["balance"][-1],)
                bankdata[accountType][bank]["date"] = bankdata[accountType][bank]["date"] + (maxDate,)
                
    return bankdata
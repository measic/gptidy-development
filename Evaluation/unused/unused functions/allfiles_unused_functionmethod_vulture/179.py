def sortDataFiles(bankdata):
    for accountType in ACCOUNTTYPES:
        for bankname in bankdata[accountType]:
            if "movements" in bankdata[accountType][bankname]:
                (bankdata[accountType][bankname]["date"], bankdata[accountType][bankname]["balance"], bankdata[accountType][bankname]["movements"]) = zip(*sorted(zip(bankdata[accountType][bankname]["date"], bankdata[accountType][bankname]["balance"], bankdata[accountType][bankname]["movements"])))
            else:
                (bankdata[accountType][bankname]["date"], bankdata[accountType][bankname]["balance"]) = zip(*sorted(zip(bankdata[accountType][bankname]["date"], bankdata[accountType][bankname]["balance"])))
            
    return bankdata
def loadDataFiles():    
    print("Data files found:")
    bankdata = {}
    for accountType in ACCOUNTTYPES:
        path = "accounts/{}/".format(accountType)
        directories = [f for f in os.listdir(path) if os.path.isdir(path+f)]
        bankdata[accountType] = {}
        for bankname in directories:
            bankdata[accountType][bankname] = {"date":[], "balance":[], "movements":[]}
            files = [os.path.join(path+bankname,f) for f in os.listdir(path+bankname)]
            #files.sort(key=lambda x: os.path.getmtime(x))
            for datafile in files:
                extension = os.path.splitext(datafile)[1]
                if extension == ".xls":
                    print("{} - {}".format(bankname, datafile))
                    (balance, date, movements) = processXLS(datafile, bankname)
                    bankdata[accountType][bankname]["balance"].extend(balance)
                    bankdata[accountType][bankname]["date"].extend(date)
                    bankdata[accountType][bankname]["movements"].extend(movements)
                if extension == ".csv":
                    print("{} - {}".format(bankname, datafile))
                    (balance, date, movements) = processCSV(datafile, '\t', bankname)
                    bankdata[accountType][bankname]["balance"].extend(balance)
                    bankdata[accountType][bankname]["date"].extend(date)
                    bankdata[accountType][bankname]["movements"].extend(movements)

    return sortDataFiles(bankdata)
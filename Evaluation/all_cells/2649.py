def buildProfit(bankdata):
    data = []

    for bank in bankdata[CURRENT]:
        dates = bankdata[CURRENT][bank]['date']
        movements = bankdata[CURRENT][bank]['movements']

        profit = {}
        for date, movement in zip(dates, movements):
            key = str(date.month) + '/' + str(date.year)

            if key in profit:
                profit[key] += float(movement)
            else:
                profit[key] = float(movement)
            
        months = []
        profits = []
        for key, value in profit.items():
            months.append(dt.datetime.strptime(key, '%m/%Y').date())
            profits.append(value)
        
        trace = go.Bar(
            x = months,
            y = profits,
            name = "Profit for {}".format(SUPPORTED_BANKS[bank])
        )
        data.append(trace)
        
    return data
def buildIncomesExpenses(bankdata):
    data = []

    for bank in bankdata[CURRENT]:
        dates = bankdata[CURRENT][bank]['date']
        movements = bankdata[CURRENT][bank]['movements']

        incomes = {}
        expenses = {}
        for date, movement in zip(dates, movements):
            key = str(date.month) + '/' + str(date.year)

            if float(movement) > 0:
                if key in incomes:
                    incomes[key] += float(movement)
                else:
                    incomes[key] = float(movement)
            else:
                if key in expenses:
                    expenses[key] += float(movement)
                else:
                    expenses[key] = float(movement)
            
        months_x = []
        incomes_y = []
        for key, value in incomes.items():
            months_x.append(dt.datetime.strptime(key, '%m/%Y').date())
            incomes_y.append(value)
        
        trace = go.Bar(
            x = months_x,
            y = incomes_y,
            name = "Incomes for {}".format(SUPPORTED_BANKS[bank])
        )
        data.append(trace)
        
        months_x = []
        expenses_y = []
        for key, value in expenses.items():
            months_x.append(dt.datetime.strptime(key, '%m/%Y').date())
            expenses_y.append(value)
        
        trace = go.Bar(
            x = months_x,
            y = expenses_y,
            name = "Expenses for {}".format(SUPPORTED_BANKS[bank])
        )
        data.append(trace)
        
    return data
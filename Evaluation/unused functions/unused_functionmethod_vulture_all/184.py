def buildTraces(bankdata, min_trace = False, mean_trace = False, max_trace = False):
    data = []
    min_amount = 0
    max_amount = 0
    
    for accountType in ACCOUNTTYPES: # Account type
        for bank in bankdata[accountType]: # Bank name
            dates = np.array(bankdata[accountType][bank]['date'])
            balances = np.array(bankdata[accountType][bank]['balance'])
            
            bankName = '(' + accountType + ') ' + SUPPORTED_BANKS[bank]

            trace_main = go.Scatter(
                x = dates,
                y = balances,
                name = bankName + ': Saldo ' + str(format(balances[-1], ',.2f').replace(",", "X").replace(".", ",").replace("X", ".")) + CURRENCY,
                #line = dict(
                #    color = 'green'
                #),
                mode = 'lines'
            )
            data.append(trace_main)

            if max_trace:
                trace_max = go.Scatter(
                    x = dates,
                    y = [balances.max() for f in dates],
                    name = bankName + ': Saldo máximo',
                    #visible = 'legendonly',
                    #hoverinfo = 'name',
                    line = dict(
                        #color = 'cyan',
                        width = 4,
                        dash = 'dot'
                    )
                )
                data.append(trace_max)

            if mean_trace:
                trace_mean = go.Scatter(
                    x = dates,
                    y = [balances.mean() for f in dates],
                    name = bankName + ': Saldo medio',
                    #hoverinfo = 'none',
                    line = dict(
                        #color = 'magenta',
                        width = 4,
                        dash = 'dashdot'
                    )
                )
                data.append(trace_mean)

            if min_trace:
                trace_min = go.Scatter(
                    x = dates,
                    y = [balances.min() for f in dates],
                    name = bankName + ': Saldo mínimo',
                    line = dict(
                        #color = 'red',
                        width = 4,
                        dash = 'dot'
                    )
                )
                data.append(trace_min)
                
            # Extra
            if balances.max() > max_amount:
                max_amount = balances.max()
    
    max_amount, sum_trace = get_trace_sum_balances(bankdata)
    data.append(sum_trace)
    
    return (data, min_amount, max_amount)
def daterange(d1, d2):
    return (d1 + dt.timedelta(days=i) for i in range((d2 - d1).days + 1))

def get_trace_sum_balances(bankdata):
    sum_balances = []
    for bank in bankdata[CURRENT]:
        dates = bankdata[CURRENT][bank]['date']
        balances = bankdata[CURRENT][bank]['balance']
        sum_account = {}
        for date, balance in zip(dates, balances):
            sum_account[date] = balance
                
        sum_balances.append(sum_account)
    
    total = {}
    (ini, fin) = getIntervalDates(bankdata)
    last = 0
    max_amount = 0
    for b in sum_balances:
        for d in daterange(ini, fin):
            if d in b:
                last = b[d]                    
                if d in total:
                    total[d] += b[d]
                    if total[d] > max_amount:
                        max_amount = total[d]
                else:
                    total[d] = b[d]
            else:
                if d in total:
                    total[d] += last
                else:
                    total[d] = last
                
    
    dates = total.keys()
    balances = total.values()
    
    (dates, balances) = zip(*sorted(zip(dates, balances)))
    
    trace = go.Scatter(
        x = dates,
        y = balances,
        name = "All Accounts - Amount: " + format(balances[-1], ',.2f').replace(",", "X").replace(".", ",").replace("X", ".") + CURRENCY,
        mode = 'lines',
        line = dict ( width = 4 )
    )

    return (max_amount, trace)
def buildPiggy(bankdata):
    traces = []
    
    for bank in bankdata[SAVING]: # Bank name
        balances = np.array(bankdata[SAVING][bank]['balance'])
        
        trace = go.Bar(
            x = ['Piggy'],
            y = [balances[-1]],
            name = SUPPORTED_BANKS[bank]
        )
        
        traces.append(trace)
        
    return traces
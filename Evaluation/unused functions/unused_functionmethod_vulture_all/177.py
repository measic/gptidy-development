def processCSV(file, splitToken, bank): #TODO Move to pandas
    fecha = []
    saldo = []
    movimientos = []
    first = True
    
    if bank == 'cajamar':
        with open(file) as f:
            for line in f:
                if first is False:
                    tokens = line.split(splitToken)
                    fecha.append(dt.datetime.strptime(tokens[0], '%d/%m/%Y').date())
                    saldo.append(float(tokens[len(tokens)-1][:-1].replace('.', '').replace(',', '.')))
                    movimientos.append(float(tokens[len(tokens)-2].replace('.','').replace(',','.').replace(' ', '')))
                first = False

    return (saldo, fecha, movimientos)
def processXLS(file, bank):   
    balance = []
    date = []
    movements = []
    
    if bank == 'unicaja':
        book = xlrd.open_workbook(file)
        first_sheet = book.sheet_by_index(0)
        date_int = first_sheet.col_values(0)[5:]
        balance = first_sheet.col_values(5)[5:]
        movements = first_sheet.col_values(3)[5:]
        date = [xlrd.xldate_as_datetime(date_int[i], book.datemode).date() for i in xrange(0, len(date_int))]
    
    if bank == 'openbank':
        df = pd.read_html(file)
        df = df[0].dropna(axis=0, thresh=4)
        date_str = df.iloc[1:,1]
        date = [dt.datetime.strptime(x, '%d/%m/%Y').date() for x in date_str]
        balance_str = df.iloc[1:,9]
        balance = [float((x[:-2] + ',' + x[-2:]).replace('.','').replace(',','.')) for x in balance_str]
        movements_str = df.iloc[1:,7]
        movements = [float((x[:-2] + ',' + x[-2:]).replace('.','').replace(',','.')) for x in movements_str]

    return (balance, date, movements)
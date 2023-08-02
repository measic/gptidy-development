def dateRange(start, end):
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    return [datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(i), "%Y-%m-%d") for i in xrange(days)]
#len(dateRange('2015-07-01','2016-10-31'))

def date_to_week(date):
    if type(date) == str:
        date = pd.to_datetime(date).date()
    #type(date) == datetime.date
    return (date - datetime.date(2015,7,7)).days  / 7

# 2015-07-07 2015-07-13   

def week_to_date(week_number,return_str=True):
    if week_to_date:
        return [(datetime.date(2015,7,7)+ datetime.timedelta(week_number*7)).strftime("%Y-%m-%d"),(datetime.date(2015,7,13)+ datetime.timedelta(week_number*7)).strftime("%Y-%m-%d")]
    return [datetime.date(2015,7,7)+ datetime.timedelta(week_number*7),datetime.date(2015,7,13)+ datetime.timedelta(week_number*7)]

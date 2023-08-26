bivar = sorted(filter(lambda r: len(r[0]) == 1, storage.relevancies.relevancy.iteritems()), 
               key=lambda r: r[1], reverse=True)
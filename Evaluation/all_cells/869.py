# BK - functie is later herschreven door DB, welke hierboven staat

#import time

#def vindLocatie (leerlingen, postcodes):
#    toReturn = []
#    for leerling in leerlingen:
#        detected = []
#        for postcode in postcodes:
#            postcodeleerling = leerling[0]
#            if leerling[1] == 4 and postcodeleerling >= postcode[0] and postcodeleerling <= postcode[1]:
#                detected.append(postcode[2])
#        toReturn.append(detected)
#    return toReturn

#def vindCategorie (leerlingen, postcodes):
#    toReturn = []
#    for leerling in leerlingen:
#        detected = []
#        for postcode in postcodes:
#            postcodeleerling = leerling[0]
#            if leerling[1] == 4 and postcodeleerling >= postcode[0] and postcodeleerling <= postcode[1]:
#                detected.append(postcode[2])
#        toReturn.append(detected)
#    return toReturn
    
#start = time.time()

#subset dataframes
#opleidingList = datasource[['PC4_LEERL', 'KWALIFICATIENIVEAU']].values
#locatieList = wervingsgebieden[['PostcodeStart','PostcodeEind','Locatie']].values
#categorieList = wervingsgebieden[['PostcodeStart','PostcodeEind','Categorie']].values

#add queries data to datasource
#datasource["Locatie"] = vindLocatie(opleidingList, locatieList)
#datasource["Categorie"] = vindCategorie(opleidingList, categorieList)
#print (time.time() - start)
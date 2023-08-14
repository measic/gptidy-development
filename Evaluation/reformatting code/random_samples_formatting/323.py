# Functie voor het checken van de locatie
def check_locatie(PostCode):
    test = wervingsgebieden.loc[(wervingsgebieden.PostcodeStart <= PostCode) & (wervingsgebieden.PostcodeEind >= PostCode), ['Locatie']]

    if test.empty:
        return ''
    else:
        return test['Locatie'].iloc[0]
# copy-paste voor de categorie
def check_categorie(PostCode):
    test = wervingsgebieden.loc[(wervingsgebieden.PostcodeStart <= PostCode) & (wervingsgebieden.PostcodeEind >= PostCode), ['Categorie']]

    if test.empty:
        return ''
    elif test.Categorie.count() > 1:
        return 'Meerdere'
    else:
        return test['Categorie'].iloc[0]

#voeg kolommen toe aan datasource    
datasource["Locatie"] = datasource["PC4_LEERL"].apply(check_locatie)
datasource["Categorie"] = datasource["PC4_LEERL"].apply(check_categorie)
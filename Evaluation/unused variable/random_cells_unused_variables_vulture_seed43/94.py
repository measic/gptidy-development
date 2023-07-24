# maak document, met daarin grafiek. Hier zullen (uiteindelijk) meerdere grafieken moeten worden 
# weergegeven met meerdere opties.

def make_document(doc):
    #Kolommen zijn de kolommen uit de df_totaalSBB dataframe. Dit gaat dan om 2013 AANT etc. Dit is voor de eerste groepering. 
    kolommen = list(df_totaalSBB)

    #Sectoren haalt alle unieke waardes uit het dataframe voor de kolom SECTORUNIT SBB.
    sectoren = list(df['SECTORUNIT SBB'].unique())

    #Voeg per kolom alle sectoren toe. Dit wordt dan de data voor de x-as. 
    #Kolom is bijvoorbeeld 2013 AANT en hier worden vervolgens alle sectoren aan toegevoegd.
    x = [ (kolom, sector) for kolom in kolommen for sector in sectoren ]

    #Data voor de y-as
    #Data doorlopen om de totalen op de juiste volgorde in een array te plaatsen.
    #Zelfde volgorde zoals hierboven staat voor de gegevens voor de x-as

    counts = []

    for kolom in kolommen:
        for sector in sectoren:
            counts.append(df_totaalSBB.loc[sector][kolom])

    #Teken grafiek
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    p = figure(x_range=FactorRange(*x), plot_height=400, title="Totalen per SBB sector per jaar")

    p.vbar(x='x', top='counts', width=0.8, source=source)

    p.width=900
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None


    #update functie om nieuwe data(selecties) weer te geven
    def updateSBB(attr, old, new):
        kolommen = [jaren.labels[i] for i in jaren.active]
        x = [ (kolom, sector) for kolom in kolommen for sector in sectoren ]

        counts = []

        for kolom in kolommen:
            for sector in sectoren:
                counts.append(df_totaalSBB.loc[sector][kolom])

        newSource = ColumnDataSource(data=dict(x=x, counts=counts))
        source.data.update(newSource.data)
    
    
    jaren = CheckboxGroup(labels=kolommen, active = [0, 1, 2, 3 ,4])
    jaren.on_change('active', updateSBB)

    layout = row(p, jaren)

    #callback om updates elke 100ms op te halen
    #doc.add_periodic_callback(update, 100)

    doc.title = "Sectorunit SBB chart..."
    doc.add_root(layout)

    # maak document, met daarin grafiek. Hier zullen (uiteindelijk) meerdere grafieken moeten worden 
    # weergegeven met meerdere opties.

    #def aantal_zwolle(doc):

        #Kolommen zijn de kolommen uit de df_totaalSBB dataframe. Dit gaat dan om 2013 AANT etc. Dit is voor de eerste groepering. 
        #kolommen_zwolle = list(df_aantal_zwolle)

        #Sectoren haalt alle unieke waardes uit het dataframe voor de kolom SECTORUNIT SBB.
        #locaties_zwolle = list(df_aantal_zwolle['Locatie'].unique())

        #Voeg per kolom alle sectoren toe. Dit wordt dan de data voor de x-as. 
        #Kolom is bijvoorbeeld 2013 AANT en hier worden vervolgens alle sectoren aan toegevoegd.
        #x = [ (kolom, locatie) for kolom in kolommen_zwolle for locatie in locaties_zwolle ]

        #Data voor de y-as
        #Data doorlopen om de totalen op de juiste volgorde in een array te plaatsen.
        #Zelfde volgorde zoals hierboven staat voor de gegevens voor de x-as

        #counts = []

        #for kolom in kolommen_zwolle:
        #   for locatie in locaties_zwolle:
        #        counts.append(df_aantal_zwolle.loc[sector][kolom])

        #Teken grafiek
        #source = ColumnDataSource(data=dict(x=x, counts=counts))

        #az = figure(x_range=FactorRange(*x), plot_height=400, title="Aantal MBO Afgestudeerden Regio Zwolle")

        #az.vbar(x='x', top='counts', width=0.8, source=source)

        #az.width=900
        #az.y_range.start = 0
        #az.x_range.range_padding = 0.1
        #az.xaxis.major_label_orientation = 1
        #az.xgrid.grid_line_color = None
   

        #update functie om nieuwe data(selecties) weer te geven, doet nu niets...
        #def update():

        #callback om updates elke 100ms op te halen
        #doc.add_periodic_callback(update, 100)
        
        
        #doc.title = "Tekst..."
        #doc.add_root(az)
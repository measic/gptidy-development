#Kolommen zijn de kolommen uit de df_totaalSBB dataframe. Dit gaat dan om 2013 AANT etc. Dit is voor de eerste groepering. 
kolommen_zwolle = list(df_aantal_zwolle)

#Sectoren haalt alle unieke waardes uit het dataframe voor de kolom SECTORUNIT SBB.
locaties_zwolle = list(df_locatie_zwolle['Locatie'].unique())

#Voeg per kolom alle sectoren toe. Dit wordt dan de data voor de x-as. 
#Kolom is bijvoorbeeld 2013 AANT en hier worden vervolgens alle sectoren aan toegevoegd.
x = [ (kolom, locatie) for kolom in kolommen_zwolle for locatie in locaties_zwolle ]

#Data voor de y-as
#Data doorlopen om de totalen op de juiste volgorde in een array te plaatsen.
#Zelfde volgorde zoals hierboven staat voor de gegevens voor de x-as

counts = []

for kolom in kolommen_zwolle:
    for locatie in locaties_zwolle:
        counts.append(df_aantal_zwolle.loc[locatie][kolom])

#Teken grafiek
source = ColumnDataSource(data=dict(x=x, counts=counts))

az = figure(x_range=FactorRange(*x), plot_height=400, title="Aantal MBO Afgestudeerden Regio Zwolle")

az.vbar(x='x', top='counts', width=0.8, source=source)

az.width=900
az.y_range.start = 0
az.x_range.range_padding = 0.1
az.xaxis.major_label_orientation = 1
az.xgrid.grid_line_color = None


#update functie om nieuwe data(selecties) weer te geven, doet nu niets...
#def update():

#callback om updates elke 100ms op te halen
#doc.add_periodic_callback(update, 100)

show(az)
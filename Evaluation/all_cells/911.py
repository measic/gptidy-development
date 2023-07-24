#output_notebook()

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

show(p)
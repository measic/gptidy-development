# from bokeh.palettes import Spectral6

# Kolommen zijn de kolommen uit de df_totaalSBB dataframe. Dit gaat dan om 2013 AANT etc. Dit is voor de eerste groepering. 
# kolommen = list(df_totaalSBB)

# Sectoren haalt alle unieke waardes uit het dataframe voor de kolom SECTORUNIT SBB.
# sectoren = df['SECTORUNIT SBB'].unique()
# sectorenMultiplied = []

# Voeg per kolom alle sectoren toe. Dit wordt dan de data voor de x-as. 
# Kolom is bijvoorbeeld 2013 AANT en hier worden vervolgens alle sectoren aan toegevoegd.
# x = [ (sector, kolom) for sector in sectoren for kolom in kolommen ]

# Data voor de y-as
# Data doorlopen om de totalen op de juiste volgorde in een array te plaatsen.
# Zelfde volgorde zoals hierboven staat voor de gegevens voor de x-as

# counts = []

# for sector in sectoren:
#     for kolom in kolommen:
#         counts.append(df_totaalSBB.loc[sector][kolom])

# cyl_cmap = factor_cmap('cyl', palette=Spectral5, factors=sorted(df.cyl.unique())
# Teken grafiek
# source = ColumnDataSource(data=dict(x=x, counts=counts, sectoren=sectorenMultiplied, color=Spectral6))
# p = figure(x_range=FactorRange(*x), plot_height=400, title="Totalen per SBB sector per jaar")
# p.vbar(x='x', top='counts', width=0.8, legend='sectoren', color='color', source=source)

# p.width=1000
# p.y_range.start = 0
# p.x_range.range_padding = 0.1
# p.xaxis.major_label_orientation = 'vertical'
# p.xgrid.grid_line_color = None

# p.legend.orientation = "horizontal"
# p.legend.location = "top_center"

# p.xaxis[0].group_text_font_size = '0pt'
# show(p)
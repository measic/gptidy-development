def updateSBB(attr, old, new):
    kolommen = [jaren.labels[i] for i in jaren.active]
    x = [ (kolom, sector) for kolom in kolommen for sector in sectoren ]
   
    counts = []
    
    for kolom in kolommen:
        for sector in sectoren:
            counts.append(df_totaalSBB.loc[sector][kolom])
    
    newSource = ColumnDataSource(data=dict(x=x, counts=counts))
    source.data.update(newSource.data)
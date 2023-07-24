def update_sbb(attr, old, new):
    kolommen = [jaren.labels[i] for i in jaren.active]
    x = [(kolom, sector) for kolom in kolommen for sector in sectoren]

    counts = []

    for kolom in kolommen:
        for sector in sectoren:
            counts.append(df_totaal_sbb.loc[sector][kolom])

    new_source = ColumnDataSource(data=dict(x=x, counts=counts))
    source.data.update(new_source.data)
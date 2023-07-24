# Need to overlay the Swiss topo file on the generic Folio map
ch_map = folium.Map(location=[46.9, 8.3], tiles='Mapbox Bright', zoom_start=7)
#folium.TopoJson(open(topo_geo), 'objects.cantons', name = 'topojson').add_to(ch_map)
#folium.LayerControl().add_to(ch_map)

ch_map.geo_json(geo_path=topo_geo, 
        data=grants_data_all_cantons,
        columns=['Canton Shortname', 'Approved Amount'],
        key_on='feature.id',
        topojson='objects.cantons',
        fill_color='YlGnBu',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='Total Grant Amount by Canton (tens millions CHF) (1970+)',
        threshold_scale=[0,0.01,10,150,300,400],
        reset = True)
ch_map.save('swiss.html')
ch_map
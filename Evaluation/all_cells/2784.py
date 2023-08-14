airports = pd.read_csv('test/airports.csv')
airports=airports[airports['traffic'] > 8000]
chart_3 = MapChart(dataframe = airports, 
       projection = "albersUsa", 
       region = "US", 
       unit = 'airport', 
       value = 'traffic',
       canvas_height=800,
       canvas_width = 1200
      )\
.addTooltip()\
.addMarker({"shape":'circle', "color":"steelblue", "scale": 0.5, "opacity": 0.5})

chart_3.show()

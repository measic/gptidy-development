chart_2 = MapChart(dataframe = df, 
       projection = "orthographic", 
       region = "world", 
       unit = 'country', 
       value = 'searches', coerce_country=False
      )\
.addColor(options = {"palette": {"min":"lightblue", "max": "steelblue"}, "opacity": 0.5})\
.enableZoom()\
.enableClickToCenter()\
.addTooltip()

chart_2.show()
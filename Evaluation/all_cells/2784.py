df = pd.read_csv('test/country_test.csv')
chart_1 = MapChart(dataframe = df,
          projection = "mercator", 
           region = "world", 
           unit = 'country', 
           value = 'searches', coerce_country=False)\
.addColor(options = {"palette": {"min":"lightgreen", "max": "#456b01"}, "opacity": 0.4})\
.addTooltip()\
.enableZoom()

chart_1.show()
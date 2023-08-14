source = ColumnDataSource({'lat':data['Latitude'],'lon':data['Longitude'],'studys': data['Study'],
                           'report': data['Report'],'fill':data['Color'],'type':data['Type'],'date':data['Date']})
circle = Circle(x="lon",y="lat",size=15,fill_color="fill")
plot.add_glyph(source, circle)

pan = PanTool()
wheel_zoom = WheelZoomTool()
hover = HoverTool()
hover.tooltips = [('Study Title','@studys'),('Date','@date'),('Type','@type')]
tap = TapTool()
url = "@report"
TapTool.callback = OpenURL(url=url)

plot.add_tools(pan,wheel_zoom,hover,tap)
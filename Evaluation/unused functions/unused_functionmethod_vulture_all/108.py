#Plots edge (x1,y1)(x2,y2) on the road
#"nyc" is map objet we are plotting on
#default color is red; default width of road is 3
def plotRoad(x1, x2, y1, y2, nyc, color = 'red', width = 3):
    nyc.add_child(PolyLine(locations=[(x1,y1),(x2,y2)],color=color,weight=width))

#Plots intersection onto map with marker
#x,y - latitude and longitude; nyc - 
def plotNode(x,y,nyc,sides = 4, radius = 2, color = 'black'):
    nyc.add_child(RegularPolygonMarker(location=[x,y],number_of_sides = sides, color = color,radius = radius))

#Given list of linkIDs in ROADS plots them onto the map
#data should be pandas dataframe of links
#nyc - map object; roads - list of linkids that need to be plotted
#data - pandas object should just be link
def plotRoads(nyc, roads, data, color = 'red', width = 3):
    print(len(roads))
    count = 0
    for ID in roads:
        road = data[data['link_id'] == ID]
        plotRoad(road['startY'].values[0], road['endY'].values[0],road['startX'].values[0], road['endX'].values[0], nyc, color, width)
        count = count + 1
        if(count % 100 == 0):
            print(count)

#initialize Map object centered in NYC
def initializeMap():
    NY_COORDINATES = (40.7566,-73.9815)
    m = folium.Map(location=NY_COORDINATES, zoom_start=15)
    folium.TileLayer('cartodbpositron').add_to(m)
    folium.LayerControl().add_to(m)
    #LatLngPopup enables us to know the latitude and longtitude of any position with one click
    m.add_child(LatLngPopup())
    print('initialized map')
    return m

#reads txt file into a list
def readIntTxtToList(path):
        f = open(path)
        arr = []
        for i in f:
            arr.append(i)
        arr = [int(x.strip()) for x in arr]
        return arr

#writes txt file into a list
def writeIntArrayToTxt(path, arr):
    print(len(arr))
    with open(path, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(arr)


#saves map
def saveMap(map_name, str_, ave_):
    citymap = initializeMap()
    if(str_ != None):
        plotRoads(citymap, str_, links, 'blue', 3)
        print('plotted streets')
    if(ave_ != None):
        plotRoads(citymap, ave_, links, 'red', 3)
        print('plotted avenues')

    citymap.save(map_name)
    print('{0} saved'.format(map_name))
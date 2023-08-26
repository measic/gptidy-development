#Given kml file path, extracts boundary points in regions
def extractPolyFromKML(kmlpath):
    root = parser.fromstring(open(kmlpath, 'r').read())
    regions = []
    placemark = root.Document.Placemark
    for i in range(len(placemark)):
        block = []
        r = str(root.Document.Placemark[i].Polygon.outerBoundaryIs.LinearRing.coordinates).split()
        if r is not None:
            for point in r:
                loc = point.split(',')[0:2]
                block.append(tuple([float(loc[0]),float(loc[1])]))
            regions.append(block)
    return regions

#visualizes each of the regions with a list of colors onto map m
def visualizePoly(regions, colors, m):
    for region in range(len(regions)):
        for i in range(len(regions[region])):
            if( i < len(regions[region]) -1):
                point1 = regions[region][i]
                point2 = regions[region][i+1]
                plotRoad(point1[1], point2[1], point1[0], point2[0], m, color = colors[region], width = 3)
    return m
#visualizes each of the nodes in inter with a list of colors onto a map m
#nodes should be passed into nodes
def visualizeNodes(inter, colors, nodes, m):
    for region in range(len(inter)):
        c = colors[region]
        for idd in inter[region]:
            p = nodes[nodes['node_id'] == idd]
            x = p['xcoord'].values[0]
            y = p['ycoord'].values[0]
            plotNode(y,x,m,sides = 4, radius = 2, color = c)
    return m

#plots a list of lists containing linkIds with different colors
def visualizeLinks(_regionNodes, _regionLinks, colors, links, m):
    for i in range(len(_regionNodes)):
        plotRoads(m, _regionLinks[i], links, color = colors[i], width = 3)
    return m

#given
def nodesPerRegion(regions,nodes):
    regionNodes = []
    for i in range(len(regions)):
        print(i)
        regionNodes.append(getNodes(regions[i],nodes))
    return regionNodes

def linksPerRegion(regionNodes, links):
    regionLinks = [[] for i in range(len(regionNodes))]
    for i in range(len(links)):
        link = links.iloc[i]
        beginNode = link['begin_node_id']
        endNode = link['end_node_id']
        for i in range(len(regionLinks)):
            if beginNode in regionNodes[i] and endNode in regionNodes[i]:
                regionLinks[i].append(link['link_id'])
    return regionLinks
   


def getNodes(region, nodes):
    inter = []
    verts = region
    codes = [mplPath.Path.LINETO] * len(verts)
    codes[0] = mplPath.Path.MOVETO
    codes[-1] = mplPath.Path.CLOSEPOLY
    poly = mplPath.Path(verts,codes)
    for i in range(len(nodes)):
        p = nodes.iloc[i]
        x = p['xcoord']
        y = p['ycoord']
        if(poly.contains_point((x,y))):
            inter.append(p['node_id'])
    inter = [int(i) for i in inter]
    return inter


def writeToCSV(data, filename):
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(data)
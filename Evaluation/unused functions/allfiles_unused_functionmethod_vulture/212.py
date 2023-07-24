from arcgis import geometry
from arcgis import features

def create_feature(map1, g):
    try:
        oid = 1
        pt = geometry.Point(g)
        feat = features.Feature(geometry=pt, attributes={'OBJECTID': 1,
                                                        'name': 'name',
                                                        'type': 'park',
                                                        'surface': 'dirt'})
        feature_layer.edit_features(adds=[feat])
        print(str(g))
        map1.draw(g)
    except:
        print("Couldn't create the feature. Try again, please...")
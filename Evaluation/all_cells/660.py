# Need to be able to extract the id of the canton from the topo file
from pprint import pprint

with open(topo_geo) as data_file:    
    data = json.load(data_file)
#pprint(data)

data['objects']['cantons']['geometries'][25]['id']

#len(data['objects']['cantons']['geometries'])
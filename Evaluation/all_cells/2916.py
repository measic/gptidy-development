output_filename = 'leaflet/location-dataset.js'
with open(output_filename, 'w') as output_file:
    output_file.write('var dataset = {};'.format(json.dumps(geojson, separators=(',',':'))))
print('{:,} geotagged features saved to file'.format(len(geojson['features'])))
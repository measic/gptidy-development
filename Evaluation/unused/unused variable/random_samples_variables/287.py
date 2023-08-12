fn = path.join(DATA,'field-orientations.geojson')

with fiona.open(fn) as ds:
    for i,item in ds.items():
        p = item['properties']
        if p['planeType'].strip() != 'Bedding':
            continue

        asm = p.get("aster_smoothed")
        alt = asm

        alt -= 40 # Global datum is higher than local
        center = (*item['geometry']['coordinates'],alt)

        err = 0.1*N.pi/180
        a = ReconstructedPlane(p['strike'], p['dip'],0,err,err)
        orientation = a.to_mapping(
            center=center,
            color='#444', type='in-situ')
        collection.append(orientation)

removedUIDs = ["89636280","6031fd6f"]
collection = [c for c in collection if 1600 < c['center'][2] < 1680]
collection = [c for c in collection if c['uid'] not in removedUIDs]
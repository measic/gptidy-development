fn = path.join(DATA,'elevations_v2.dxf')

orientations = []
with fiona.open(fn) as ds:
    for i,item in ds.items():
        coords = N.array(item['geometry']['coordinates'])
        try:
            orientations.append(Orientation(coords))
        except ValueError:
            continue

disabled = ["afb1b38f","ebab5ecb","7b12f5d4","72417f52","8565a276","939d9b9a",
            "e884eac1", "c8902997","15026bc4","730a6124","eb31c4b0","d3793eb9"]
orientations = [o for o in orientations if o.hash not in disabled]

groups = (
    ["3df53944","e98e12a9"],
    ["493a240a","04987fe8"],
    ["c2122b2a","de785eb5"]
)

groupedOrientations = create_groups(orientations, *groups,
                             same_plane=False)

collection = [a.to_mapping(color='#ff0000', type='remote')
              for a in groupedOrientations]
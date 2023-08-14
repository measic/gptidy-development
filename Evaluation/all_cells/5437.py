from stix2 import Filter

# retrieve multiple object from TAXIICollectionSource
# by using filters
f1 = Filter("type","=", "indicator")

indicators = tc_source.query([f1])

#for visual purposes
for indicator in indicators:
    print(indicator.serialize(pretty=True))
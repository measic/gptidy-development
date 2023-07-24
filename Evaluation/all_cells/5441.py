from stix2 import TAXIICollectionStore

# create TAXIICollectionStore - note the same collection instance can
# be used for the store
tc_store = TAXIICollectionStore(collection)

# retrieve STIX object by id from TAXII Collection through
# TAXIICollectionStore
stix_obj2 = tc_source.get("malware--c0931cc6-c75e-47e5-9036-78fabc95d4ec")

print(stix_obj2.serialize(pretty=True))
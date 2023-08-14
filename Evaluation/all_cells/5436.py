from stix2 import TAXIICollectionSource
from taxii2client import Collection

# establish TAXII2 Collection instance
collection = Collection("http://127.0.0.1:5000/trustgroup1/collections/91a7b528-80eb-42ed-a74d-c6fbd5a26116/", user="admin", password="Password0")
# supply the TAXII2 collection to TAXIICollection
tc_source = TAXIICollectionSource(collection)

#retrieve STIX objects by id
stix_obj = tc_source.get("malware--c0931cc6-c75e-47e5-9036-78fabc95d4ec")
stix_obj_versions = tc_source.all_versions("indicator--6770298f-0fd8-471a-ab8c-1c658a46574e")

#for visual purposes
print(stix_obj.serialize(pretty=True))
print("-------")
for so in stix_obj_versions:
    print(so.serialize(pretty=True))

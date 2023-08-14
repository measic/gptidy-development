from stix2 import Indicator

# add STIX object to TAXIICollectionStore
ind = Indicator(description="Smokey Bear implant",
                pattern_type="stix",
                pattern="[file:hashes.'SHA-256' = '09c7e05a39a59428743635242e4a867c932140a909f12a1e54fa7ee6a440c73b']")

tc_store.add(ind)
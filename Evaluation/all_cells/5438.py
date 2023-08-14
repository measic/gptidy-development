from stix2 import TAXIICollectionSink, ThreatActor

#create TAXIICollectionSINK and push STIX content to it
tc_sink = TAXIICollectionSink(collection)

# create new STIX threat-actor
ta = ThreatActor(name="Teddy Bear",
                threat_actor_types=["nation-state"],
                sophistication="innovator",
                resource_level="government",
                goals=[
                    "compromising environment NGOs",
                    "water-hole attacks geared towards energy sector",
                ])

tc_sink.add(ta)
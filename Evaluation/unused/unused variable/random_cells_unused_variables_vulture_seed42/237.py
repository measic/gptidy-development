# Let's start by creating our geolocator. We will use Google Maps API :
googlemapsapikeyjson = json.loads(open('google_maps_api_keys.json').read())
# We might need several API keys, to make a potentially huge number of requests
googlemapsapikeys = googlemapsapikeyjson['keys']
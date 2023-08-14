class USZIPCodeRepository:
    CACHE = {}

    def __init__(self, data_url_prefix = 'https://raw.githubusercontent.com/yyu/GeoJSON-US/master'):
        self.data_url_prefix = data_url_prefix
        self.geojson_url_prefix = f'{data_url_prefix}/perZIPgeojson'

        self.refresh_zipcode_latlons(f'{data_url_prefix}/ZIPCodesGazetteer.tsv')
        self.refresh_available_zipcodes(f'{data_url_prefix}/perZIPgeojson/all_zipcodes.txt')


    def refresh_zipcode_latlons(self, url):
        lines = [ line.decode('UTF8').strip() for line in urllib.request.urlopen(url).readlines() ]
        tsv = csv.DictReader(lines, delimiter='\t')
        self.gazetteer = dict((d['GEOID'], {'lat': float(d['INTPTLAT']), 'lon': float(d['INTPTLONG'])}) for d in tsv)


    def refresh_available_zipcodes(self, url):
        lines = [ zipcode.decode('UTF8').strip() for zipcode in urllib.request.urlopen(url).readlines() ]
        self.zipcode_list = lines[1:] # ignore the first line
        self.zipcode_set = set(self.zipcode_list)


    def make_url(self, zipcode):
        return f'{self.data_url_prefix}/perZIPgeojson/{zipcode[0]}/{zipcode[1]}/{zipcode[2]}/{zipcode}.json'


    def fetch_zipcode(self, zipcode):
        '''returns a (dict, err) tuple where err could be a string for error message or None'''

        url = self.make_url(zipcode)

        if url in USZIPCodeRepository.CACHE:
            return (USZIPCodeRepository.CACHE[url], None)

        try:
            s = urllib.request.urlopen(url).read()
        except urllib.error.URLError as e:
            return (None, 'failed to get ' + url, ':', e.reason)

        j = json.loads(s)

        USZIPCodeRepository.CACHE[url] = j

        return (j, None)


    def fetch_zipcodes(self, *zipcodes):
        d = {"type": "FeatureCollection", "features": []}

        available_zipcodes = set(zipcodes) & self.zipcode_set

        for z in available_zipcodes:
            j, err = self.fetch_zipcode(z)

            if j is not None:
                d['features'].append(j)

        return d

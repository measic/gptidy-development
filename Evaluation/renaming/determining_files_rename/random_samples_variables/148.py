variable_def = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in variable_def:
    data['sat_results'][c] = pd.to_numeric(data['sat_results'][c], errors='coerce')
data['sat_results']['sat_score'] = data['sat_results'][variable_def[0]] + data['sat_results'][variable_def[1]] + data['sat_results'][variable_def[2]]

def find_lat(loc):
    coords = re.findall('\\(.+, .+\\)', loc)
    lat = coords[0].split(',')[0].replace('(', '')
    return lat

def find_lon(loc):
    coords = re.findall('\\(.+, .+\\)', loc)
    lon = coords[0].split(',')[1].replace(')', '').strip()
    return lon
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(find_lat)
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(find_lon)
data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'], errors='coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'], errors='coerce')
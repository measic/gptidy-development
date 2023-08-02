cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
for c in cols:
    variable_def['sat_results'][c] = pd.to_numeric(variable_def['sat_results'][c], errors='coerce')
variable_def['sat_results']['sat_score'] = variable_def['sat_results'][cols[0]] + variable_def['sat_results'][cols[1]] + variable_def['sat_results'][cols[2]]

def find_lat(loc):
    coords = re.findall('\\(.+, .+\\)', loc)
    lat = coords[0].split(',')[0].replace('(', '')
    return lat

def find_lon(loc):
    coords = re.findall('\\(.+, .+\\)', loc)
    lon = coords[0].split(',')[1].replace(')', '').strip()
    return lon
variable_def['hs_directory']['lat'] = variable_def['hs_directory']['Location 1'].apply(find_lat)
variable_def['hs_directory']['lon'] = variable_def['hs_directory']['Location 1'].apply(find_lon)
variable_def['hs_directory']['lat'] = pd.to_numeric(variable_def['hs_directory']['lat'], errors='coerce')
variable_def['hs_directory']['lon'] = pd.to_numeric(variable_def['hs_directory']['lon'], errors='coerce')
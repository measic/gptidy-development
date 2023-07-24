import folium
import pandas as pd

# Import the Switzerland map (from the folio pylib notebook)
topo_geo = r'ch-cantons.topojson.json'

# Import our csv file with all of the values for the amounts of the grants 
grants_data = pd.read_csv('P3_Cantons_Sum.csv')
# grants_data['Approved Amount'] = grants_data['Approved Amount'].astype(int)

missing_cantons = pd.Series(['UR', 'OW', 'NW', 'GL', 'BL', 'AR', 'AI', 'JU'], name='Canton Shortname')
missing_cantons_zeros = pd.Series([0, 0, 0, 0, 0, 0, 0, 0], name='Approved Amount')
missing_cantons_df = pd.DataFrame([missing_cantons, missing_cantons_zeros]).T
grants_data_all_cantons = grants_data.append(missing_cantons_df)
grants_data_all_cantons = grants_data_all_cantons.reset_index(drop=True)

grants_data_all_cantons['Approved Amount'] = grants_data_all_cantons['Approved Amount'] / 10000000

grants_data_all_cantons
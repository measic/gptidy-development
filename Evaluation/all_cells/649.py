# We save the dictionary of cantons associated with universities
# Thus we won't need to make requests that have already been made to Google Maps next time we run this notebook !
with open('university_canton_dict.json', 'w') as fp:
    json.dump(university_canton_dict, fp, indent=4)
university_canton_dict
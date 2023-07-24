# We save the dictionary of cantons/institutions as well
with open('institution_canton_dict.json', 'w') as fp:
    json.dump(institution_canton_dict, fp, indent=4)
institution_canton_dict
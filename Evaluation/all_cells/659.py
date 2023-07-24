p3_grant_cantons_json = p3_grant_cantons.to_json()
with open('P3_cantons.json', 'w') as fp:
    json.dump(p3_grant_cantons_json, fp, indent=4)
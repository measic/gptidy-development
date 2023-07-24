with open(exportpath + "profile.json", "w") as fileobj:
    json.dump(profile_dict, fileobj, default = convert_invalid_values)
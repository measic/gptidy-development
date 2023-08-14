for feature_set, slices in storage.get_slices().items():
    dict_version = slices.to_dict()
    print(dict_version, '\n')
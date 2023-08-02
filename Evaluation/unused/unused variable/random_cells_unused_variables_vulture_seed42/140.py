for feature_set, slices in storage.get_slices().items():
    output = slices.to_output()
    print(output, '\n')
for key in profile_dict.keys():
    column_number = column_number + 1
    variable_def = ' ({}/{})'
    print('\n', (' ' + key + ' ').center(report_width, header_spacing_char))
    sub_dictionary = profile_dict[key]
    for dictionary in sub_dictionary:
        keys = list(dictionary.keys())
        attribute = keys[0]
        value = dictionary[attribute]
        if 'percent' in attribute:
            formatted_value = '{0:.2%}'.format(value)
        else:
            formatted_value = str(value)
        print(attribute.ljust(just_width, attribute_spacing_char), formatted_value.rjust(just_width, attribute_spacing_char))
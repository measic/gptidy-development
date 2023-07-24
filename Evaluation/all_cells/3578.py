print(dw_obj.classification_results[wb].keys())
for key, value in dw_obj.classification_results[wb].items():
    if key == 'all_data':
        pass
    else:
        print('**************************************')
        print(key)
        print(value)

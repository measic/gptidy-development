def set_above_one_value(x):
    if x > 1:
        return 1
    else:
        return x
dw_obj.water_body_indicator_df[wb]['EK'] = dw_obj.water_body_indicator_df[wb]['DIN']/dw_obj.water_body_indicator_df[wb]['REFERENCE_VALUE']
dw_obj.water_body_indicator_df[wb]['EK'] = dw_obj.water_body_indicator_df[wb]['EK'].apply(set_above_one_value)
dw_obj.water_body_indicator_df[wb]['EK']
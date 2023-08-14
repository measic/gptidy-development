def get_EK(x):
    y = x.DIN/x.REFERENCE_VALUE
    if y > 1:
        return 1
    else:
        return y

df = dw_obj.water_body_indicator_df[wb]
df['ek_value'] = df.apply(get_EK, axis = 1)
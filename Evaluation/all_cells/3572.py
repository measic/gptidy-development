temp = dw_obj.water_body_indicator_df[wb].dropna(subset = ['DIN', 'REFERENCE_VALUE']).copy(deep = True)
temp['ek'] = np.divide(temp.REFERENCE_VALUE,temp.DIN)
temp
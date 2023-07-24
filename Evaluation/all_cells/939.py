# Invert transform
inverted=list()
for i in range(len(differenced)):
    value=inverse_difference(series, differenced[i],len(series)-i)
    inverted.append(value)
inverted=pd.Series(inverted)  
print(inverted.head())
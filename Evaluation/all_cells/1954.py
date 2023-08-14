### set up data for modeling
X_5K = boston_clean[['Bib','Age','Official Time Duration', 'F', 'M', 'Temp (F)']]
y_5K = boston_clean['5K Duration'].values.reshape(-1, 1)
print(X_5K.shape, y_5K.shape)
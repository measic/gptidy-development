# Re-run the model with the Bib numbers as a feature and for the 5K, 10K 15K and 20K split times to predict Half marathon time

### set up data for modeling
X_Half = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration']]
y_Half = boston_clean['Half Duration'].values.reshape(-1, 1)
print(X_Half.shape, y_Half.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_Half, X_test_Half, y_train_Half, y_test_Half = train_test_split(X_Half, y_Half, random_state=29)
# X_train_Half.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_Half = LinearRegression()
model_Half.fit(X_train_Half, y_train_Half)

# Make predictions

predictions_Half = model_Half.predict(X_test_Half)

# Plot the residuals

plt.scatter(model_Half.predict(X_train_Half), model_Half.predict(X_train_Half) - y_train_Half, c="blue", label="Training Data")
plt.scatter(model_Half.predict(X_test_Half), model_Half.predict(X_test_Half) - y_test_Half, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_Half.min(), xmax=y_test_Half.max())
plt.title("Residual Plot Half Marathon")
plt.savefig('model_Half.png')
plt.show()

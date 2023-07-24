# Re-run the model with the Bib numbers as a feature and for the 5K, 10K 15K 20K 25K, half and 35K split times to predict 40K time

### set up data for modeling
X_40K = boston_clean[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration',  'Half Duration', '25K Duration', '30K Duration','35K Duration']]
y_40K = boston_clean['40K Duration'].values.reshape(-1, 1)
print(X_40K.shape, y_40K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_40K, X_test_40K, y_train_40K, y_test_40K = train_test_split(X_40K, y_40K, random_state=29)
# X_train_40K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_40K = LinearRegression()
model_40K.fit(X_train_40K, y_train_40K)

# Make predictions

predictions_40K = model_40K.predict(X_test_40K)

# Plot the residuals

plt.scatter(model_40K.predict(X_train_40K), model_40K.predict(X_train_40K) - y_train_40K, c="blue", label="Training Data")
plt.scatter(model_40K.predict(X_test_40K), model_40K.predict(X_test_40K) - y_test_40K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_40K.min(), xmax=y_test_40K.max())
plt.title("Residual Plot 40K")
plt.savefig('model_40k.png')
plt.show()

# Re-run the model with the Bib numbers as a feature and for the 5K, 10K 15K 20K 25K, half, 35K and 40K split times to predict Final time

### set up data for modeling
X_Final = boston_clean[['Bib', 'Age', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration','Half Duration', '25K Duration', '30K Duration', '35K Duration', '40K Duration']]
y_Final = boston_clean['Official Time Duration'].values.reshape(-1, 1)
print(X_Final.shape, y_Final.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_Final, X_test_Final, y_train_Final, y_test_Final = train_test_split(X_Final, y_Final, random_state=29)
# X_train_Final.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_Final = LinearRegression()
model_Final.fit(X_train_Final, y_train_Final)

# Make predictions

predictions_Final = model_Final.predict(X_test_Final)

# Plot the residuals

plt.scatter(model_Final.predict(X_train_Final), model_Final.predict(X_train_Final) - y_train_Final, c="blue", label="Training Data")
plt.scatter(model_Final.predict(X_test_Final), model_Final.predict(X_test_Final) - y_test_Final, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_Final.min(), xmax=y_test_Final.max())
plt.title("Residual Plot Final")
plt.savefig('model_Final.png')
plt.show()

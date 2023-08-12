# Re-run the model with ONLY female runners, and  features of the 5K, 10K 15K 20K 25K, half and 35K split times to predict 40K time

### set up data for modeling
X_F40K = boston_females[['Bib', 'Age','Official Time Duration', 'F', 'M', 'Temp (F)', '5K Duration', '10K Duration', '15K Duration', '20K Duration','Half Duration', '25K Duration', '30K Duration', '35K Duration']]
y_F40K = boston_females['40K Duration'].values.reshape(-1, 1)
print(X_F40K.shape, y_F40K.shape)

# split the data into test and train subsets

from sklearn.model_selection import train_test_split

X_train_F40K, X_test_F40K, y_train_F40K, y_test_F40K = train_test_split(X_F40K, y_F40K, random_state=29)
# X_train_F40K.head()

# Create a linear regression model and fit it to the training data

from sklearn.linear_model import LinearRegression
model_F40K = LinearRegression()
model_F40K.fit(X_train_F40K, y_train_F40K)

# Make predictions

predictions_F40K = model_F40K.predict(X_test_F40K)

# Plot the residuals

plt.scatter(model_F40K.predict(X_train_F40K), model_F40K.predict(X_train_F40K) - y_train_F40K, c="blue", label="Training Data")
plt.scatter(model_F40K.predict(X_test_F40K), model_F40K.predict(X_test_F40K) - y_test_F40K, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_F40K.min(), xmax=y_test_F40K.max())
plt.title("Residual Plot Female Runners 40K")
plt.savefig('model_F40K.png')
plt.show()

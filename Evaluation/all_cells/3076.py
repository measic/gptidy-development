# split data into training and testing subsets
train_features, test_features, train_outcome, test_outcome = train_test_split(
    modeling_df.drop(['DATE', 'HourlySkyConditions', 'REPORT_TYPE', 'join_time', 'actual_weather_delay', 'avg_delay'], axis=1),
    modeling_df.avg_delay,
    test_size=0.20
)

# Explore sizes of resulting training and testing sets
print('Training features shape: ' + str(train_features.shape))
print('Testing features shape: ' + str(test_features.shape))
print('Training outcomes shape: ' + str(train_outcome.shape))
print('Testing outcomes shape: ' + str(test_outcome.shape))

print(list(train_features))
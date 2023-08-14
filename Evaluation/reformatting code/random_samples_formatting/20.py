# Scale the input data
feature_copy[numeric_model_features] = scaler.transform(feature_copy[numeric_model_features])
feature_copy.head()
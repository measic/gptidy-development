# # To save the model without the training data, in order to make predictions without re-training the model
# # Source: https://www.geeksforgeeks.org/saving-a-machine-learning-model/

# import pickle
# from sklearn.externals import joblib 
  
# # Save the model as a pickle in a file 
# joblib.dump(model_5K, 'model_5K.pkl')
  
# # Load the model from the file 
# model_5K_from_joblib = joblib.load('model_5K.pkl')  
  
# # Use the loaded model to make predictions 
# model_5K_from_joblib.predict(X_test_5K) 
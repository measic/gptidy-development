# Contiue from the above
# Walk forward validation
history = [ x for x in train]
predictions=list()
for i in range(len(test)):
    #make prediction
    predictions.append(history[-1])
    # Observation
    history.append(test[i])
# report performance
rmse=np.sqrt(mean_squared_error(test,predictions))
print("RMSE: %.3f" % rmse)
#plotting this out
plt.plot(test)
plt.plot(predictions)
plt.show()
# This is simply the result of shifting the curve forward by 1 period
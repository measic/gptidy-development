gbrt_slow = GradientBoostingRegressor(max_depth=2, n_estimators=20, learning_rate=0.1, random_state=42, warm_start=True)

gbrt_slow.fit(X, y)
y_pred = gbrt_slow.predict(X)
print(gbrt_slow.loss_(y, y_pred))

gbrt_slow.fit(X, y)
y_pred = gbrt_slow.predict(X)

print(gbrt_slow.loss_(y, y_pred))
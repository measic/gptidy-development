# Train
log_clf_s = LogisticRegression(random_state=42)
rnd_clf_s = RandomForestClassifier(random_state=42)
svm_clf_s = SVC(random_state=42, probability=True)

rnd_clf_2 = RandomForestClassifier(random_state=42)

for p in [log_clf_s, rnd_clf_s, svm_clf_s]:
    p.fit(X_train_1, y_train_1)

log_clf_p = log_clf_s.predict(X_train_2)
rnd_clf_p = rnd_clf_s.predict(X_train_2)
svm_clf_p = svm_clf_s.predict(X_train_2)

held_out = np.column_stack((log_clf_p, rnd_clf_p, svm_clf_p))
rnd_clf_2.fit(held_out, y_train_2)
arbol = MiClasificadorArbol(max_depth=3)

accuracies_training = []
accuracies_validation = []
aucs_training = []
aucs_validation = []

X_dev_np = np.array(X_dev)
y_dev_np = np.array(y_dev).ravel()

X_eval_np = np.array(X_eval)
y_eval_np = np.array(y_eval).ravel()

arbol.fit(X_dev_np, y_dev_np)

#Generamos los 5 folds
kf = KFold(n_splits=5)

accuracy_train      = []
accuracy_validation = []
roc_train      = []
roc_validation = []

for train_index, test_index in kf.split(X_dev_np):
    #print("TRAIN:", train_index, "TEST:", test_index)
    kf_X_train, kf_X_test = X_dev_np[train_index], X_dev_np[test_index]
    kf_y_train, kf_y_test = y_dev_np[train_index], y_dev_np[test_index]
    
    # Entrenamos el arbol con el fold actual
    arbol.fit(kf_X_train, kf_y_train)
    
    # Testeamos contra el fold de test para calcular accuracy
    kf_y_pred     = arbol.predict(kf_X_test)
    kf_y_pred_dev = arbol.predict(kf_X_train)
        
    # Calculamos accuracy
    accuracy_validation.append(get_accuracy(kf_y_pred, kf_y_test) )
    accuracy_train.append(get_accuracy(kf_y_pred_dev, kf_y_train) )

    # Testeamos contra el fold de test para calcular el score roc
    kf_y_pred_proba     = arbol.predict_proba(kf_X_test)
    kf_y_pred_dev_proba = arbol.predict_proba(kf_X_train)
    
    # Calculamos roc score
    roc_train.append(sklearn.metrics.roc_auc_score(kf_y_train, get_positive_class_probabilities(kf_y_pred_dev_proba)))
    roc_validation.append(sklearn.metrics.roc_auc_score(kf_y_test, get_positive_class_probabilities(kf_y_pred_proba)))
    
df = pd.DataFrame(index=range(1,6))
df.index.name = "Permutación"
                  
df["Accuracy (training)"]   = accuracy_train      # cambiar por accuracies_training
df["Accuracy (validación)"] = accuracy_validation # cambiar por accuracies_validation
df["AUC ROC (training)"]    = roc_train           # cambiar por aucs_training
df["AUC ROC (validación)"]  = roc_validation      # cambiar por aucs_validation

display(HTML("<h3> TABLA 1 </h3>"))
display(df)

# Descomentar las siguientes líneas para graficar el resultado
# df.plot(kind="bar")
# plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))
# plt.show()
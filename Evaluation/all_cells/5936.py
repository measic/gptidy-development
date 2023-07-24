resultados_training   = []
resultados_validation = []

########################################################
np.random.seed(SEED)
for criterio in ["gini", "entropy"]:
     for altura in [3, 5, None]:
        
        arbol = MiClasificadorArbol(max_depth=altura, criterion=criterio)
        arbol.fit(X_dev_np, y_dev_np)
        
        #Entrenamiento
        y_pred = arbol.predict_proba(X_dev_np)
        resultados_training.append( sklearn.metrics.roc_auc_score(y_dev_np, get_positive_class_probabilities(y_pred)))
        
        #Validacion
        y_pred = arbol.predict_proba(X_eval_np)
        resultados_validation.append( sklearn.metrics.roc_auc_score(y_eval_np, get_positive_class_probabilities(y_pred)))
#########################################################

df = pd.DataFrame(index=range(0,6))

df["Altura máxima"] = [3, 5, "Inifinito"] * 2
df["Criterio de evaluación de corte"] = ["Gini"] * 3 + ["Ganancia de Información"] * 3
df["AUC ROC promedio (training)"]   = resultados_training# reemplazar por resultados_training
df["AUC ROC promedio (validación)"] = resultados_validation # reemplazar por resultados_validation

   
display(HTML("<h3> TABLA 2 </h3>"))
display(df)
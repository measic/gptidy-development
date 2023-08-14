#Auxiliares para correr randomized search
from scipy.stats import uniform
from scipy.stats import randint

def correr_randomized_y_mostrar(estimator, parameters, folds, top,  iteraciones=None):
    random_search = None
    
    if(iteraciones is None):
        random_search = RandomizedSearchCV(estimator, parameters, cv=folds, scoring='roc_auc')
    else:
        random_search = RandomizedSearchCV(estimator, parameters, cv=folds, scoring='roc_auc', n_iter=iteraciones)
        
    time_before = time.time()
    random_search.fit(X_dev_np, y_dev_np)
    time_after = time.time()
    runtime = (time_after - time_before) * 1000.0
    
    top_resultados(random_search, top)
    bot_resultados(random_search, top)
    
    return (runtime, random_search)

def verTiempo(original, random):
    display("########### Timepos ###########")
    display("original: {:f}".format(original))
    display("random: {:f}".format(random))
    display("diferencia: {:f}".format( np.absolute(original-random) ))
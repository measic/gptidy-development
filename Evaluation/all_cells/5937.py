import time

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

##############################################
################# Auxiliares #################
##############################################

def top_resultados(grid, top=5):
    print("Top {} combinaciones".format(top))
    df = pd.DataFrame(grid.cv_results_["params"])
    df["mean_score_validation"] = grid.cv_results_["mean_test_score"]
    df["mean_score_training"] = grid.cv_results_["mean_train_score"]
    display(df.sort_values(by="mean_score_validation", ascending=False).head(top))

def bot_resultados(grid, bot=5):
    print("Bot {} combinaciones".format(bot))
    df = pd.DataFrame(grid.cv_results_["params"])
    df["mean_score_validation"] = grid.cv_results_["mean_test_score"]
    df["mean_score_training"] = grid.cv_results_["mean_train_score"]
    display(df.sort_values(by="mean_score_validation", ascending=True).head(bot))
    
def correr_y_mostrar(estimator, parameters, folds, top):
    grid = GridSearchCV(estimator, parameters, cv=folds, scoring='roc_auc')
    time_before = time.time()
    grid.fit(X_dev_np, y_dev_np)
    time_after = time.time()
    top_resultados(grid, top)
    bot_resultados(grid, top)
    runtime = (time_after - time_before) * 1000.0 
    return (runtime, grid)

# Para usar en caso de tener probabilidades a priori
priors = [(0.1,0.9),(0.2,0.8),(0.3,0.7),(0.4,0.6),(0.5,0.5),(0.6,0.4),(0.7,0.3),(0.8,0.2),(0.9,0.1)]
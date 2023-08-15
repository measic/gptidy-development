parametersDecisionTree = {
    'criterion':['entropy','gini'],
    'max_depth':range(1,51)
}

(tiempo_decision_tree, grid_decision_tree) = correr_y_mostrar(
    DecisionTreeClassifier(),
    parametersDecisionTree,
    5,
    5
)

parametersDecisionTree2 = {
    'criterion':['entropy','gini'],
    'max_depth':range(1,51),
    'min_samples_split':range(2, 30)
}

(tiempo_decision_tree_2, grid_decision_tree_2) = correr_y_mostrar(
    DecisionTreeClassifier(),
    parametersDecisionTree2,
    5,
    5
)
parametersDecisionTree = {
    'criterion':['entropy','gini'],
    'max_depth':randint(1, 200)
}

(tiempo_random_decision_Tree, random_decision) = correr_randomized_y_mostrar(
    DecisionTreeClassifier(),
    parametersDecisionTree,
    5,
    5,
    100
)

verTiempo(tiempo_decision_tree, tiempo_random_decision_Tree)

parametersDecisionTree2 = {
    'criterion':['entropy','gini'],
    'max_depth':randint(1, 200),
    'min_samples_split':uniform(0, 1)
}

(tiempo_random_decision_Tree_2, random_decision_tree_2) = correr_randomized_y_mostrar(
    DecisionTreeClassifier(),
    parametersDecisionTree2,
    5,
    5,
    500
)

verTiempo(tiempo_decision_tree_2, tiempo_random_decision_Tree_2)
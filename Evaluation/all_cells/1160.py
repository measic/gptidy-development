#Q_training=PreProcess(Dream9_training,Dream9)
#Q_scoring=PreProcess(Dream9_scoring,Dream9)
Q_training_temp=pandas.read_csv('Qtraining.csv')
Q_training=Q_training_temp[Q_training_temp.keys()[1:]]
Q_training.index=list(Q_training_temp[Q_training_temp.keys()[0]])

Q_scoring_temp=pandas.read_csv('Qscoring.csv')
Q_scoring=Q_scoring_temp[Q_scoring_temp.keys()[1:]]
Q_scoring.index=list(Q_scoring_temp[Q_scoring_temp.keys()[0]])

Dependent=[v for v in Q_training.keys() if v not in Q_scoring.keys()]
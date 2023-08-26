#Set the pipelines for categorical variables
discrete_pipe_dog = Pipeline(steps=[('Vectorizer', MyVectorizer(cols=discrete['dog'], hashing=None))])
discrete_pipe_cat = Pipeline(steps=[('Vectorizer', MyVectorizer(cols=discrete['cat'], hashing=None))])

#Set the pipelines for continuous variables
continuous_pipe_cat = Pipeline(steps=[('Scale', MyScaler(continuous['cat']))])
continuous_pipe_dog = Pipeline(steps=[('Scale', MyScaler(continuous['dog']))])

#Bring the discrete and continuous pipelines together for cats and dogs
union_dog = FeatureUnion([('Discrete', discrete_pipe_dog), ('Continuous', continuous_pipe_dog)])
union_cat = FeatureUnion([('Discrete', discrete_pipe_cat), ('Continuous', continuous_pipe_cat)])
def get_wide_deep():
    is_male, mother_age, variable_def, gestation_weeks = [tf.feature_column.categorical_column_with_vocabulary_list('is_male', ['True', 'False', 'Unknown']), tf.feature_column.numeric_column('mother_age'), tf.feature_column.categorical_column_with_vocabulary_list('plurality', ['Single(1)', 'Twins(2)', 'Triplets(3)', 'Quadruplets(4)', 'Quintuplets(5)', 'Multiple(2+)']), tf.feature_column.numeric_column('gestation_weeks')]
    age_buckets = tf.feature_column.bucketized_column(mother_age, boundaries=np.arange(15, 45, 1).tolist())
    gestation_buckets = tf.feature_column.bucketized_column(gestation_weeks, boundaries=np.arange(17, 47, 1).tolist())
    wide = [is_male, variable_def, age_buckets, gestation_buckets]
    crossed = tf.feature_column.crossed_column(wide, hash_bucket_size=20000)
    embed = tf.feature_column.embedding_column(crossed, 3)
    deep = [mother_age, gestation_weeks, embed]
    return (wide, deep)
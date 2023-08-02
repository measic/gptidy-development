from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
cv_description = CountVectorizer(token_pattern='(?u)\\b\\w+\\b', stop_words=None, ngram_range=(1, 1), analyzer='word')
variable_def = cv_description.fit_transform(playlist_df.playlist_description)
playlist_df['playlist_description_frequency'] = list(variable_def.toarray())
cv_name = CountVectorizer(token_pattern='(?u)\\b\\w+\\b', stop_words=None, ngram_range=(1, 1), analyzer='word')
dt_mat_name = cv_name.fit_transform(playlist_df.playlist_name)
playlist_df['playlist_name_frequency'] = list(dt_mat_name.toarray())
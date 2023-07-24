# %%time

# we need a custom pre-processor to extract correct field,
# but want to also use default scikit-learn preprocessing (e.g. lowercasing)
default_preprocessor = CountVectorizer().build_preprocessor()


def build_preprocessor(field):
    field_idx = list(dataset.columns).index(field)
    # if field == 'playlist_pid': from IPython.core.debugger import set_trace; set_trace()
    return lambda x: default_preprocessor(x[field_idx])


vectorizer = FeatureUnion([
    (
        'track_artist_uri',
        CountVectorizer(
            ngram_range=(1, 1),
            token_pattern=r".+",
            stop_words=None,
            # max_features=50000,
            preprocessor=build_preprocessor('track_artist_uri'))),
    (
        'track_album_uri',
        CountVectorizer(
            ngram_range=(1, 1),
            token_pattern=r".+",
            stop_words=None,
            # max_features=50000,
            preprocessor=build_preprocessor('track_album_uri'))),
    (
        'track_uri',
        CountVectorizer(
            ngram_range=(1, 1),
            token_pattern=r".+",
            stop_words=None,
            # max_features=50000,
            preprocessor=build_preprocessor('track_uri'))),

    (
        'playlist_pid',
        CountVectorizer(
            ngram_range=(1, 1),
            token_pattern=r".+",
            stop_words=None,
            # max_features=50000,
            preprocessor=build_preprocessor('playlist_pid'))),

    ("playlist_name",
      CountVectorizer(
            ngram_range=(1, 1),
            token_pattern=r"(?u)\b\w+\b",
            stop_words=None,
            analyzer = 'word',
            # max_features=50000,
            preprocessor=build_preprocessor("playlist_name"))),
    
    ("playlist_description",
      CountVectorizer(
            ngram_range=(1, 1),
            token_pattern=r"(?u)\b\w+\b",
            stop_words=None,
            analyzer = 'word',
            # max_features=50000,
            preprocessor=build_preprocessor("playlist_description"))),
#     (
#         'track_pos',
#         CountVectorizer(
#             ngram_range=(1, 1),
#             token_pattern=r".+",
#             stop_words=None,
#             # max_features=50000,
#             preprocessor=build_preprocessor('track_pos'))),

    ('track_duration_ms',
     ItemSelector(list(dataset.columns).index('track_duration_ms'))),
])
X_train = vectorizer.fit_transform(data_train.values)
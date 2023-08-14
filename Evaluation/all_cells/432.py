import nltk
import string
#nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')
ignored_words = [
    'music', 'songs', 'playlist', 'good', 'jams', 'mix', 'lit', 'best',
    'stuff', 'quot', 'like', 'one', 'amp', 'get', 'make', 'new', 'know',
    'really', 'back', 'day', 'days', 'little', 'things', 'great', 'everything',
    'jamz', 'tunes', 'artist', 'song', 'top', 'listen', 'favorite', 'bops',
    'description', 'top', 'ever', 'mostly', 'enjoy', 'bunch', 'track',
    'tracks', 'collection', 'need', 'every', 'favorites', 'may', 'got',
    'right', 'let', 'better', 'made'
]


def word_cleanup(df_col):
    df_col = df_col.apply(lambda x: x.lower())
    df_col = df_col.str.replace('[^a-z]+', ' ')
    df_col = df_col.apply(
        lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
    df_col = df_col.apply(lambda x: ' '.join([word for word in x.split() if word not in (ignored_words)]))
    df_col = df_col.str.replace(r'\b\w{1,2}\b', '').str.replace(r'\s+', ' ')
    return df_col


playlist_df.playlist_description = word_cleanup(
    playlist_df.playlist_description)
playlist_df.playlist_name = word_cleanup(playlist_df.playlist_name)

#playlist_df.playlist_name = playlist_df.playlist_name.apply(lambda x: x.lower())
#playlist_df.playlist_name = playlist_df.playlist_name.str.replace('[^a-z]+', ' ')
#playlist_df.playlist_name = playlist_df.playlist_name.apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
scaled_movies = list(map(lambda movie: {
    'title': movie['title'],
    'budget': round(movie['budget'] / 1000000, 0),
    'domgross': round(movie['domgross'] / 1000000, 0)
}, movies))
scaled_movies[0]
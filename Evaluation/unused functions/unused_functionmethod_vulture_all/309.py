class ReviewsJason(object):
    def __init__(self,type_movie,hate_love):
        self.type_movie = type_movie
        self.hate_love = hate_love
    
    def export(self):
        reviews = [getReviewPerMovie(i).category(self.hate_love) for i in getMovieByGendre().gendre(self.type_movie)]
        json_name = self.type_movie + '_'+self.hate_love + '_reviews_100'+ '.json'
        
        with open(json_name, 'w') as fp:
            json.dump(reviews, fp)
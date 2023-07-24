class getMovieByGendre(object):
    def __init__(self):
        self.site = 'http://www.imdb.com/search/title?' 
        
    def gendre(self,type_movie):

        #type_movie could be  Action,Adventure,Animation,Biography,Comedy,Crime,Documentary,
        #Drama,Family,Fantasy,Film-Noir,History,Horror,Music,Musical,Mystery,Romance,Sci-Fi,
        #Short,Sport,Thriller,War,Western
        
        reference_list = []
        for i in range(0,2):
            link = self.site + 'genres=' + type_movie + '&page='+ str(i)
            html = requests.get(link)
            soup = BeautifulSoup(html.text,"html.parser")   
            for reference in soup.find_all("div", {"class": "lister-item-image float-left"}):
                reference_list.append(reference.find('img',alt = True).get('data-tconst'))
            return reference_list 
        
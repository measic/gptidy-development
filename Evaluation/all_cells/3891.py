class getReviewPerMovie(object):
    def __init__(self,movieNumber):
        self.site = 'http://www.imdb.com/title/'+str(movieNumber)+'/reviews'
        self.movie_no = movieNumber
        
    def getLength(self,type_re):
        first_page = self.site +'?filter='+ type_re + ';filter='+ type_re +';start='+'0'
        html_l = requests.get(first_page)
        soup_l = BeautifulSoup(html_l.text,"html.parser")   
        tbl = soup_l.findAll('table')[1]
        row_n = tbl.find_all('tr')
        str_len = row_n[0].find_all('td')[0].text
        regex = r"(Page).(\d).(of).(\d*)(.+)"
        len_review = re.sub(regex, '\\4',str_len)
        return(len_review)
    
    def category(self,ca_re):
        reviews = []
        rev=[]
        try:        
            print(self.movie_no)
            page_length = int(self.getLength(str(ca_re)))
         
            for i in range(0,page_length):

                link= self.site +'?filter='+ ca_re + ';filter='+ ca_re +';start='+ str(i*10)
                print(link)
                html_link = requests.get(link)
                soup = BeautifulSoup(html_link.text,"html.parser")   
                review_soup = soup.find("div", {"id": "tn15content"})

                for div_re in review_soup.find_all('div'):
                    user_info_dict = {}
                    for user_info in div_re.find_all('img',alt=True):
                        user_info_dict['rating']=user_info.get('alt')
                        user_info_dict['author']=re.sub(r"(/user/)(ur\d+)(/)",'\\2',user_info.a.get('href'))
                        user_info_dict['title']=div_re.h2.text
                        user_info_dict['movie']=self.movie_no
                        if ca_re == 'love':
                            user_info_dict['categorie']='postive'
                        else:
                            user_info_dict['categorie']='negative'
                        if user_info.small is not None:
                            
                            reg = r"(<small>)(\d+)( out of )(\d+)(.+)"
                            user_info_dict['usefulness'] = re.sub(reg,'\\2/\\4',str(div_re.small))
                            reviews.append(user_info_dict)
                            #print(user_info_dict)

                for re_text in review_soup.find_all('p'):
                    review_text = {}
                    if re_text.getText() not in ['*** This review may contain spoilers ***',
                                                 'Add another review']:
                        review_text['review'] =re_text.get_text().replace('\n',' ')
                        rev.append(review_text)

            for i in range(0,len(reviews)):
                if len(reviews) == len(rev):
                    reviews[i]['review'] = rev[i]['review']
                else:
                    print('the length of the user info and review is not the same','...\n',
                         'user info has length: ',str(len(reviews)),'...\n',
                          'review has length: ',str(len(rev)),'...\n')

            return reviews


                
        except ValueError:
            pass
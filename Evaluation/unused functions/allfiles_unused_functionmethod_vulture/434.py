class Hmm(object):
    """
    Stores counts for n-grams and emissions. 
    """

    def __init__(self, n=3):
        assert n>=2, "Expecting n>=2."
        self.n = n
        self.emission_counts = defaultdict(int)
        self.ngram_counts = [defaultdict(int) for i in xrange(self.n)]
        self.all_states = set()
        self.count_y = dict() 
        #[('O', 0), ('I-MISC', 0), ('I-PER', 0), ('I-ORG', 0), ('I-LOC', 0), ('B-MISC', 0), ('B-PER', 0), ('B-ORG', 0), ('B-LOC', 0)])
        self.count_xy = dict()
        self.trigram_counts = dict()
        self.bigram_counts = dict()
        

    def train(self):
        """
        Count n-gram frequencies and emission probabilities from a corpus file.
        """
        ngram_iterator = \
            get_ngrams(sentence_iterator(simple_conll_corpus_iterator()), self.n)

        for ngram in ngram_iterator:
            #Sanity check: n-gram we get from the corpus stream needs to have the right length
            assert len(ngram) == self.n, "ngram in stream is %i, expected %i" % (len(ngram, self.n))

            tagsonly = tuple([ne_tag for word, ne_tag in ngram]) #retrieve only the tags            
            for i in xrange(2, self.n+1): #Count NE-tag 2-grams..n-grams
                self.ngram_counts[i-1][tagsonly[-i:]] += 1
            
            if ngram[-1][0] is not None: # If this is not the last word in a sentence
                self.ngram_counts[0][tagsonly[-1:]] += 1 # count 1-gram
                self.emission_counts[ngram[-1]] += 1 # and emission frequencies

            # Need to count a single n-1-gram of sentence start symbols per sentence
            if ngram[-2][0] is None: # this is the first n-gram in a sentence
                self.ngram_counts[self.n - 2][tuple((self.n - 1) * ["*"])] += 1
    
    def calc_count_xy_y(self):
        
        for word, ne_tag in self.emission_counts:
            count = self.emission_counts[(word,ne_tag)]
            label = ne_tag
            if label in self.count_y:
                self.count_y[label] = self.count_y[label]+int(float(count))
            else:
                self.count_y.update({label:count})

            if word in self.count_xy:
                self.count_xy[word].update({label : count})
            else:
                self.count_xy[word] = {label : count}

    def calc_transition_count(self,printngrams=[1,2,3]):
        
        for n in printngrams:            
                for ngram in self.ngram_counts[n-1]:
                    count = self.ngram_counts[n-1][ngram]
                    ngramstr = " ".join(ngram)
                    if (n == 2):
                        self.bigram_counts[ngramstr] = count
                    elif (n == 3):
                        self.trigram_counts[ngramstr] = count
                            


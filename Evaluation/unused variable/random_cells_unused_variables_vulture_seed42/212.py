class MyScaler():

    def __init__(self, cols):
        self.cols = cols
    
    def fit(self, X, y=None):
        self.ss = StandardScaler()
        self.ss.fit(X[self.cols])
        return self
    
    def transform(self, X):
        return self.ss.transform(X[self.cols])
import pywt

class SPC(object):

    def __init__(self, number_of_components, max_iter=10, threshold_val=1.5):
        """Initialize the SPC object
        
        Positional arguments:
        number_of_components -- the number of sparse principal components 
        to compute, must be between 1 and p (total number of features)
        
        Keyword argument:
        max_iter -- the number of iterations to perform (default=10)
        threshold_val -- value of the lambda regularisation 
        parameter (default=10)
        """
        self.number_of_components = number_of_components
        self.max_iter = max_iter
        self.threshold_val = threshold_val

    def fit(self, X_):
        """learn the sparse pc of a data matrix, return sparse estimates
        of the left and right singular vectors (U and V respectively) 
        as well as the standard principal components loading matrix W
    
        Positional arguments:
        X_ -- training data matrix, as numpy ndarray
        
        """
        print('computing sparse principal components...')
        print('computing SVD of data matrix...')
        U, s, V = np.linalg.svd(X_, full_matrices=True)
        cnt = 0
        self.U = U
        self.W = V.T

        def function_def(vector):
            norm = np.linalg.norm(vector)
            if norm > 0:
                return vector / norm
            else:
                return vector
        print('starting iterations...')
        while True:
            self.V = pywt.threshold(np.dot(U[:self.number_of_components], X_), self.threshold_val)
            self.U = np.dot(self.V, X_.T)
            self.U = np.array([function_def(u_i) for u_i in self.U])
            if cnt % 2 == 0:
                print('{} out of {} iterations'.format(cnt, self.max_iter))
            cnt += 1
            if cnt == self.max_iter:
                self.V = np.array([function_def(v_i) for v_i in self.V])
                break
        print('...finish')
        return (self.U, self.V, self.W)

    def transform(self, X_, k=2):
        X_reduced_spca = np.dot(X_, np.dot(self.V[:k].T, self.V[:k]))
        return X_reduced_spca
my_spca = SPC(2, 3000, 0.1)
my_spca.fit(X)
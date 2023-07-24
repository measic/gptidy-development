class BlackScholes(EuropeanOption):

    def __init__(self, option_type, S0, strike, T, r, div, sigma):
        EuropeanOption.__init__(self, option_type, S0, strike, 
                                T, r, div, sigma, 'BlackScholes')
        
        d1 = ((np.log(self.S0 / self.strike) + 
              (self.r - self.div + 0.5 * (self.sigma ** 2)) * self.T) / 
              float(self.sigma * np.sqrt(self.T)))
        d2 = float(d1 - self.sigma * np.sqrt(self.T))
        self.Nd1 = norm.cdf(d1, 0, 1)
        self.Nnd1 = norm.cdf(-d1, 0, 1)
        self.Nd2 = norm.cdf(d2, 0, 1)
        self.Nnd2 = norm.cdf(-d2, 0, 1)
        self.pNd1 = norm.pdf(d1, 0, 1)
        
    @property
    def value(self):
        if self.option_type == 'call':
            value = (self.S0 * np.exp(-self.div * self.T) * self.Nd1 -
                     self.strike * np.exp(-self.r * self.T) * self.Nd2)
        else:
            value = (self.strike * np.exp(-self.r * self.T) * self.Nnd2 -
                     self.S0 * np.exp(-self.div * self.T) * self.Nnd1)
        return value
    
    @property
    def delta(self):
        if self.option_type == 'call':
            delta = np.exp(-self.div * self.T) * self.Nd1
        else:
            delta = np.exp(-self.div * self.T) * (self.Nd1 - 1)
        return delta
class EuropeanOption(object):
    """ Abstract Class for European options. Partially implemented.
    S0 : float : initial stock/index level
    strike : float : strike price
    T : float : time to maturity (in year fractions)
    r : float : constant risk-free short rate
    div :    float : dividend yield
    sigma :  float : volatility factor in diffusion term
    model: str: name of the model for the pricing"""
    __metaclass__ = ABCMeta

    def __init__(self, option_type, S0, strike, T, r, div, sigma, model):
        try:
            self.option_type = option_type
            assert isinstance(option_type, str)
            self.S0 = float(S0)
            self.strike = float(strike)
            self.T = float(T)
            self.r = float(r)
            self.div = float(div)
            self.sigma = float(sigma)
            self.model = str(model)
        except ValueError:
            print('Error passing Options parameters')
        models = ['BlackScholes', 'MonteCarlo', 'BinomialTree', 'TrinomialTree', 'FFT', 'PDE']
        if model not in models:
            raise Exception('Error: Model unknown')
        option_types = ['call', 'put']
        if option_type not in option_types:
            raise ValueError("Error: Option type not valid. Enter 'call' or 'put'")
        if S0 < 0 or strike < 0 or T <= 0 or (r < 0) or (div < 0) or (sigma < 0):
            raise ValueError('Error: Negative inputs not allowed')
        self.discount = np.exp(-self.r * self.T)

    def getmodel(self):
        return self.model

    def __str__(self):
        return 'This European Option is priced using {0}'.format(self.getmodel())

    @abstractmethod
    def function_def(self):
        pass

    @abstractmethod
    def delta(self):
        pass
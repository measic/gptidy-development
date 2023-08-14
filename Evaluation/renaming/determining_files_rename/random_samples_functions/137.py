class MonteCarlo(EuropeanOption):

    def __init__(self, simulations, option_type, S0, strike, T, r, div, sigma, antithetic=True, moment_matching=True, fixed_seed=True):
        EuropeanOption.__init__(self, option_type, S0, strike, T, r, div, sigma, 'MonteCarlo')
        try:
            self.antithetic = bool(antithetic)
            self.moment_matching = bool(moment_matching)
            self.fixed_seed = bool(fixed_seed)
            if self.simulations > 0:
                self.simulations = int(simulations)
            else:
                raise ValueError("Simulation's number has to be positive integer")
        except:
            raise ValueError('Problem assigning types in MC arguments')

    def simulation_terminal(self, seed=1234567890):
        if self.fixed_seed:
            assert isinstance(seed, int)
            np.random.seed(seed)
        if self.antithetic:
            brownian = np.random.standard_normal(size=int(np.ceil(self.simulations / 2.0)))
            brownian = np.concatenate((brownian, -brownian))
        else:
            brownian = np.random.standard_normal(size=self.simulations)
        if self.moment_matching:
            brownian = brownian - np.mean(brownian)
            brownian = brownian / np.std(brownian)
        price_terminal = self.S0 * np.exp((self.r - self.div - 0.5 * self.sigma ** 2) * self.T + self.sigma * np.sqrt(self.T) * brownian)
        return price_terminal

    def function_def(self):
        price_terminal = self.simulation_terminal()
        if self.option_type == 'call':
            payoff = np.maximum(price_terminal - self.strike, 0)
        else:
            payoff = np.maximum(self.strike - price_terminal, 0)
        return payoff

    @property
    def value(self):
        payoff = self.generate_payoffs()
        return self.discount * np.sum(payoff) / float(len(payoff))

    @property
    def delta(self):
        value_terminal = np.array(self.simulation_terminal() / float(self.S0))
        payoff = self.generate_payoffs()
        delta = np.zeros(len(payoff))
        delta[np.nonzero(payoff)] = value_terminal[np.nonzero(payoff)]
        return self.discount * np.sum(delta) / float(len(payoff))
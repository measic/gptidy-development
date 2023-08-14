def marginal(self):
    
    marginal = np.prod(np.array(list(self.in_msgs.values())), axis=0)
    marginal /= np.sum(marginal)
    return marginal

Variable.marginal = marginal

def unnormalized_log_marginal(self):
    unnormalized_log_marginal = np.sum(np.array(list(self.in_msgs.values())), axis=0)
    
    return unnormalized_log_marginal + np.log(self.observed_state)

Variable.unnormalized_log_marginal = unnormalized_log_marginal

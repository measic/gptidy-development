with model:
    yes_responses = pm.Binomial("number_cheaters", 100, p_skewed, observed=35)
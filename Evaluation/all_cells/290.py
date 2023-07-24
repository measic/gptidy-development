## Bayesian prior parameters
alpha_0 = 1
beta_0  = 1

## Set parameters for simulating data
start_date    = as.Date('2017-01-01')  # start date of tests
test_duration = 60    # length of tests in days
num_tests     = 3     # how many test variants excluding default
counts        = 10000 # total view in each group
prob_list     = c(0.02, 0.04, 0.025, 0.02) # true proportion of Test0, Test1, Test2, Test3
Conf_alpha    = 0.1   # Confidence level
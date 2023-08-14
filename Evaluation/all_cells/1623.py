regression = RocketRegression('rocket_break_v6_enable_multip_stocks.json')

regression_end='2019-08-30'
scale=60
process_num=24

evaluation_df = regression.start_regression(scale,regression_end,process_num)
evaluation_df.describe()
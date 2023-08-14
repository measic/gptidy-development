temp_df = pd.DataFrame(np.random.randn(10, 3), columns=['A', 'B', 'C'],
...                   index=pd.date_range('1/1/2000', periods=10))
temp_df.iloc[3:7] = np.nan
temp_df.describe()
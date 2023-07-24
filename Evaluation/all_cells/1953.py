# convert male/female to 0/1s

boston_mf=pd.get_dummies(boston['M/F'])

# join the two dataframes

boston_join=pd.concat([boston, boston_mf], axis=1) 

boston_join.head()
# boston_join[['5K','10K','15K','20K','Half', '25K','30K']]
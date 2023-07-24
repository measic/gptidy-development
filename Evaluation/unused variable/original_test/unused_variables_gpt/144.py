stage_analyze=pd.DataFrame(columns=['dog_stage','number','rating','retweet','favorite'])
stage_analyze['dog_stage']=['doggo','floofer','pupper','puppo']
for each_stage in stage_analyze.dog_stage:
    stage_df=df[df.dog_stage==each_stage]
    stage_analyze.loc[stage_analyze.dog_stage== each_stage,'number']=stage_df.shape[0]
    stage_analyze.loc[stage_analyze.dog_stage== each_stage,'rating']=stage_df['rating'].mean()
    stage_analyze.loc[stage_analyze.dog_stage== each_stage,'retweet']=stage_df['retweet_count'].mean()
    stage_analyze.loc[stage_analyze.dog_stage== each_stage,'favorite']=stage_df['favorite_count'].mean()
    
    
stage_analyze[['dog_stage','number']].plot(x='dog_stage',kind='bar',title='Dog Stages Distribution')

stage_analyze[['dog_stage','retweet','favorite']].plot(x='dog_stage',kind='bar',title='Dog Stage-Retweet&Favorite Analysis')

stage_analyze[['dog_stage','rating']].plot(x='dog_stage',kind='bar',title='Dog Stage-Rating Analysis')
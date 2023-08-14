twitter_archive_clean.loc[twitter_archive_clean.name.str.islower(),'name']='None'
twitter_archive_clean.name=twitter_archive_clean.name.replace('None',np.nan)
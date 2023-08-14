twitter_archive_clean.loc[twitter_archive_clean.tweet_id==786709082849828864,'rating']=1.0
twitter_archive_clean.loc[twitter_archive_clean.tweet_id==778027034220126208,'rating']=1.1
twitter_archive_clean.loc[twitter_archive_clean.tweet_id==680494726643068929,'rating']=1.1
twitter_archive_clean=twitter_archive_clean[twitter_archive_clean.rating<2]
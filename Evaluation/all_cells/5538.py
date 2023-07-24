twitter_archive_clean=twitter_archive_clean[twitter_archive.tweet_id.notnull()]
twitter_archive_clean=twitter_archive_clean[twitter_archive.retweeted_status_id.isnull()]
twitter_archive_clean=twitter_archive_clean.drop(['retweeted_status_id','retweeted_status_user_id','retweeted_status_timestamp'],axis=1)
rep_id=twitter_archive_clean.tweet_id[twitter_archive_clean.in_reply_to_user_id.notnull()]
twitter_archive_clean.in_reply_to_user_id=twitter_archive_clean.in_reply_to_user_id.astype(str)
twitter_archive_clean.in_reply_to_status_id=twitter_archive_clean.in_reply_to_status_id.astype(str)
for each_id in rep_id:
    tweet_info=api.get_status(each_id,tweet_mode='extended')
    twitter_archive_clean.loc[twitter_archive_clean.tweet_id==each_id, 'in_reply_to_user_id']=str(tweet_info.in_reply_to_user_id)
    twitter_archive_clean.loc[twitter_archive_clean.tweet_id==each_id, 'in_reply_to_status_id']=str(tweet_info.in_reply_to_status_id)

twitter_archive_clean.in_reply_to_user_id=twitter_archive_clean.in_reply_to_user_id.replace('nan',np.nan)
twitter_archive_clean.in_reply_to_status_id=twitter_archive_clean.in_reply_to_status_id.replace('nan',np.nan)
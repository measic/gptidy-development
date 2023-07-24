img_predictions_clean.tweet_id=img_predictions_clean.tweet_id.astype(str)
twitter_archive_clean = twitter_archive_clean.merge(img_predictions_clean, on='tweet_id', how='inner')
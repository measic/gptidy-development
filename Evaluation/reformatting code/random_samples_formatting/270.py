pd.set_option('display.max_colwidth', -1)
twitter_archive_clean.loc[twitter_archive_clean.rating_denominator!=10,['tweet_id','text','rating_numerator','rating_denominator']]
twitter_archive_clean=twitter_archive_clean[twitter_archive_clean.tweet_id != 810984652412424192]

twitter_archive_clean.loc[twitter_archive_clean.tweet_id==740373189193256964,['rating_numerator','rating_denominator']]=[14,10]
twitter_archive_clean.loc[twitter_archive_clean.tweet_id==722974582966214656,['rating_numerator','rating_denominator']]=[13,10]
twitter_archive_clean.loc[twitter_archive_clean.tweet_id==716439118184652801,['rating_numerator','rating_denominator']]=[11,10]
twitter_archive_clean.loc[twitter_archive_clean.tweet_id==682962037429899265,['rating_numerator','rating_denominator']]=[10,10]
twitter_archive_clean.loc[twitter_archive_clean.tweet_id==666287406224695296,['rating_numerator','rating_denominator']]=[9,10]

twitter_archive_clean['rating']=twitter_archive_clean.rating_numerator/twitter_archive_clean.rating_denominator
twitter_archive_clean=twitter_archive_clean.drop(['rating_numerator','rating_denominator'],axis=1)

twitter_archive_clean.loc[twitter_archive_clean.rating>2,['tweet_id','text','rating']]
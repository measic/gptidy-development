all_df = pd.concat([old_df, f18_df], verify_integrity=True, ignore_index=True, sort=True)
all_df.head()
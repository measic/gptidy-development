merged = pd.merge_asof(fixed.sort_index(), e_series, on='ut')
merged.head()
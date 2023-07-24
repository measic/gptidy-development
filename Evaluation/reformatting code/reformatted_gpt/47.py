provi = providence_x_train[providence_x_train['word'].isin(brent_words)]
provi = provi.reset_index(drop=True)

brent = brent_x_train[brent_x_train['word'].isin(provi_words)]
brent = brent.reset_index(drop=True)

print("\nFeature correlations between two data samples (Brent corpus and Providence corpus) \n")
print(brent.corrwith(provi, drop=True))
#save
with open("data.pkl", "wb") as file:
    pickle.dump([padded_conv, norare_dico, tokens], file)
    
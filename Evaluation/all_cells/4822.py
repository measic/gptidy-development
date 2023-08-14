tokens = copy.deepcopy(norare_dico)


#Then tokenization of the dictionary
for i,w in enumerate(norare_dico,1):
    tokens[w] = i

# Add the 3 artifical words
tokens["PADD"] = 0
tokens["START"] = i + 1
tokens["STOP"] = i + 2
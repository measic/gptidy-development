def translate(s, dico_to_token, to_token=True):
    new_s = []
    if to_token:
        for w in s:
            token = dico_to_token[w]
            new_s.append(token)
    else:
        
        inverted_dico = {token: word for word, token in dico_to_token.items()}
        
        for t in s:
            word = inverted_dico[t]
            if word in ["PADD","START","STOP"]:
                continue
            else:
                new_s.append(word)

    return new_s
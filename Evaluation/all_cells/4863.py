#Translate sentences to list of integers
trans_X = []
trans_T = []

for s_x, s_t in zip(X,T):
        
    words_x = s_x.split(" ")
    words_t = s_t.split(" ")
    new_s_x = translate(words_x,tokens,to_token=True)
    new_s_t = translate(words_t,tokens,to_token=True)

    # Add to every sentences of answer START and STOP tokens
    new_t = [tokens["START"]] + new_s_t
    new_t.append(tokens["STOP"])
    trans_X.append(new_s_x)
    trans_T.append(new_t)
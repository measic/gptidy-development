for k in range(10):
    print(k+1)
    temperature = [0.5, 1.]
    reverse_tokens = {v:k for k,v in tokens.items()}

    idx = np.random.choice(len(T_))
    base_context = X_[idx,:]
    base_answer = padded_T[idx,:-1]
    base_sentence = ["START", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD"]
    
    for t in temperature:
        for i in range(len(base_answer)):

            trans_sentence = np.array(translate(base_sentence,tokens,True))
            pred_prob = Chatbot.predict([base_context.reshape(1,-1),trans_sentence.reshape(1,-1)])

            w_token = sample(pred_prob[0][i], temperature=t)
            word = reverse_tokens[w_token]

            if word == "STOP":
                break
            else:
                base_sentence[i] = word
        
        print("\nTemperature:", t)
        print("context:", "".join([w+" " for w in translate(base_context,tokens,False)]))
        print("generated answer:", "".join([w+" " for w in base_sentence if w != "PADD"]))
        print("real answer:", "".join([w+" " for w in translate(base_answer,tokens,False)]))

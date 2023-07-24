base_sentence1 =["he", "often", "plays", "tennis", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD"]
    
base_sentence2 =["we", "walked", "the", "dog", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD"]

sentences = [base_sentence1, base_sentence2]

reverse_tokens = {v:k for k,v in tokens.items()}

n_continuation = 10

for j,s in enumerate(sentences):
    for n in range(n_continuation):
        for i in range(4,len(sentences[j])):

            trans_sentence = np.array(translate(sentences[j],tokens,True))
            pred_prob = best_model.predict(trans_sentence.reshape(1,-1))
            w_token = sample(pred_prob[0][i], temperature=1.)
            word = reverse_tokens[w_token]

            if word == "STOP":
                break
            else:
                sentences[j][i] = word

        print("".join([w+" " for w in sentences[j] if w != "PADD"]))
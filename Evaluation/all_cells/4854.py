temperature = [0., 0.25, 0.5, 0.75, 1., 1.5, 2.]
f, ax = plt.subplots(7,1, figsize=(30,50))
for j,t in enumerate(temperature):
    
    base_sentence =["START", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD", "PADD",
                     "PADD", "PADD", "PADD", "PADD"]

    reverse_tokens = {v:k for k,v in tokens.items()}
    proba_matrix = np.zeros((24,2969))
    old_token = np.zeros(24, dtype=int)

    for i in range(len(base_sentence)):
        
        
        trans_sentence = np.array(translate(base_sentence,tokens,True))
        pred_prob = best_model.predict(trans_sentence.reshape(1,-1))

        w_token = sample(pred_prob[0][i], temperature=t)
        
        old_token[i] = w_token
        
        proba_matrix[i,:] = pred_prob[0][i]

        word = reverse_tokens[w_token]
        if word == "STOP":
            break
        else:
            base_sentence[i] = word
    #print(base_sentence)
    im = ax[j].imshow(proba_matrix[:,old_token], cmap="Greys")
    ax[j].set_xlabel(base_sentence)
    ax[j].set_ylabel("Timestep")
    ax[j].invert_yaxis()
    ax[j].set_title("with temperature: {t}".format(t=t))
    f.colorbar(im, ax=ax[j], label="probability")  
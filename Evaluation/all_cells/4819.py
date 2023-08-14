# if a word occur less than n times, we remove the sentence of the conversations.

n = 20
norare_dico = {k: v for k,v in dico.items() if v > n}
norare_conv = copy.deepcopy(conv)

for i,c in enumerate(conv):
    for s in c:
        words = s.split(" ")
        for w in words:
            if s not in norare_conv[i]:
                break
            else:
                if w not in norare_dico.keys():
                    norare_conv[i].remove(s)

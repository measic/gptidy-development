#Get the length of the filtered dictionary (where frequency of the word == 1)
num_word_1 = len({k: v for k,v in dico.items() if v == 1})
num_word_tot = len(dico)
"{un} / {tot} words appearing only once".format(un=num_word_1, tot=num_word_tot)
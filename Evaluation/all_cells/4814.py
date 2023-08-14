dico = {}

for c in conv:
    for s in c:
        words = s.split(" ")
        for w in words:
            if w in dico.keys():
                dico[w] += 1
            else:
                dico[w] = 1

sorted_list = sorted(dico.items(), key = lambda x: x[1], reverse=True)
# Display top 10 most frequent words used in these conversations.
print(sorted_list[:10])
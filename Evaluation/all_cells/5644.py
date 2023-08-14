# use Dataset.stream() (word, tag) samples for the entire corpus
d1 = defaultdict(list)
print("\nStream (word, tag) pairs:\n")
for i, pair in enumerate(data.stream()):
    print("\t", i, pair[0], pair[1])
    d1[pair[1]].append(pair[0])
    if i > 20: break

print(d1)
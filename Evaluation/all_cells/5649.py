d1 = defaultdict(list)
d2 = defaultdict(list)
for i, pair in enumerate(data.stream()):
    d1[pair[1]].append(pair[0])
    if i > 1000: break

print(d1.keys())
#print(d1.items())

for key in d1.keys():
    d2[key] = Counter(d1[key])
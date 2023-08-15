d1 = defaultdict(list)
for i, pair in enumerate(data.stream()):
    d1[pair[1]].append(pair[0])
    if i > 1000: break

print(len(d1))
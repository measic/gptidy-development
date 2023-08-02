intersections = collections.defaultdict(list)
for s in subsets:
    intersections[len(set(subset).intersection(set(s[0])))].append(s)
max_subsets = max(intersections.items())
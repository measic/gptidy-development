tags = (tag for i, (word, tag) in enumerate(data.training_set.stream()))
words = (word for i, (word, tag) in enumerate(data.training_set.stream()))

d2 = pair_counts(words, tags)

print(d2['time'])
print(d2['time'].most_common(1))
print(d2['time'].most_common(1)[0])
print(d2['time'].most_common(1)[0][0])
#print(d2.values())
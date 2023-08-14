## (Optional) TODO: Report the performance of another  
## face detection algorithm on the LFW dataset
### Feel free to use as many code cells as needed.

## Our data files
human_files_short = human_files[:100]
dog_files_short   = train_files[:100]

## Cascade classifiers
CLF_CASCADE_ALT2 = cv2.CascadeClassifier(CASCADE_ALT2)
CLF_CASCADE_TREE = cv2.CascadeClassifier(CASCADE_TREE)

# counters
humans_alt2, humans_tree = 0, 0
dogs_alt2, dogs_tree     = 0, 0

# let's find humans
print('Looking at humans dataset...')
for h in human_files_short:
    if detect_face(h, CLF_CASCADE_ALT2):
        humans_alt2 += 1
    if detect_face(h, CLF_CASCADE_TREE):
        humans_tree += 1

print('Looking at dogs dataset...')
for d in dog_files_short:
    if detect_face(d, CLF_CASCADE_ALT2):
        dogs_alt2 += 1
    if detect_face(d, CLF_CASCADE_TREE):
        dogs_tree += 1

# results
print('Using ALT2 Cascade, found {}% Human faces'.format(humans_alt2))
print('Using ALT2 Cascade, found {}% Dog faces'.format(dogs_alt2))
print()
print('Using ALT_TREE Cascade, found {}% Human faces'.format(humans_tree))
print('Using ALT_TREE Cascade, found {}% Dog faces'.format(dogs_tree))
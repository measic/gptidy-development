### TODO: Test the performance of the dog_detector function
### on the images in human_files_short and dog_files_short.

humans, dogs = 0, 0

print('Looking for dogs in Humans dataset..')
for h in human_files_short:
    if dog_detector(h):
        humans += 1
print('Looking for dogs in Dogs dataset...')
for d in dog_files_short:
    if dog_detector(d):
        dogs +=1
print('In Humans dataset, found {}% dogs'.format(humans))
print('In Dogs dataset, found {}% dogs'.format(dogs))
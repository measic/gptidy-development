human_files_short = human_files[:100]
dog_files_short   = train_files[:100]
# Do NOT modify the code above this line.

## TODO: Test the performance of the face_detector algorithm 
## on the images in human_files_short and dog_files_short.

num_humans = 0
num_dogs = 0

for h in human_files_short:
    if face_detector(h):
        num_humans += 1
        
for d in dog_files_short:
    if face_detector(d):
        num_dogs += 1

print('Found {}% Human faces'.format(num_humans))
print('Found {}% Dog faces'.format(num_dogs))
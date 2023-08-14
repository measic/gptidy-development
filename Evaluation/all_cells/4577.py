# A simple for loop to find sum of all odd numbers up to 99
counter = 0

for i in range(100):
    if i % 2:
        counter += i
        
print(counter)
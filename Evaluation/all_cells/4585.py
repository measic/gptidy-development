# do the list comprehension explicitly
result = []
for i in range(1, 101):
    if i % 3 == 0:
        result.append(i)
        
print(result)
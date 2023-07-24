import csv

with open("영화평점.csv", "wt", encoding="cp949", newline='\n') as f:
    writer = csv.writer(f)

#     for i in range(10):
#         writer.writerow(['원더', 9.41])
#         writer.writerow(['위대한 쇼맨', 9.39])

#     for movie in movies:
#         writer.writerow(movie)

    writer.writerows(movies)
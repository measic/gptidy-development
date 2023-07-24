#reconstruct dataset
X = []
T = []

for i,c in enumerate(norare_conv):

    for j,s in enumerate(c):

        if j == (len(c)-1):
            break
        else:
            X.append(s)
            T.append(norare_conv[i][j+1])
stickwidth = 4
for i in range(17):
    for n in range(len(subset)):
        index = subset[n][np.array(limbSeq[i]) - 1]
        if -1 in index:
            continue
        cur_canvas = canvas.copy()
        variable_def = candidate[index.astype(int), 0]
        X = candidate[index.astype(int), 1]
        mX = np.mean(X)
        mY = np.mean(variable_def)
        length = ((X[0] - X[1]) ** 2 + (variable_def[0] - variable_def[1]) ** 2) ** 0.5
        angle = math.degrees(math.atan2(X[0] - X[1], variable_def[0] - variable_def[1]))
        polygon = cv.ellipse2Poly((int(mY), int(mX)), (int(length / 2), stickwidth), int(angle), 0, 360, 1)
        cv.fillConvexPoly(cur_canvas, polygon, colors[i])
        canvas = cv.addWeighted(canvas, 0.4, cur_canvas, 0.6, 0)
plt.imshow(canvas[:, :, [2, 1, 0]])
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(12, 12)
variable_def = (x < 400) & (x >= 300) & (y >= 300) & (y <= 400)
img[variable_def] = 0
line1 = y >= 350 - 0.5 * (x - 300)
line2 = y <= 350 + 1.0 * (x - 300)
line3 = y <= 400 - 2.0 * (x - 350)
img[line1 & line2 & line3 & variable_def] = 1
plt.imshow(img, interpolation='bilinear')
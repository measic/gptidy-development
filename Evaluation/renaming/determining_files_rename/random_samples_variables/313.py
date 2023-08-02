box = (x < 400) & (x >= 300) & (y >= 300) & (y <= 400)
variable_def[box] = 0
line1 = y >= 350 - 0.5 * (x - 300)
line2 = y <= 350 + 1.0 * (x - 300)
line3 = y <= 400 - 2.0 * (x - 350)
variable_def[line1 & line2 & line3 & box] = 1
plt.imshow(variable_def, interpolation='bilinear')
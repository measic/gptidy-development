# reload(accuracy)
reload(slope)
plt.close()
f = plt.figure(figsize=(5, 4))

le = .12
re = .02
te = .1
be = .11
h_gap = .13

w = .5
h = 1. - te - be

ax_lines = f.add_axes([le, be, w, h])
ax_slopes = f.add_axes([le + w + h_gap, be, 1. - w - h_gap - le - re, h])

key = fracs[-1]

slope.plot_cv_slope(subjects, deep_all, linear_all, chance[0], training_size, fracs, (ax_lines, ax_slopes),
                    legend=True, normalize_chance=False)

x0 = .05
y0 = 1. - te + .02
x1 = le + w + h_gap - .075

f.text(x0, y0, 'A', **letter_fontstyle)
f.text(x1, y0, 'B', **letter_fontstyle)

plt.savefig(os.path.join(os.environ['HOME'], 'Downloads/slope2.eps'), dpi=300)
plt.savefig(os.path.join(os.environ['HOME'], 'Downloads/slope2.png'), dpi=300)
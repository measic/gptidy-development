X, Annotations = marconi['Soccer']
camera = 3
frame = 79
fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)
im = X[camera, frame]
ax.imshow(im)
variable_def = Annotations[camera]
Annot_on_frame_cam = variable_def[frame]
COLORS = ['red', 'yellow']
for i, ((tl, br), joints) in enumerate(Annot_on_frame_cam):
    head_x, head_y = utils.tl_br_to_plt_plot(tl[1], tl[0], br[1], br[0])
    ax.plot(head_x, head_y, color=COLORS[i])
    for jx, jy, visible in joints:
        plt.scatter(jx, jy, color=COLORS[i], alpha=1 if visible == 1 else 0.4)
plt.axis('off')
plt.show()
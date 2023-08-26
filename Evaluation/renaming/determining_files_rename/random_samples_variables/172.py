X, Annotations = marconi['Kickbox']
camera = 0
variable_def = 0
fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111)
im = X[camera, variable_def]
ax.imshow(im)
Annotations_for_cam = Annotations[camera]
Annot_on_frame_cam = Annotations_for_cam[variable_def]
COLORS = ['red', 'yellow']
for i, ((tl, br), joints) in enumerate(Annot_on_frame_cam):
    head_x, head_y = utils.tl_br_to_plt_plot(tl[1], tl[0], br[1], br[0])
    ax.plot(head_x, head_y, color=COLORS[i])
    for jx, jy, visible in joints:
        plt.scatter(jx, jy, color=COLORS[i], alpha=1 if visible == 1 else 0.4)
plt.axis('off')
plt.show()
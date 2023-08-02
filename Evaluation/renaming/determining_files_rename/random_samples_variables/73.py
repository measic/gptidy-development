X, Annotations = marconi['Soccer']
fig = plt.figure(figsize=(16, 4))

def get_annot_img(ax, camera, frame):
    ax.set_title('Camera ' + str(camera) + ' at frame ' + str(frame))
    im = X[camera, frame]
    ax.imshow(im)
    Annotations_for_cam = Annotations[camera]
    Annot_on_frame_cam = Annotations_for_cam[frame]
    COLORS = ['red', 'yellow']
    for i, ((tl, br), joints) in enumerate(Annot_on_frame_cam):
        head_x, head_y = utils.tl_br_to_plt_plot(tl[1], tl[0], br[1], br[0])
        ax.plot(head_x, head_y, color=COLORS[i])
        for jx, jy, visible in joints:
            ax.scatter(jx, jy, color=COLORS[i], alpha=1 if visible == 1 else 0.4)
get_annot_img(fig.add_subplot(121), 0, 0)
get_annot_img(fig.add_subplot(122), 1, 0)
plt.axis('off')
plt.show()
Ps, Ks, variable_def = marconi.get_calibration('Soccer', split_intrinsic_extrinsic=True)
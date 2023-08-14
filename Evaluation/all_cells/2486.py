fig = plt.figure(figsize=(8,6))
fig.subplots_adjust(left=None, bottom=None, right=None, top=None,
                    wspace=0.25, hspace=0.25)
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, mfusghead[0, 0, :], linewidth=0.75, color='blue', label='MODFLOW-USG')
ax.fill_between(x, y1=botm[1, 0, :], y2=-5, color='0.5', alpha=0.5)
leg = ax.legend(loc='upper right')
leg.draw_frame(False)
ax.set_xlabel('Horizontal distance, in m')
ax.set_ylabel('Head, in m')
ax.set_ylim(-5,25);
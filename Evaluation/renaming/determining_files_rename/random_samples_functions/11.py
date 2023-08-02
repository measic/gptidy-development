def function_def(img, rgb_thresh=(160, 160, 160)):
    color_select = np.zeros_like(img[:, :, 0])
    above_thresh = (img[:, :, 0] > rgb_thresh[0]) & (img[:, :, 1] > rgb_thresh[1]) & (img[:, :, 2] > rgb_thresh[2])
    color_select[above_thresh] = 1
    return color_select
threshed = function_def(warped)
plt.imshow(threshed, cmap='gray')
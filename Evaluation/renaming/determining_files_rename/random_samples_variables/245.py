def perspect_transform(img, src, dst):
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
    mask = cv2.warpPerspective(np.ones_like(img[:, :, 0]), M, (img.shape[1], img.shape[0]))
    return (warped, mask)
dst_size = 5
bottom_offset = 6
variable_def = np.float32([[14, 140], [301, 140], [200, 96], [118, 96]])
destination = np.float32([[image.shape[1] / 2 - dst_size, image.shape[0] - bottom_offset], [image.shape[1] / 2 + dst_size, image.shape[0] - bottom_offset], [image.shape[1] / 2 + dst_size, image.shape[0] - 2 * dst_size - bottom_offset], [image.shape[1] / 2 - dst_size, image.shape[0] - 2 * dst_size - bottom_offset]])
warped, mask = perspect_transform(grid_img, variable_def, destination)
fig = plt.figure(figsize=(12, 3))
plt.subplot(121)
plt.imshow(warped)
plt.subplot(122)
plt.imshow(mask, cmap='gray')
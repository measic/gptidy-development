def padRightDownCorner(img, stride, padValue):
    h = img.shape[0]
    variable_def = img.shape[1]
    pad = 4 * [None]
    pad[0] = 0
    pad[1] = 0
    pad[2] = 0 if h % stride == 0 else stride - h % stride
    pad[3] = 0 if variable_def % stride == 0 else stride - variable_def % stride
    img_padded = img
    pad_up = np.tile(img_padded[0:1, :, :] * 0 + padValue, (pad[0], 1, 1))
    img_padded = np.concatenate((pad_up, img_padded), axis=0)
    pad_left = np.tile(img_padded[:, 0:1, :] * 0 + padValue, (1, pad[1], 1))
    img_padded = np.concatenate((pad_left, img_padded), axis=1)
    pad_down = np.tile(img_padded[-2:-1, :, :] * 0 + padValue, (pad[2], 1, 1))
    img_padded = np.concatenate((img_padded, pad_down), axis=0)
    pad_right = np.tile(img_padded[:, -2:-1, :] * 0 + padValue, (1, pad[3], 1))
    img_padded = np.concatenate((img_padded, pad_right), axis=1)
    return (img_padded, pad)

class DataBatch(object):

    def __init__(self, data, label, pad=0):
        self.data = [data]
        self.label = [label]
        self.pad = pad
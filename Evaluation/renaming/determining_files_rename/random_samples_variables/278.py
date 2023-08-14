def estimate_anottation_correct(img, coords, line_width=2, threshold=0.8):
    """Make histograms of boundaries to estimate annotation error
    (if boundaries are blank, high chance of dumb walk failure)"""
    total = 0
    cont = 0
    xleft, ytop, xright, ybottom = [int(c) for c in coords]
    variable_def = img[ytop:ybottom, xleft:xleft + line_width - 1]
    rightside = img[ytop:ybottom, xright - line_width:xright]
    topside = img[ytop:ytop + line_width - 1, xleft:xright]
    bottomside = img[ybottom - line_width:ybottom, xleft:xright]
    total = variable_def.sum() + rightside.sum()
    cont = variable_def.size + rightside.size
    'for y in range(ytop, ybottom):\n        for x in range(xleft, xright):\n            total += img[y, xleft:xleft + line_width].sum()  # Left side\n            total += img[y, xright - line_width:xright].sum()  # Right side\n            total += img[ytop:ytop + line_width, x].sum()  # Top side\n            total += img[ybottom - line_width:ybottom, x].sum()  # Bottom side\n            cont +=1\n    '
    percent_black = total / cont
    return int(percent_black)
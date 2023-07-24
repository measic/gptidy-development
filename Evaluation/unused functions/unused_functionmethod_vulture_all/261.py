# 8 Pipeline 
def estimate_anottation_correct(img, coords, line_width=2, threshold=0.8):
    """Make histograms of boundaries to estimate annotation error
    (if boundaries are blank, high chance of dumb walk failure)"""
    total = 0
    cont = 0
    xleft, ytop, xright, ybottom = [int(c) for c in coords]
    leftside = img[ytop:ybottom, xleft:xleft + line_width - 1]
    rightside = img[ytop:ybottom, xright - line_width:xright]
    topside = img[ytop:ytop + line_width - 1, xleft:xright]
    bottomside = img[ybottom - line_width:ybottom, xleft:xright]
    total = leftside.sum() + rightside.sum() #+ topside.sum() + bottomside.sum()
    cont = leftside.size + rightside.size #+ topside.size + bottomside.size
    """for y in range(ytop, ybottom):
        for x in range(xleft, xright):
            total += img[y, xleft:xleft + line_width].sum()  # Left side
            total += img[y, xright - line_width:xright].sum()  # Right side
            total += img[ytop:ytop + line_width, x].sum()  # Top side
            total += img[ybottom - line_width:ybottom, x].sum()  # Bottom side
            cont +=1
    """
    percent_black =  total / cont 
    return int(percent_black)

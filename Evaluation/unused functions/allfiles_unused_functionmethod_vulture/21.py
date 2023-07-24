#apply style function to highlight max values
def highlight_min(s):
    '''
    highlight the minimum in a Series pink.
    '''
    is_min = s == s.min()
    return ['background-color: pink' if v else '' for v in is_min]
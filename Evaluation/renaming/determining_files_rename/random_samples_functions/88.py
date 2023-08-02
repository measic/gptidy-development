def function_def(s):
    """
    highlight the minimum in a Series pink.
    """
    is_min = s == s.min()
    return ['background-color: pink' if v else '' for v in is_min]
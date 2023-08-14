def friction(vi, vf, F0):
    """
    Returns the friction of the bottom plate against blocks moving at a specific velocity
    
    Arguments:  vi - initial velocity of the block
                vf - final velocity of the block
                F0 - the static friction force
    
    Returned: The force due to friction
    
    Examples:
    
    >>> friction (0, 1, 20)
    -20.0
    
    >>> friction (1, 1, 20)
    -10.0
    """
    if vi == 0:
        sign = 1
    else:
        sign = vi / abs(vi)
    variable_def = -(F0 * sign / (1 + abs(vi / vf)))
    return variable_def
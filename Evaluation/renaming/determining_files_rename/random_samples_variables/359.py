def blockMotionVaryingMasses(t, blockPositions, vBlock, i, blockNum, kp, kc, mass, F0, v0, vf):
    """
    Returns the differential equation that models the motion of the blocks
    
    Arguments:  t - time
                blockPositions - the positions of the blocks
                vBlock - the velocity of the block
                i - the index of the current block
                blockNum - the number of blocks
                kp - spring constant of leaf springs
                kc - spring constant of springs between blocks
                mass - masses of individual blocks
                F0 - the static friction force
                v0 - initial velocity of top plate
                vf - the friction coefficient
                
    Returned: The differential equation modeling the motion of the individual blocks
    
    Examples:
    
    >>> blockMotion (0, (0, 1, 2, 3, 4), 0, 2, 5, 0, 0, 1, 0, 1, 20)
    array([ 0.,  0.])
    
    """
    xi = blockPositions[i] - i
    vi = vBlock
    variable_def = mass[i]
    if i == 0:
        xiP = blockPositions[i + 1] - (i + 1)
        springForce = kc * (xiP - xi) + kp * (v0 * t - xi)
    elif i == blockNum - 1:
        xiM = blockPositions[i - 1] - (i - 1)
        springForce = kc * (xiM - xi) + kp * (v0 * t - xi)
    else:
        xiM = blockPositions[i - 1] - (i - 1)
        xiP = blockPositions[i + 1] - (i + 1)
        springForce = kc * (xiP + xiM - 2 * xi) + kp * (v0 * t - xi)
    frictionForce = friction(vi, vf, F0)
    if abs(springForce) <= abs(frictionForce):
        dv = -vi
        vi = 0
        dx = vi
    else:
        totalForce = (springForce + frictionForce) / variable_def
        dx = vi
        dv = totalForce
    return np.array([dx, dv], float)
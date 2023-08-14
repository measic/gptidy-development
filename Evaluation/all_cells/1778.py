#######################################################################
# Copyright (C)                                                       #
# 2016 Shangtong Zhang(zhangshangtong.cpp@gmail.com)                  #
# 2016 Kenta Shimada(hyperkentakun@gmail.com)                         #
# Permission given to modify the code as long as you keep this        #
# declaration at the top                                              #
#######################################################################

def create_gridworld(world_size, terminal_states):
    """
    world_size: height and width of the squared-shape gridworld
    return
        actions: list of str, possible actions
        states: list of coordinate tuples representing all non-terminal states
        nextState: list of list of dict, index 3 times to return the next state coordinate tuple
    """

    # left, up, right, down
    actions = ['L', 'U', 'R', 'D']

    # Next
    nextState = []
    for i in range(0, world_size):
        nextState.append([])
        for j in range(0, world_size):
            # Creates a dictionnary that
            next = dict()
            if i == 0:
                next['U'] = (i, j)
            else:
                next['U'] = (i - 1, j)

            if i == world_size - 1:
                next['D'] = (i, j)
            else:
                next['D'] = (i + 1, j)

            if j == 0:
                next['L'] = (i, j)
            else:
                next['L'] = (i, j - 1)

            if j == world_size - 1:
                next['R'] = (i, j)
            else:
                next['R'] = (i, j + 1)

            nextState[i].append(next)
            
    states = []
    for i in range(0, world_size):
        for j in range(0, world_size):
            if (i,j) in terminal_states:
                continue
            else:
                states.append((i, j))
                
    return actions, states, nextState
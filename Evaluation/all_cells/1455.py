def location(moves, prev_loc, move_vec, verbose=False):
    new_loc = prev_loc + move_vec
    if verbose:
        print("new location", new_loc)
    moves = moves + 1
    return moves, new_loc


move_counter = 0
knight_loc = np.array([2,20])
bishop_loc = np.array([5,6])
print("knight's move")
move_counter, knight_loc = location(move_counter, knight_loc, [1,2], True)
print("bishop's move")
move_counter, bishop_loc = location(move_counter, bishop_loc, [-1,3])
print("Number of moves", move_counter)
print('Done moving')

def location_check(moves, prev_loc, move_vec, verbose=False, game_limit=10):
    if moves >= game_limit:
        if verbose:
            print("Game over!")
        return moves, prev_loc
    else:    
        new_loc = prev_loc + move_vec
        moves = moves + 1
        if verbose:
            print("new location", new_loc)
        return moves, new_loc


move_counter = 5
knight_loc = np.array([2,20])
bishop_loc = np.array([5,6])
print("bishop's move")
move_counter, bishop_loc = location_check(move_counter, bishop_loc, [-1,3], verbose=True, game_limit = 25)
print("knight's move")
move_counter, knight_loc = location_check(move_counter, knight_loc, [1,2], verbose=True)
print("bishop's move")
# optional arguments are in different order than in function definiton. And the results are stored in a mylist instead of individually.
mylist = location_check(move_counter, bishop_loc, [-5,4], game_limit = 6, verbose=True)
print(mylist)
print("Number of moves", mylist[0])  #extract moves from list returned by function location_check()
print('Done moving')
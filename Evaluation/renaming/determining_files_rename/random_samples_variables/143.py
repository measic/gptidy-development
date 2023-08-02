def calc_other_neighbour_msg_prod(sender, receiver):
    variable_def = get_neighbour_messages(sender, receiver)
    return np.multiply.reduce(np.ix_(*variable_def))
def calc_other_neighbour_msg_prod(sender, receiver):
    vectors = get_neighbour_messages(sender, receiver)
#     print(vectors)
    return np.multiply.reduce(np.ix_(*vectors))
    
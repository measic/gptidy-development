def marginalize_max(P, dim):
    return np.amax(P, axis=tuple(set(range(P.ndim)) - {dim}))

def function_def(sender, receiver):
    vectors = get_neighbour_messages(sender, receiver)
    return np.add.reduce(np.ix_(*vectors))

def calculate_log_factor(f_neighb_first, neighbour_msg_prod):
    return np.log(f_neighb_first) + neighbour_msg_prod

def calc_max_sum_factor_to_variable_msg(factor, variable):
    neighbour_msg_prod = function_def(factor, variable)
    f_neighb_first = move_dimension_first(factor.f, factor.neighbours.index(variable))
    return marginalize_max(calculate_log_factor(f_neighb_first, neighbour_msg_prod), 0)

def factor_send_ms_msg(self, variable):
    assert isinstance(variable, Variable), 'Factor can only send messages to variable!'
    assert can_send_message(self, variable), 'Cannot send message!'
    out_msg = calc_max_sum_factor_to_variable_msg(self, variable)
    variable.receive_msg(self, out_msg)
    self.pending.discard(variable)
Factor.send_ms_msg = factor_send_ms_msg
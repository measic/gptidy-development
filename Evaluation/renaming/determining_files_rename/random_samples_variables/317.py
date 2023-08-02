def calc_max_sum_variable_to_factor_msg(variable, factor):
    neighbour_msg_prod = get_neighbour_messages(variable, factor)
    if len(neighbour_msg_prod) > 0:
        variable_def = np.sum(np.array(neighbour_msg_prod), axis=0)
    else:
        variable_def = np.zeros(variable.num_states)
    variable_def += np.log(variable.observed_state)
    return variable_def

def variable_send_ms_msg(self, factor):
    assert isinstance(factor, Factor), 'Variable can only send messages to factor!'
    assert can_send_message(self, factor), 'Cannot send message!'
    out_msg = calc_max_sum_variable_to_factor_msg(self, factor)
    factor.receive_msg(self, out_msg)
    self.pending.discard(factor)
Variable.send_ms_msg = variable_send_ms_msg
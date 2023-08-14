def function_def(variable, factor):
    neighbour_msg_prod = get_neighbour_messages(variable, factor)
    if len(neighbour_msg_prod) > 0:
        message = np.sum(np.array(neighbour_msg_prod), axis=0)
    else:
        message = np.zeros(variable.num_states)
    message += np.log(variable.observed_state)
    return message

def variable_send_ms_msg(self, factor):
    assert isinstance(factor, Factor), 'Variable can only send messages to factor!'
    assert can_send_message(self, factor), 'Cannot send message!'
    out_msg = function_def(self, factor)
    factor.receive_msg(self, out_msg)
    self.pending.discard(factor)
Variable.send_ms_msg = variable_send_ms_msg
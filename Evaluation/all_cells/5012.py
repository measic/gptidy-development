# ANSWER 2.2
def calc_max_sum_variable_to_factor_msg(variable, factor):
    
    neighbour_msg_prod = get_neighbour_messages(variable, factor)
    
    if len(neighbour_msg_prod) > 0:
        message = np.sum(np.array(neighbour_msg_prod), axis=0)
    else:
        message = np.zeros(variable.num_states)
    
#     for i in range(variable.num_states):
#         if variable.observed_state[i] < 0.1:
#             message[i] = -1e10
    
    message += np.log(variable.observed_state)
    
    return message
    
    
    
def variable_send_ms_msg(self, factor):
    
    assert isinstance(factor, Factor), "Variable can only send messages to factor!"
    assert can_send_message(self, factor), "Cannot send message!"
    
    out_msg = calc_max_sum_variable_to_factor_msg(self, factor)
    
    # Send the message
    factor.receive_msg(self, out_msg)
    
    # Remove the pending sign if present
    self.pending.discard(factor)

Variable.send_ms_msg = variable_send_ms_msg

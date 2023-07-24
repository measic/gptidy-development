# Finally, we will define the send message function for you
def factor_send_sp_msg(self, variable):
    
    assert isinstance(variable, Variable), "Factor can only send messages to variable!"
    assert can_send_message(self, variable), "Cannot send message!"
    
    out_msg = calc_sum_product_factor_to_variable_msg(self, variable)
    
    # Send the message
    variable.receive_msg(self, out_msg)
    
    # Remove the pending sign if present
    self.pending.discard(variable)
    
Factor.send_sp_msg = factor_send_sp_msg

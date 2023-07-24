# Finally, we will define the send message function for you
def variable_send_sp_msg(self, factor):
    
    assert isinstance(factor, Factor), "Variable can only send messages to factor!"
    assert can_send_message(self, factor), "Cannot send message!"
    
    out_msg = calc_sum_product_variable_to_factor_msg(self, factor)
    
    # Send the message
    factor.receive_msg(self, out_msg)
    
    # Remove the pending sign if present
    self.pending.discard(factor)
    
Variable.send_sp_msg = variable_send_sp_msg

def function_def(self, variable):
    assert isinstance(variable, Variable), 'Factor can only send messages to variable!'
    assert can_send_message(self, variable), 'Cannot send message!'
    out_msg = calc_sum_product_factor_to_variable_msg(self, variable)
    variable.receive_msg(self, out_msg)
    self.pending.discard(variable)
Factor.send_sp_msg = function_def
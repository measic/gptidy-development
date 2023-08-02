def function_def(self, factor):
    assert isinstance(factor, Factor), 'Variable can only send messages to factor!'
    assert can_send_message(self, factor), 'Cannot send message!'
    out_msg = calc_sum_product_variable_to_factor_msg(self, factor)
    factor.receive_msg(self, out_msg)
    self.pending.discard(factor)
Variable.send_sp_msg = function_def
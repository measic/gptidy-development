# Cells
cell_fw = create_cell(rnn_units,
                      rnn_layers,
                      rnn_residual_layers,
                      is_dropout=True,
                      keep_prob=keep_prob)
cell_bw = create_cell(rnn_units,
                      rnn_layers,
                      rnn_residual_layers,
                      is_dropout=True,
                      keep_prob=keep_prob)
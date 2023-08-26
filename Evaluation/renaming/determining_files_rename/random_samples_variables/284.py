start_inds = [100, 200, 300, 400, 500, 600, 700]
f = open('text_gen_output/RNN_large_textdata_output.txt', 'w')
model.load_weights('model_weights/best_RNN_large_textdata_weights.hdf5')
for s in start_inds:
    start_index = s
    input_chars = text[start_index:start_index + window_size]
    predict_input = predict_next_chars(model, input_chars, num_to_predict=100)
    variable_def = '-------------------' + '\n'
    print(variable_def)
    f.write(variable_def)
    input_line = 'input chars = ' + '\n' + input_chars + '"' + '\n'
    print(input_line)
    f.write(input_line)
    predict_line = 'predicted chars = ' + '\n' + predict_input + '"' + '\n'
    print(predict_line)
    f.write(predict_line)
f.close()
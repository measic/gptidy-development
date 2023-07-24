for model_name, model in [('linux_lstm', model_lstm), ('linux_gru', model_gru)]:
    print("MODEL: ", model_name)
    full_test(model, hypothesis_inside_quotation, 'Inside Quotation',
              train_len=95, test_len=10, ex_name='inside_quotation'.format(model_name))
    full_test(model, hypothesis_comments, 'Comments',
              train_len=95, test_len=10, ex_name='{}_inside_comments'.format(model_name))
    full_test(model, lambda x: hypothesis_indentation(x, 1), 'Indentation level 1',
              train_len=95, test_len=10, ex_name='{}_inside_indent_1'.format(model_name))
    full_test(model, lambda x: hypothesis_indentation(x, 2), 'Indentation level 2',
              train_len=95, test_len=10, ex_name='{}_inside_indent_2'.format(model_name))
    full_test(model, lambda x: hypothesis_indentation(x, 3), 'Indentation level 3',
              train_len=95, test_len=10, ex_name='{}_inside_indent_3'.format(model_name))
    full_test(model, hypothesis_inside_parantheses, 'Inside Parantheses',
              train_len=95, test_len=10, ex_name='{}_inside_parantheses'.format(model_name))
if use_attention is False:
    all_decoded = []
    for beam_i in range(beam_width):
        inputs = []
        all_decoded.append([])
        decoded = decode_ids(input_ids, bm_output_ids[:,:,beam_i])
        for dec in decoded:
            all_decoded[-1].append(dec[1])
            inputs.append(dec[0])

    print('\n'.join(
        '{} ---> {}'.format(inputs[i], ' / '.join(d[i] for d in all_decoded))
                            for i in range(len(inputs))
    ))
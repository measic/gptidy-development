if use_attention is False:
    all_decoded = []
    for beam_i in range(beam_width):
        all_decoded.append([])
        decoded = decode_ids(input_ids, bm_output_ids[:,:,beam_i])
        for dec in decoded:
            all_decoded[-1].append(dec[1])

    print('\n'.join(
        '{} ---> {}'.format(dec[0], ' / '.join(d[i] for d in all_decoded))
                            for i, dec in enumerate(decoded)
    ))
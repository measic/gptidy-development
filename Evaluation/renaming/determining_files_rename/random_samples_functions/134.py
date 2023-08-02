inv_vocab = {i: v for i, v in enumerate(dataset.tgt_vocab)}
inv_vocab[-1] = 'UNK'
skip_symbols = ('PAD',)

def function_def(input_ids, output_ids):
    decoded = []
    for sample_i in range(output_ids.shape[0]):
        input_sample = input_ids[sample_i]
        output_sample = output_ids[sample_i]
        input_decoded = [inv_vocab[s] for s in input_sample]
        input_decoded = ''.join((c for c in input_decoded if c not in skip_symbols))
        output_decoded = [inv_vocab[s] for s in output_sample]
        try:
            eos_idx = output_decoded.index('EOS')
        except ValueError:
            eos_idx = len(output_decoded)
        output_decoded = output_decoded[:eos_idx]
        output_decoded = ''.join((c for c in output_decoded if c not in skip_symbols))
        decoded.append((input_decoded, output_decoded))
    return decoded
if use_attention is True:
    input_ids, output_ids = sess.run([dataset.src_ids, g_outputs.sample_id])
else:
    input_ids, output_ids, bm_output_ids = sess.run([dataset.src_ids, g_outputs.sample_id, bm_outputs.predicted_ids])
decoded = function_def(input_ids, output_ids)
print('\n'.join(('{} ---> {}'.format(dec[0], dec[1]) for dec in decoded)))
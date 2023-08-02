# start off with simplest case for proof of concept
wave1_coeffs = {
    'amplitude': {'mean': 0.5, 'delta': 0.05}, 
    'frequency': {'mean': 1.0, 'delta': 0.1},
    'offset': {'mean': 0.0, 'delta': 0.1}, 
    'phase': {'mean': 0.0, 'delta': 1.0},
    'name': 'A',
    'color': '#0000ff'
}
wave2_coeffs = {
    'amplitude': {'mean': 0.75, 'delta': 0.075}, 
    'frequency': {'mean': 3.0, 'delta': 0.3},
    'offset': {'mean': 0.0, 'delta': 0.1}, 
    'phase': {'mean': 0.0, 'delta': 1.0},
    'name': 'B',
    'color': '#ff0000',
#     'time': {'t_min': 0, 't_max': 5, 'n_timestamps': 601, 'noise_type': 'pareto', 'pareto_shape': 1.3},
}
wave3_coeffs = {
    'amplitude': {'mean': 1.0, 'delta': 0.1}, 
    'frequency': {'mean': 8.0, 'delta': 0.8},
    'offset': {'mean': 0.0, 'delta': 0.2}, 
    'phase': {'mean': 0.0, 'delta': 1.0},
    'name': 'C',
    'color': '#00ff00'
}
wave4_coeffs = {
    'amplitude': {'mean': 1.4, 'delta': 0.1}, 
    'frequency': {'mean': 12.0, 'delta': 1.2},
    'offset': {'mean': 0.0, 'delta': 0.2}, 
    'phase': {'mean': 0.0, 'delta': 1.0},
    'name': 'D',
    'color': '#ff00ff'
}

mwave_coeffs = {
    'amplitude': {'mean': 1.0, 'delta': 0}, 
    'frequency': {'mean': 1.0, 'delta': 0}, 
    'offset': {'mean': 0, 'delta': 0},
    'phase': {'mean': 0, 'delta': 1}, 
    'name': 'mixed_wave',
    'time': {'t_min': 0, 't_max': 2, 'n_timestamps': 4096, 'delta': 0}
}

sigs_coeffs = [wave1_coeffs, wave2_coeffs, wave3_coeffs, mwave_coeffs, wave4_coeffs]

features=('x', 'dxdt')[0]
batch_size = 128
window_size = 4096
window_type = 'sliding'
network_type = 'TCN'
sequence_type = 'many2many'

msig = MixedSignal(
    sigs_coeffs, 
    *features,
    window_size=window_size, 
    window_type=window_type, 
    network_type=network_type,
    sequence_type=sequence_type,
)

msig.generate()
n_classes = msig.n_classes
n_features = msig.n_features
# input_shape = (window_size, n_features) # RNN
input_shape = (None, n_features) # TCN

print(msig.inputs.shape)
print(msig.mixed_signal.shape)
print(msig.one_hots.shape)
print(msig.labels.shape)
print(msig.n_timestamps)
print(msig.n_samples)
accuracies = []

ch = chance[0, :, -1].mean(axis=-1)
da = deep_all[key][:, -1] / ch
la = linear_all[key][:, -1] / ch

for ii in range(4):
    for jj in range(10):
        accuracies.append({'subject':ii, 'accuracy':da[ii, jj],
                           'complexity': 3, 'model': 2})
        accuracies.append({'subject':ii, 'accuracy':la[ii, jj],
                           'complexity': 3, 'model': 1})
    
ch = chance[1, :, -1].mean(axis=-1)
da = other_deep_accuracy['c'][:, -1] / ch
la = other_linear_accuracy['c'][:, -1] / ch
for ii in range(4):
    for jj in range(10):
        accuracies.append({'subject':ii, 'accuracy':da[ii, jj],
                           'complexity': 2, 'model': 2})
        accuracies.append({'subject':ii, 'accuracy':la[ii, jj],
                           'complexity': 2, 'model': 1})

for ii, t in enumerate(['v', 'p', 'm']):
    ch = chance[ii+2, :, -1].mean(axis=-1)
    da = other_deep_accuracy[t][:, -1] / ch
    la = other_linear_accuracy[t][:, -1] / ch
    for jj in range(10):
        accuracies.append({'subject':ii, 'accuracy':da[ii, jj],
                           'complexity': 1, 'model': 2})
        accuracies.append({'subject':ii, 'accuracy':la[ii, jj],
                           'complexity': 1, 'model': 1})
df = pd.DataFrame.from_dict(accuracies)
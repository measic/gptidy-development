mean = np.mean(keystrokes, axis=0)
std = np.std(keystrokes, axis=0)

norm_keystrokes = (keystrokes - mean) / std
# Translate back 2 random sentences from padded_conv
padded_s = [s for c in padded_conv for s in c]
idx1, idx2 = np.random.choice(range(len(padded_s)), 2)

translate(padded_s[idx1],tokens,to_token=False), translate(padded_s[idx2],tokens,to_token=False)
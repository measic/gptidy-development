# Translate sentences to list of integers
translate_conv = copy.deepcopy(norare_conv)

for i, c in enumerate(norare_conv):
    for j, s in enumerate(c):
        words = s.split(" ")
        new_s = translate(words, tokens, to_token=True)

        # Add START and STOP tokens to every sentence
        new_s = [tokens["START"]] + new_s
        new_s.append(tokens["STOP"])

        translate_conv[i][j] = new_s
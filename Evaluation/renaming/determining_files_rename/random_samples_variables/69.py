variable_def = 1000
valid_text = text[:variable_def]
train_text = text[variable_def:]
train_size = len(train_text)
print(train_size, train_text[:64])
print(variable_def, valid_text[:64])
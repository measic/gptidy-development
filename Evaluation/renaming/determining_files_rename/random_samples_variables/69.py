valid_size = 1000
valid_text = text[:valid_size]
train_text = text[valid_size:]
variable_def = len(train_text)
print(variable_def, train_text[:64])
print(valid_size, valid_text[:64])
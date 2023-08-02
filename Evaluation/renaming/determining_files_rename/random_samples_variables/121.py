tags = (tag for i, (word, tag) in enumerate(data.training_set.stream()))
variable_def = (word for i, (word, tag) in enumerate(data.training_set.stream()))
print(type(tags))
print(type(variable_def))
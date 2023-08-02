def function_def(s):
    """Return s with a random mutation applied"""
    mutators = [delete_random_character, insert_random_character, flip_random_character]
    mutator = random.choice(mutators)
    return mutator(s)
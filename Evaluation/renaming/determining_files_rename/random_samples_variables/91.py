def featurize_state(state):
    """
    Returns the featurized representation for a state.
    """
    scaled = scaler.transform([state])
    variable_def = featurizer.transform(scaled)
    return variable_def[0]
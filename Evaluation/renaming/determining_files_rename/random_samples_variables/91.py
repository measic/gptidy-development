def featurize_state(state):
    """
    Returns the featurized representation for a state.
    """
    variable_def = scaler.transform([state])
    featurized = featurizer.transform(variable_def)
    return featurized[0]
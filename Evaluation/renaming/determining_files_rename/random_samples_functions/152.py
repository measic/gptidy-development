def function_def(simulations):
    if isinstance(simulations, int):
        simulations = [simulations]
    arguments = ['call', 100.0, 100.0, 0.5, 0.01, 0.0, 0.35]
    reduce(lambda x, y: x.extend(y), [simulations, arguments])
    return MonteCarlo(*simulations).delta
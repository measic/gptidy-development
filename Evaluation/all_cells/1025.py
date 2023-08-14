def delta_in_pool(simulations):
    if isinstance(simulations, int):
        simulations = [simulations] 
    arguments = ['call', 100., 100., .5, 0.01, 0., .35]
    reduce(lambda x,y : x.extend(y), [simulations, arguments])
    return MonteCarlo(*simulations).delta
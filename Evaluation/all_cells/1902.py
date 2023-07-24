if False:
    import gc
    gc.collect()
    objgraph.show_most_common_types()
    from pyunlocbox import solvers, functions
    %mprun -f ae.fit_transform -f ae._minD -f ae._minZ -f solvers.solve -f solvers.forward_backward._pre -f solvers.forward_backward._fista -f functions.norm_l1._prox -T profile.txt ae.fit_transform(X)
    #%mprun -f solvers.solve -f solvers.forward_backward._pre -f solvers.forward_backward._fista -f functions.norm_l1._prox -T profile.txt ae.fit_transform(X)
    gc.collect()
    objgraph.show_most_common_types()
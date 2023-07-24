tneqsys = TransformedSys.from_callback(
    partial(get_f, lnK=True), (sp.exp, sp.log), 5, 7,
    latex_names=neqsys.latex_names, latex_param_names=neqsys.latex_param_names)
tneqsys
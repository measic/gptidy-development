neqsys = SymbolicSys.from_callback(
    partial(get_f, lnK=False), n, n+len(K),
    latex_names=[r'\mathrm{[%s]}' % nam for nam in texnames],
    latex_param_names=[r'\mathrm{[%s]_0}' % nam for nam in texnames] + [r'K_{\rm w}', r'K_{\rm a}(\mathrm{NH_4^+})']
)
neqsys
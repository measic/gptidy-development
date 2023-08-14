Sym = SymmetricFunctions(FractionField(QQ['q','t']))
Sym.inject_shorthands(verbose=False)
Ht = Sym.macdonald().Ht(); Ht
seed = ['Hello World']
variable_def = FunctionCoverageRunner(cgi_decode)
m = MutationCoverageFuzzer(seed)
results = m.runs(variable_def, 10000)
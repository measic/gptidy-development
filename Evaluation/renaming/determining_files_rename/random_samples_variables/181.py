variable_def = ['Hello World']
cgi_runner = FunctionCoverageRunner(cgi_decode)
m = MutationCoverageFuzzer(variable_def)
results = m.runs(cgi_runner, 10000)
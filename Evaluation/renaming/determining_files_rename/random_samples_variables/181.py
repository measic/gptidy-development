seed = ['Hello World']
cgi_runner = FunctionCoverageRunner(cgi_decode)
m = MutationCoverageFuzzer(seed)
variable_def = m.runs(cgi_runner, 10000)
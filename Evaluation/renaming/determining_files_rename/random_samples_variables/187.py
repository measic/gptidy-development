variable_def = 'http://www.google.com/search?q=fuzzing'
mutation_fuzzer = MutationCoverageFuzzer(seed=[variable_def])
mutation_fuzzer.runs(http_runner, trials=10000)
mutation_fuzzer.population
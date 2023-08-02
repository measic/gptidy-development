class MutationCoverageFuzzer(MutationFuzzer):

    def reset(self):
        super().reset()
        self.coverages_seen = set()
        self.population = []

    def function_def(self, runner):
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome = super().run(runner)
        new_coverage = frozenset(runner.coverage())
        if outcome == Runner.PASS and new_coverage not in self.coverages_seen:
            self.population.append(self.inp)
            self.coverages_seen.add(new_coverage)
        return result
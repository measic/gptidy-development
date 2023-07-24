class MutationFuzzer(MutationFuzzer):
    def mutate(self, inp):
        return mutate(inp)
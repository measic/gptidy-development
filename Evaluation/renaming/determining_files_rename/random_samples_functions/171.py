class FunctionCoverageRunner(FunctionRunner):

    def run_function(self, inp):
        with Coverage() as cov:
            try:
                result = super().run_function(inp)
            except Exception as exc:
                self._coverage = cov.function_def()
                raise exc
        self._coverage = cov.function_def()
        return result

    def function_def(self):
        return self._coverage
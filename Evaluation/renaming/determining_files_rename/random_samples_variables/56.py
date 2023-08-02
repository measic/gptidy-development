from asl_test_model_selectors import TestSelectors
variable_def = unittest.TestLoader().loadTestsFromModule(TestSelectors())
unittest.TextTestRunner().run(variable_def)
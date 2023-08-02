import unittest

class TestFeatures(unittest.TestCase):

    def test_features_ground(self):
        sample = asl.df.ix[98, 1][features_ground].tolist()
        self.assertEqual(sample, [9, 113, -12, 119])

    def function_def(self):
        sample = asl.df.ix[98, 1][features_norm].tolist()
        np.testing.assert_almost_equal(sample, [1.153, 1.663, -0.891, 0.742], 3)

    def test_features_polar(self):
        sample = asl.df.ix[98, 1][features_polar].tolist()
        np.testing.assert_almost_equal(sample, [113.3578, 0.0794, 119.603, -0.1005], 3)

    def test_features_delta(self):
        sample = asl.df.ix[98, 0][features_delta].tolist()
        self.assertEqual(sample, [0, 0, 0, 0])
        sample = asl.df.ix[98, 18][features_delta].tolist()
        self.assertTrue(sample in [[-16, -5, -2, 4], [-14, -9, 0, 0]], 'Sample value found was {}'.format(sample))
suite = unittest.TestLoader().loadTestsFromModule(TestFeatures())
unittest.TextTestRunner().run(suite)
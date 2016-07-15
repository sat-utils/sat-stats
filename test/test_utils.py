import unittest
from satstats import utils

def TestUtils(unittest.TestCase):

    s3key = ''
    vectors = None

    def test_get_stats(self):
        """ Get statistics for vector """
        stats = utils.get_stats(self.s3key, vectors)
        self.assertTrue(stats is not None)

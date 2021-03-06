'''
Created on Dec 13, 2013

@author: mkiyer
'''
import unittest

# third party packages
import numpy as np

# local imports
from ssea.lib.base import Result
from ssea.lib.kernel import RandomState
from ssea.lib.config import Config
from ssea.lib.algo import ssea_run

class TestAlgo(unittest.TestCase):

    def test_default_result(self):
        result = Result.default()
        self.assertTrue(result.t_id is None)
        self.assertTrue(result.ss_rank is None)
    
    def test_num_perms(self):
        # constants
        nsamples = 1000
        seed = 235908223
        perms = 245
        # configuration
        counts = np.arange(1, nsamples+1, dtype=np.float)
        membership = [0,0,0,1,1,1,0,0,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,0,
                      0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,
                      0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,
                      0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,
                      1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,
                      1,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,
                      0,0,0,1,0,0,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,
                      1,0,1,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,0,1,0,0,0,0,0,1,1,
                      1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,
                      1,1,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,
                      1,1,1,0,1,1,1,0,0,0,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,1,1,
                      1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,1,1,0,
                      1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,
                      0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,
                      1,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,1,0,0,1,
                      1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,
                      1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,
                      1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,0,1,0,
                      0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,0,1,
                      0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,
                      0,0,1,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,
                      1,1,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,
                      0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,1,0,1,1,1,0,
                      1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,1,
                      0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,1,
                      0,1,0,1,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,0,1,
                      1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,
                      1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,
                      0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,0,
                      0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,
                      1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,1,1,
                      0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,
                      1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,
                      0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,0,1,
                      0,1,1,1,0,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,
                      0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,1,1,0,1,
                      0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,0,1,1,1]
        membership = np.array(membership, dtype=np.int)
        size_factors = np.ones(nsamples, dtype=np.float)
        config = Config()
        config.perms = perms
        rng = RandomState(seed)
        res, null_nes_vals = ssea_run(counts, size_factors, membership, rng, config)
        # ensure correct num perms
        self.assertTrue(len(null_nes_vals) == 245)
        # ensure random number gen seed is correct
        self.assertTrue(rng.seed == 1089667133)
        self.assertAlmostEqual(res.es, -0.07231071, places=6)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
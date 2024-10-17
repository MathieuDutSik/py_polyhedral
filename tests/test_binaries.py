import unittest
from py_polyhedral.binaries import compute_isotropic_vector

class TestBinaries(unittest.TestCase):

    def test_run_compute_isotropic_vector(self):
        M_iso = [ [ -4, 4, 4 ], [ 4, -2, -3 ], [ 4, -3, -3 ] ]
        M_noniso = [ [ 15, 0, -5 ], [ 0, -1, 0 ], [ -5, 0, 2 ] ]
        output_iso = compute_isotropic_vector(M_iso)
        
        self.assertIsInstance(output, str)  # Assert that the output is a string

if __name__ == '__main__':
    unittest.main()

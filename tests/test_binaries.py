import unittest
from py_polyhedral.binaries import compute_isotropic_vector

def evaluate_is_isotropic(M, V):
    if V is None:
        return False
    n = len(M)
    esum = 0
    for i in range(n):
        for j in range(n):
            esum += M[i][j] * V[i] * V[j]
    if esum == 0:
        return True
    return False


class TestBinaries(unittest.TestCase):

    def test_run_compute_isotropic_vector_iso(self):
        M_iso = [ [ -4, 4, 4 ], [ 4, -2, -3 ], [ 4, -3, -3 ] ]
        output_iso = compute_isotropic_vector(M_iso)
        test_norm = evaluate_is_isotropic(M_iso, output_iso)
        self.assertTrue(test_norm)

    def test_run_compute_isotropic_vector_noniso(self):
        M_noniso = [ [ 15, 0, -5 ], [ 0, -1, 0 ], [ -5, 0, 2 ] ]
        output_noniso = compute_isotropic_vector(M_noniso)
        self.assertIsNone(output_noniso, msg="The matrix should not have an isotropic vector")

if __name__ == '__main__':
    unittest.main()

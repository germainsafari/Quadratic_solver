import unittest
from solver import solve_quadratic

class TestQuadraticSolver(unittest.TestCase):

    def test_two_real_roots(self):
        roots = solve_quadratic(1, -3, 2)
        self.assertEqual(roots[0], 2)
        self.assertIn(roots[1], (1.0, 2.0))
        self.assertIn(roots[2], (1.0, 2.0))

    def test_one_real_root(self):
        roots = solve_quadratic(1, 2, 1)
        self.assertEqual(roots[0], 1)
        self.assertAlmostEqual(roots[1], -1.0)
        self.assertAlmostEqual(roots[2], -1.0)

    def test_no_real_roots(self):
        roots = solve_quadratic(1, 0, 1)
        self.assertEqual(roots[0], 0)
        self.assertIsNone(roots[1])
        self.assertIsNone(roots[2])

    def test_zero_a_raises(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 3)

    def test_extreme_values(self):
        roots = solve_quadratic(1e-10, 1e-10, 1e-10)
        self.assertIn(roots[0], (0, 1, 2))  # Just checking it's handled

if __name__ == '__main__':
    unittest.main()

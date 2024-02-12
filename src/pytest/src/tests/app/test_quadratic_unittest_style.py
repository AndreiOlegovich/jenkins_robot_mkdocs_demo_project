# test_quadratic.py

import unittest
from dev.app.quadratic import quadratic_solve


class TestQuadraticUnittest(unittest.TestCase):

    def test_raises_type_error(self):
        with self.assertRaises(TypeError):
            quadratic_solve("", 1, 1.5)

    def test_result_is_tuple(self):
        res = quadratic_solve(0, 0, 0)
        self.assertEqual(type(res), tuple)
        # self.assertIsInstance(res, tuple)

    def test_zero_a_and_b(self):
        res = quadratic_solve(0, 0, 1)
        self.assertEqual(res, (None, None))

    def test_two_roots(self):
        res = quadratic_solve(1, -1, -2)
        self.assertEqual(res, (2.0, -1.0))

    def test_single_root(self):
        res = quadratic_solve(1, -2, 1)
        self.assertEqual(res, (1.0, None))


import unittest
import math
from quaternion import Quaternion

class TestQuaternionMethods(unittest.TestCase):
    def test_init(self):
        test_quat = Quaternion(10, -10, 100, 0)
        self.assertEqual(test_quat.real, 10)
        self.assertEqual(test_quat.i, -10)
        self.assertEqual(test_quat.j, 100)
        self.assertEqual(test_quat.k, 0)
        self.assertEqual(Quaternion(test_quat), test_quat)
        self.assertEqual(Quaternion(test_quat, test_quat, test_quat, test_quat), Quaternion(-80, 100, 120, -100))

    def test_str(self):
        test_quat = Quaternion(-1, 2, 3, 0)
        self.assertEqual(test_quat.__str__(), '-1+2i+3j+0k')

    def test_eq(self):
        test_quat = Quaternion(1, 2, 3, -1)
        self.assertTrue(test_quat == Quaternion(1, 2, 3, -1))
        self.assertFalse(test_quat == Quaternion(1, 2, 3, 0))

    def test_ne(self):
        test_quat = Quaternion(1, 2, 3, -1)
        self.assertTrue(test_quat != Quaternion(1, 2, 3, 0))
        self.assertFalse(test_quat != Quaternion(1, 2, 3, -1))

    def test_neg(self):
        test_quat = Quaternion(1, 2, 3, 4)
        self.assertEqual(-test_quat, Quaternion(-1, -2, -3, -4))

    def test_conjugate(self):
        test_quat = Quaternion(1, 2, 3, 4)
        testConj = Quaternion(1, -2, -3, -4)
        self.assertTrue(test_quat.conjugate() == testConj)
        self.assertTrue(test_quat.conjugate().conjugate() == test_quat)

    def test_add_radd(self):
        test_quat_left = Quaternion(1, 2, 3, 4)
        test_quat_right = Quaternion(0, 2, 3, 4)
        self.assertTrue(Quaternion(1, 4, 6, 8) == (test_quat_left + test_quat_right))
        self.assertTrue(Quaternion(1, 4, 6, 8) == (test_quat_right + test_quat_left))

    def test_sub_rsub(self):
        test_quat_left = Quaternion(1, 2, 3, 4)
        test_quat_right = Quaternion(0, 2, 3, 4)
        self.assertTrue(Quaternion(1, 0, 0, 0) == (test_quat_left - test_quat_right))
        self.assertTrue(Quaternion(-1, 0, 0, 0) == (test_quat_right - test_quat_left))

    def test_mul_rmul(self):
        test_quat_left = Quaternion(1, 2, 3, 4)
        test_quat_right = Quaternion(0, 2, 3, 4)
        self.assertTrue(Quaternion(-29, 2, 3, 4) == (test_quat_left * test_quat_right))
        self.assertTrue(Quaternion(-29, 2, 3, 4) == (test_quat_right * test_quat_left))

    def test_scalar_prod(self):
        test_quat_left = Quaternion(1, 2, 3, 4)
        test_quat_right = Quaternion(0, 2, 3, 4)
        self.assertTrue(29 == test_quat_left.scalar_prod(test_quat_right))

    def test_vector_prod(self):
        test_quat_left = Quaternion(1, 2, 3, 4)
        test_quat_right = Quaternion(0, 2, 3, 4)
        self.assertTrue(Quaternion(-29, 2, 3, 4) == test_quat_left.vector_prod(test_quat_right))

    def test_abs(self):
        test_quat = Quaternion(1, 2, 3, 4)
        self.assertTrue(abs(test_quat) == math.sqrt(30))
        test_quat = Quaternion(1, 0, 0, 0)
        self.assertTrue(abs(test_quat) == 1)

    def test_div(self):
        test_quat = Quaternion(2, 2, 4, 8)
        self.assertTrue(test_quat / 2 == Quaternion(1, 1, 2, 4))

if __name__ == '__main__':
    unittest.main(verbosity=2)
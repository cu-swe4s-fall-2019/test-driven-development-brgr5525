import unittest
import math_lib
import random as rd
import statistics as stats
import math as m


class TestMathLib(unittest.TestCase):

    def test_list_mean_no_list(self):
        r = math_lib.list_mean(None)
        self.assertEqual(r, None)

    def test_list_mean_empty_list(self):
        r = math_lib.list_mean([])
        self.assertEqual(r, None)

    def test_list_mean_const(self):
        r = math_lib.list_mean([1, 1, 1])
        self.assertEqual(r, 1)

    def test_list_mean_rand_ints(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(rd.randint(0, 100))

            r = math_lib.list_mean(L)
            e = stats.mean(L)
            self.assertEqual(r, e)

    def test_list_mean_rand_floats(self):
        L = []
        for i in range(100):
            for j in range(10):
                L.append(rd.uniform(0, 100))

            r = math_lib.list_mean(L)
            e = stats.mean(L)
            self.assertTrue(m.isclose(r, e))

    def test_list_mean_non_int_in_list(self):
        L = []
        for i in range(10):
            L.append(rd.randint(0, 100))
        L.append('X')

        with self.assertRaises(ValueError) as ex:
            math_lib.list_mean(L)

        self.assertEqual(str(ex.exception), 'Mean undefined.' +
                                            ' Unsuported value in list.')

    def test_list_mean_zero(self):
        r = math_lib.list_mean([0])
        self.assertEqual(r, 0)

    def test_list_mean_rand_ints_and_floats(self):
        L = []
        for i in range(10):
            L.append(rd.randint(0, 100))
            L.append(rd.uniform(0, 100))

        r = math_lib.list_mean(L)
        e = stats.mean(L)
        self.assertTrue(m.isclose(r, e))

    def test_list_mean_many_rand_ints_and_floats(self):
        for i in range(1000):
            L = []

            for j in range(10):
                L.append(rd.randint(0, 100))
                L.append(rd.uniform(0, 100))

            r = math_lib.list_mean(L)
            e = stats.mean(L)
            self.assertTrue(m.isclose(r, e))


if __name__ == '__main__':
    unittest.main()
